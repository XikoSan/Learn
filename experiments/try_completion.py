import openai

openai.api_key = "..."

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "Ты помогаешь думать логически."},
    {"role": "user", "content": "Как определить, что решение задачи корректно?"}
  ]
)

print(response['choices'][0]['message']['content'])
