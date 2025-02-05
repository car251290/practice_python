# chatbot 
def chat():
    print("Hello! My name is Chatbot. I am here to help you with any questions you may have. If you would like to exit, type 'bye'.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I do not understand. Please try again.")
chat()