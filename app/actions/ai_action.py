import os
import anthropic

def run_ai_action(prompt: str, payload: dict) -> dict:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key:
        return {"message": "IA simulada (sem chave configurada)", "prompt": prompt, "payload": payload}

    client = anthropic.Anthropic(api_key=api_key)

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"{prompt}\n\nDados do evento: {payload}"
            }
        ]
    )

    return {"response": message.content[0].text}