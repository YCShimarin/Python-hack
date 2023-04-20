import openai

# Set your API key
openai.api_key = "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"

# Set the prompt text
prompt = "jelaskan apa itu nasi goreng"

# Set the parameters for the API request
model = "text-davinci-002"  # versi model
temperature = 0.8  # kontrol kreativitas AI
max_tokens = 250    # proses text dengan pustaka

# Send the request to the API and get the response
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens
)

# Print the generated text
print("Pertanyaan : " + prompt)
print(response.choices[0].text.strip())
