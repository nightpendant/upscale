from groq import Groq

# paste the API key here because git doesnt let me push it lol
client = Groq(api_key="")

async def query_llm(prompt: str):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )

    return response.choices[0].message.content
