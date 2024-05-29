import requests

def query_llm(prompt):
    url = "https://api.together.xyz/v1/completions"

    payload = {
        "model": "meta-llama/Llama-3-8b-chat-hf",
        "prompt": prompt,
        "max_tokens": 200,
        "stop": ["</s>"]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer 551774149a5aa92cf7b8cee1a296851f6b04cf2a3b4f212317083155ceef6f72"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)

    return response.json()["choices"][0]["text"].strip()
