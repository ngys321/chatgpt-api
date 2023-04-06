import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)