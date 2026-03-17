import os
from groq import Groq

def run_ai_action(prompt: str, payload: dict) -> dict:
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return {"message": "IA simulada (sem chave configurada)", "prompt": prompt, "payload": payload}

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"{prompt}\n\nDados do evento: {payload}"
            }
        ]
    )

    return {"response": response.choices[0].message.content}