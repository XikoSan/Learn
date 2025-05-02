import requests

api_key = "26a1324b22453df1920a640df36c73517919d07677a92d2a2dec9daf22d5736c"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
    "messages": [
        {"role": "user", "content": "Explain how transformers work in simple terms."}
    ],
    "temperature": 0.7,
    "max_tokens": 256,
    "top_p": 0.9,
}

response = requests.post("https://api.together.xyz/v1/chat/completions", headers=headers, json=data)

print(response.json()["choices"][0]["message"]["content"])
