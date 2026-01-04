def chatbot():
    print("Chatbot: Hello! I am a rule-based chatbot.")
    print("Chatbot: Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I help you?")

        elif "how are you" in user_input:
            print("Chatbot: I am fine, thank you! How about you?")

        elif "your name" in user_input:
            print("Chatbot: I am a simple rule-based chatbot.")

        elif "help" in user_input:
            print("Chatbot: I can answer basic questions like greetings and general queries.")

        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a nice day 😊")
            break

        else:
            print("Chatbot: Sorry, I didn't understand that.")

# Run the chatbot
chatbot()

