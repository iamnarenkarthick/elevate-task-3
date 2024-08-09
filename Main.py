import re
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext

# Chatbot logic
def preprocess_input(user_input):
    """Preprocess the user input for better matching."""
    user_input = user_input.lower().strip()
    user_input = re.sub(r'[^a-zA-Z0-9\s]', '', user_input)  # Remove punctuation
    return user_input

def get_response(user_input):
    """Generate a response based on user input."""
    user_input = preprocess_input(user_input)
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm here to assist you!"
    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M")
        return f"The current time is {current_time}."
    elif "search" in user_input:
        search_query = user_input.replace("search", "").strip()
        return f"You asked to search for: {search_query}. Unfortunately, I can't search the web right now."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Tkinter UI
class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")

        self.chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', height=15)
        self.chat_log.pack(padx=10, pady=10)

        self.user_input = tk.Entry(root, width=50)
        self.user_input.pack(padx=10, pady=10)
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=10)

        self.add_message("Chatbot: Hello! I'm your friendly chatbot. How can I assist you today?")

    def add_message(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, message + '\n')
        self.chat_log.config(state='disabled')
        self.chat_log.yview(tk.END)

    def send_message(self, event=None):
        user_input = self.user_input.get()
        if user_input.strip():
            self.add_message(f"You: {user_input}")
            self.user_input.delete(0, tk.END)
            response = get_response(user_input)
            self.add_message(f"Chatbot: {response}")
            if "bye" in user_input.lower() or "exit" in user_input.lower():
                self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
