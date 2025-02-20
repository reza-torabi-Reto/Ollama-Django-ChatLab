import requests
import json
from time import time
import functools

def time_gernerate_ai(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        time_elapsed = round(end_time - start_time, 2)
        return result, time_elapsed  # برگرداندن result و time_elapsed
    return wrapper

@time_gernerate_ai
def gernerate_ai(model, qust):
    # model = ('llama3.2:1b', 'deepseek-r1:1.5b', 'gemma:2b')
    url = "http://localhost:11434/api/chat"
    paylooad = {
        "model" : model,
        "messages" : [{ "role": "user", "content": qust }]
    }
    response = requests.post(url, json=paylooad, stream=True)
    if response.status_code == 200:
        print("Streaming ...")
        texts = ""
        for line in response.iter_lines(decode_unicode=True):
            try:
                json_data = json.loads(line)
                if "message" in json_data and "content" in json_data["message"]:
                    texts += json_data["message"]["content"]
            except json.JSONDecodeError:
                print(f"\nFailed to parse line {line}") 
    result = {
        "answer": texts,
        "model": paylooad['model'],
    }
    return result

















# import ollama
# response = ollama.chat(model='llama2', messages=[
#   {
#     'role': 'user',
#     'content': 'Why is the sky blue?',
#   },
# ])
# print(response['message']['content'])


# import requests
# import json

# url = "http://localhost:11434/api/chat"

# paylooad = {
#     "model" : "deepseek-r1:1.5b",
#     "messages" : [{ "role": "user", "content": "what is python?" }]
# }

# response = requests.post(url, json=paylooad, stream=True)

# if response.status_code == 200:
#     print("Streaming ...")
#     texts = ""
#     for line in response.iter_lines(decode_unicode=True):
#         try:
#             json_data = json.loads(line)
#             texts += json_data["message"]["content"]

#         except json.JSONDecodeError:
#             print(f"\nFailed to parse line {line}")
#     print("=========================")
#     print(texts)

# import requests
# import json
# url = "http://localhost:11434/api/chat"

# paylooad = {
#     "model" : "deepseek-r1:1.5b",
#     "messages" : [{ "role": "user", "content": "what is python?" }]
# }

# response = requests.post(url, json=paylooad, stream=True)

# if response.status_code == 200:
#     print("Streaming ...")
#     for line in response.iter_lines(decode_unicode=True):
#         if line:
#             try:
#                 json_data = json.loads(line)
#                 if "message" in json_data and "content" in json_data["message"]:
#                     print(json_data["message"]["content"], end="")
#             except json.JSONDecodeError:
#                 print(f"\nFailed to parse line {line}")
#     print()
# else:
#     print(f"Error: {response.status_code}")
#     print(response.text)
# ----------------------------------------
# import ollama

# client = ollama.Client()

# _model = "deepseek-r1:1.5b"
# _prompt = "what is python?"
# response = client.generate(model = _model, prompt = _prompt)
# print(response.response)
