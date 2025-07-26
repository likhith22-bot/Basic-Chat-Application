def chatbot():
    print("Hello! I'm ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("ChatBot: Hello there! How can I help you today?")
        elif user_input in ["how are you", "how are you doing"]:
            print("ChatBot: I'm just a bunch of code, but I'm functioning as expected!")
        elif user_input in ["what is your name", "who are you"]:
            print("ChatBot: I'm a simple chatbot,I am here to help you.")
        elif user_input in ["tell me a joke", "make me laugh"]:
            print("ChatBot: Why did the scarecrow win an award? Because he was outstanding in his field!")
        elif user_input in ["what can you do", "help me"]:
            print("ChatBot: I can chat with you, tell jokes, and answer simple questions.")
        elif user_input in["why you here", "what's your purpose"]:
            print("ChatBot: I'm here to assist you and make your day a little brighter!")
        elif user_input in ["bye", "exit", "quit"]:
            print("ChatBot: Goodbye! Have a great day!")
            break
        else:
            print("ChatBot: Sorry, I didn't understand that.")

chatbot()
