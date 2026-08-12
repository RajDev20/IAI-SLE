# Create a complete Python project structure for a simple AI Agent using the GitHub Copilot SDK. 

def chatbot():
    print("Simple AI Agent")
    while True:
        user = input("You: ")

        if user.lower() == "bye":
            print("Agent: Goodbye!")
            break

        elif "hello" in user.lower():
            print("Agent: Hello! Nice to meet you.")

        elif "name" in user.lower():
            print("Agent: I am a simple AI agent.")

        else:
            print("Agent: Sorry, I don't understand.")

chatbot()
