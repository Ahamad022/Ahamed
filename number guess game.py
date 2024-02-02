import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("300x150")

        self.secret_number = random.randint(1, 100)
        self.guess_label = tk.Label(self.master, text="Enter your guess:")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self.master)
        self.guess_entry.pack()

        self.guess_button = tk.Button(self.master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

    def check_guess(self):
        try:
            user_guess = int(self.guess_entry.get())
            if user_guess == self.secret_number:
                messagebox.showinfo("Congratulations!", "You guessed the correct number!")
                self.master.destroy()
            elif user_guess < self.secret_number:
                messagebox.showinfo("Incorrect", "Try a higher number.")
            else:
                messagebox.showinfo("Incorrect", "Try a lower number.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessGame(root)
    root.mainloop()
