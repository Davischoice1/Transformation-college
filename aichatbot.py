def chatbot():
    print("AI: Hello! I am your AI assistant. Type 'exit' to stop.")

    # Get the user's name
    name = input("AI: Welcome! What's your name? ").strip()
    print(f"AI: Nice to meet you, {name}! You can ask me any question or type 'exit' to stop.")

    while True:
        user_input = input(f"{name}: ").lower().strip()

        if "hello" in user_input:
            print("AI: Hi there! How can I help you?")
        elif "how are you" in user_input:
            print("AI: I'm just a program, but I'm doing fine! Thanks for asking.")
        elif "hungry" in user_input and "food" in user_input:
            print("AI: I can't give you food but I can suggest what to eat.")
        elif "bye" in user_input:
            print(f"AI: Goodbye, {name}! Have a great day.")
            break
        elif "exit" in user_input:
            print(f"AI: Exiting... Have a nice day, {name}!")
            break
        else:
            print("AI: I'm not sure how to respond to that. Feel free to ask me anything!")

# Run the chatbot
chatbot()


