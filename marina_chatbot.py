import openai

client = openai.OpenAI(api_key="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")  # Replace with your new key or use environment variable

with open("marina_reference.md", "r", encoding="utf-8") as f:
    reference = f.read()

print("Marina Quick Reference Chatbot (type 'exit' to quit)")

while True:
    user_question = input("\nAsk a question: ")
    if user_question.strip().lower() == "exit":
        break

    prompt = f"""You are a helpful assistant at a marina that specializes in Suzuki and Yamaha outboard motors, boat repair, and marine fuel. Use the following reference information to answer questions concisely and accurately. If the answer isn’t in the reference, say you don’t know.

Reference:
{reference}

Question: {user_question}
Answer:"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You answer as a marina expert using the provided reference guide."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=250,
        temperature=0.2,
    )

    print(response.choices[0].message.content.strip())
