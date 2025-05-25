import openai

# Paste your OpenAI API key here
openai.api_key = "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"

# Read your reference file
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

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You answer as a marina expert using the provided reference guide."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=250,
        temperature=0.2,
    )

    print(response['choices'][0]['message']['content'].strip())
