import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, size):
        self.size = size    
    def easy(self):
        chars = string.ascii_uppercase + string.ascii_lowercase
        return ''.join(random.choice(chars) for _ in range(self.size))  
    def inter(self):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for _ in range(self.size)) 
    def hard(self):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "@!#_*&^$%"
        return ''.join(random.choice(chars) for _ in range(self.size))

def generate_password():
    try:
        size = int(size_entry.get())
        complexity = complexity_var.get()
        generator = PasswordGenerator(size)
        
        if complexity == "easy":
            password = generator.easy()
        elif complexity == "inter":
            password = generator.inter()
        elif complexity == "hard":
            password = generator.hard()
        else:
            raise ValueError("Invalid complexity level")
        
        password_text.config(state=tk.NORMAL)
        password_text.delete(1.0, tk.END)
        password_text.insert(tk.END, password)
        password_text.config(state=tk.DISABLED)
    except ValueError:
        password_text.config(state=tk.NORMAL)
        password_text.delete(1.0, tk.END)
        password_text.insert(tk.END, "Please enter a valid size and complexity")
        password_text.config(state=tk.DISABLED)

def copy_to_clipboard():
    password = password_text.get(1.0, tk.END).strip()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.resizable(False, False)
root.config(bg="#282c34")

title_label = ttk.Label(root, text="Password Generator", font=("Helvetica", 18, "bold"), background="#61afef", foreground="white")
title_label.pack(pady=20, fill=tk.X)

size_frame = ttk.Frame(root, padding="10")
size_frame.pack(pady=10, fill=tk.X, padx=20)
size_label = ttk.Label(size_frame, text="Enter Password Size:", font=("Helvetica", 12, "bold"))
size_label.pack(side=tk.LEFT, padx=5)
size_entry = ttk.Entry(size_frame, width=10, font=("Helvetica", 12))
size_entry.pack(side=tk.LEFT, padx=5)

complexity_frame = ttk.LabelFrame(root, text="Select Complexity", padding="10", labelanchor='n')
complexity_frame.pack(pady=10, fill=tk.X, padx=20)
complexity_var = tk.StringVar(value="easy")
complexity_easy = ttk.Radiobutton(complexity_frame, text="Easy", variable=complexity_var, value="easy")
complexity_easy.pack(side=tk.LEFT, padx=5)
complexity_inter = ttk.Radiobutton(complexity_frame, text="Intermediate", variable=complexity_var, value="inter")
complexity_inter.pack(side=tk.LEFT, padx=5)
complexity_hard = ttk.Radiobutton(complexity_frame, text="Hard", variable=complexity_var, value="hard")
complexity_hard.pack(side=tk.LEFT, padx=5)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)


password_text = tk.Text(root, height=3, wrap=tk.WORD, font=("Helvetica", 12, "bold"), background="#282c34", foreground="white", state=tk.DISABLED)
password_text.pack(pady=10, fill=tk.X, padx=20)

root.mainloop()
