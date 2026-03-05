from groq import Groq

groq_key = ""
# paste the API key as a text file here because git doesnt let me push it lol
with open("groq_key.txt") as file:
    groq_key = file.read()

client = Groq(api_key=groq_key)

async def query_llm(prompt: str):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )

    return response.choices[0].message.content
