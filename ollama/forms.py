from django import forms
import os
import json
from django.conf import settings


def get_models_from_json():
    json_file_path = os.path.join(settings.BASE_DIR, 'static', 'data', 'models_ai.json')
    try:
        with open(json_file_path, 'r') as f:
            models = json.load(f)
            return [(model, model) for model in models]
    except FileNotFoundError:
        return [('', 'No models found')]


# def get_models_from_json():
#     json_file_path = os.path.join(settings.BASE_DIR, 'static', 'data', 'models_ai.json')
#     try:
#         # باز کردن و خواندن فایل JSON
#         with open(json_file_path, 'r') as f:
#             models = json.load(f)
#             return [(model, model) for model in models]
#     except FileNotFoundError:
#         # مدیریت خطای پیدا نشدن فایل
#         print("File not found.")
        

class QuestionForm(forms.Form):
    model_choices = get_models_from_json()
    
    model = forms.ChoiceField(choices=model_choices, label="Select AI Model")
    question = forms.CharField(label='Your Question', max_length=1000, widget=forms.Textarea)
    