from django.shortcuts import render
from django.http import JsonResponse
from .forms import QuestionForm
from .MyAI import gernerate_ai


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