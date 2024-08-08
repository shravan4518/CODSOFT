import tkinter as tk
from tkinter import ttk, messagebox
import random

user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    
    if (user_choice == 'Rock' and computer_choice == 'Scissors') or (user_choice == 'Paper' and computer_choice == 'Rock') or (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result_text.set(f'You chose {user_choice}, computer chose {computer_choice}. You win!')
        user_score += 1
    elif user_choice == computer_choice:
        result_text.set(f'You chose {user_choice}, computer chose {computer_choice}. It\'s a draw!')
    else:
        result_text.set(f'You chose {user_choice}, computer chose {computer_choice}. You lose!')
        computer_score += 1
    
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    
    if not messagebox.askyesno("Play Again", "Do you want to play another round?"):
        root.quit()

def show_instructions():
    instructions = (
        "Instructions:\n\n"
        "1. Choose Rock, Paper, or Scissors by clicking the corresponding button.\n"
        "2. The computer will also make a choice.\n"
        "3. The winner is decided by the following rules:\n"
        "   - Rock beats Scissors\n"
        "   - Scissors beat Paper\n"
        "   - Paper beats Rock\n"
        "4. Your score and the computer's score will be displayed.\n"
        "5. After each round, you will be asked if you want to play again."
    )
    messagebox.showinfo("How to Play", instructions)

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("500x450")
root.configure(bg="#2c3e50")

style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", font=("Helvetica", 14), padding=10, background="#34495e", foreground="white")
style.map("TButton", background=[('active', '#1abc9c')])
style.configure("TLabel", background="#2c3e50", foreground="white", font=("Helvetica", 12))

title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 24, "bold"), bg="#2c3e50", fg="#ecf0f1")
title_label.pack(pady=20)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="#ecf0f1")
result_label.pack(pady=20)

user_score_label = tk.Label(root, text=f"Your Score: {user_score}", font=("Helvetica", 14), bg="#2c3e50", fg="#ecf0f1")
user_score_label.pack(side=tk.LEFT, padx=20)

computer_score_label = tk.Label(root, text=f"Computer Score: {computer_score}", font=("Helvetica", 14), bg="#2c3e50", fg="#ecf0f1")
computer_score_label.pack(side=tk.RIGHT, padx=20)

button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=40)

rock_button = ttk.Button(button_frame, text="Rock", command=lambda: play_game('Rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = ttk.Button(button_frame, text="Paper", command=lambda: play_game('Paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = ttk.Button(button_frame, text="Scissors", command=lambda: play_game('Scissors'))
scissors_button.grid(row=0, column=2, padx=10)

instructions_button = ttk.Button(root, text="Instructions", command=show_instructions)
instructions_button.pack(pady=10)

exit_button = ttk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
