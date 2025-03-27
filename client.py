from openai import OpenAI

Openapi_key = "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"
client = OpenAI(api_key=Openapi_key)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assisstant named Jarvis. You are a creation of Developer Armaan. You give short answers in English and Hindi"},
        {
            "role": "system",
            "content": "What is coding"
        }
    ]
)

print(completion.choices[0].message)