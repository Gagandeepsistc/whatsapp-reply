from openai import OpenAI

# client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="put your API of chat gpt",
 )
chat_history = """

"""

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "system",
       "content": "Output should be response according to the last chat (text message only). You are a person named Gagan who speaks hindi and hindi. You are from India and you are a coder. You analyze chat history and roast in a funny way. Output should be the next chat response (text message only)"},
      {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Rohan Das: "},
      {"role": "user", "content": chat_history}
  ]
)

print(completion.choices[0].message.content)