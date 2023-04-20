import openai
import os

openai.api_key = "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"

prompt = "jelaskan dalam 50 kata apa itu nasi goreng"

model_engine = "davinci"

response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=100,
    temperature=0.9,
)

print(response.choices[0].text.strip())
