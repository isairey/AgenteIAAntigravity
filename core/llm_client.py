import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt: str, model="gpt-4o-mini"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Eres un asistente experto en programación."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content