import tkinter as tk
from tkinter import messagebox
import time
import random

# Sample texts for typing
sample_texts = [
    "the quick brown fox jumps over the lazy dog",
    "python is a versatile programming language for beginners and experts",
    "practice makes perfect, so keep typing to improve your speed",
    "tkinter is a built-in Python module for creating GUI applications",
    "consistency and dedication are key to mastering any skill"

]

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x400")
        self.root.config(bg="#b8b8b8")

        self.start_time = 0

        self.text_to_type = tk.StringVar()
        self.text_to_type.set(random.choice(sample_texts))

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Typing Speed Test", font=("Helvetica", 24), bg="#f0f0f0").pack(pady=20)

        self.sample_label = tk.Label(self.root, text=self.text_to_type.get(), font=("Helvetica", 16), wraplength=650, bg="#f0f0f0")
        self.sample_label.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Helvetica", 16), width=70)
        self.entry.pack(pady=20)
        self.entry.bind("<KeyPress>", self.start_timer)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        tk.Button(self.root, text="Check Speed", font=("Helvetica", 14), command=self.calculate_speed).pack(pady=10)
        tk.Button(self.root, text="New Text", font=("Helvetica", 14), command=self.new_text).pack(pady=5)

    def start_timer(self, event):
        if self.start_time == 0:
            self.start_time = time.time()

    def calculate_speed(self):
        end_time = time.time()
        typed_text = self.entry.get()
        total_words = len(typed_text.split())
        elapsed_minutes = (end_time - self.start_time) / 60

        if elapsed_minutes > 0:
            wpm = total_words / elapsed_minutes
            self.result_label.config(text=f"Your typing speed: {wpm:.2f} WPM")
        else:
            self.result_label.config(text="Please type some words first!")

    def new_text(self):
        self.text_to_type.set(random.choice(sample_texts))
        self.sample_label.config(text=self.text_to_type.get())
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
