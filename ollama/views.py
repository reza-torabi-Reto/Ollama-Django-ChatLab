from django.shortcuts import render
from django.http import JsonResponse
import json
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .forms import QuestionForm
from .MyAI import gernerate_ai
from googletrans import Translator  # یا هر کتابخانه ترجمه دیگری


def get_models_from_json():
    json_file_path = os.path.join(settings.BASE_DIR, 'static', 'data', 'models_ai.json')
    try:
        with open(json_file_path, 'r') as f:
            models = json.load(f)
            return models
    except FileNotFoundError:
        return []


def write_models_to_json(models):
    json_file_path = os.path.join(settings.BASE_DIR, 'static', 'data', 'models_ai.json')
    with open(json_file_path, 'w') as f:
        json.dump(models, f, indent=4)


# @csrf_exempt
def translate_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        try:
            translator = Translator()
            translation = translator.translate(text, dest='fa').text
            return JsonResponse({'translation': translation})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)


def ollama_view(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':        
        form = QuestionForm(request.POST)
        print("OKKKK")

        if form.is_valid():
            model = form.cleaned_data['model']
            question = form.cleaned_data['question']
            _result, time_elapsed = gernerate_ai(model, question)
            return JsonResponse({'model': _result['model'], 'answer': _result['answer'], 'me':question, "time_elapsed": time_elapsed})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    else:
        form = QuestionForm()
        return render(request, 'ollama/home.html', {'form': form})
    


@csrf_exempt  # برای غیرفعال کردن CSRF protection برای این view (فقط برای نمونه کد)
def manage_models(request):
    if request.method == 'GET':
        models = get_models_from_json()
        return JsonResponse({'models': models})

    elif request.method == 'POST':
        data = json.loads(request.body)
        action = data.get('action')
        model_name = data.get('model_name')

        models = get_models_from_json()

        if action == 'add':
            if model_name and model_name not in models:
                models.append(model_name)
        elif action == 'delete':
            if model_name and model_name in models:
                models.remove(model_name)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid action'}, status=400)

        write_models_to_json(models)
        return JsonResponse({'status': 'success', 'models': models})
