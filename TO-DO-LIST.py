import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Main GUI
app = tk.Tk()
app.title("To-Do List")

# Entry and Buttons
entry = tk.Entry(app, width=30)
entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(app, text="Add", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=10)

remove_button = tk.Button(app, text="Remove", command=remove_task)
remove_button.grid(row=1, column=0, columnspan=2, pady=5)

# Task Listbox
listbox = tk.Listbox(app, selectmode=tk.SINGLE, width=40)
listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()