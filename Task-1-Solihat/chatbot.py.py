print("🤖 Welcome to DecodeBot!")
print("Type 'bye' to end the chat.")

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi there!")

    elif user == "hi":
        print("Bot: Hello!")

    elif user == "how are you":
        print("Bot: I am fine, thank you!")

    elif user == "what is your name":
        print("Bot: My name is DecodeBot.")

    elif user == "what is ai":
        print("Bot: AI means Artificial Intelligence.")

    elif user == "what is python":
        print("Bot: Python is a programming language.")

    elif user == "good morning":
        print("Bot: Good morning! Have a great day.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
