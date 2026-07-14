from groq import Groq

AI = open("API.txt").read().strip()

api = Groq(api_key = AI)

print("working")

try:
    response = api.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = [
            {
                "role": "user",
                "content": "tell me a joke"
            }
        ]
    )
    print("\n response:" + response.choices[0].message.content)

except Exception as e:
    print(f"connection fail. details: \n {e}")