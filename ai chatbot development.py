import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

# Dummy function to simulate AI response
def get_bot_response(user_input):
    # Dummy responses
    responses = {
        "hi": "Hello!",
        "how are you?": "I'm just a bot, but thank you for asking!",
        "bye": "Goodbye! Have a great day!",
    }
    return responses.get(user_input.lower(), "I'm sorry, I don't understand that.")

# Function to handle user input
def send_message(event=None):
    user_input = user_entry.get()
    if user_input.strip() == "":
        return
    chat_area.configure(state="normal")
    chat_area.insert(tk.END, "You: " + user_input + "\n")
    chat_area.configure(state="disabled")

    bot_response = get_bot_response(user_input)
    chat_area.configure(state="normal")
    chat_area.insert(tk.END, "Bot: " + bot_response + "\n")
    chat_area.configure(state="disabled")

    user_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("AI Chatbot")

# Create chat area
chat_area = scrolledtext.ScrolledText(root, width=50, height=20, state="disabled")
chat_area.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Create user input entry
user_entry = tk.Entry(root, width=50)
user_entry.grid(row=1, column=0, padx=10, pady=10, sticky="w")
user_entry.bind("<Return>", send_message)

# Create send button
send_button = tk.Button(root, text="Send", width=10, command=send_message)
send_button.grid(row=1, column=0, padx=(0, 10), pady=10, sticky="e")

# Focus on the input entry when the application starts
user_entry.focus()

root.mainloop()
