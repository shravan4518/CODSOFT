import random
import tkinter as tk
from tkinter import messagebox, ttk

current_list = []

def code_gen():
    while True:
        code = random.randint(1000, 9999)
        if code not in current_list:
            current_list.append(code)
            return code

def finish_entity(to_do, finish):
    for task in to_do:
        if task["code"] == finish:
            task["status"] = "(completed)"
            return True
    return False

def delete_entity(to_do, delete):
    for task in to_do:
        if task["code"] == delete:
            to_do.remove(task)
            return True
    return False

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.to_do = []

        self.root.title("To-Do List Application")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        self.title_label = tk.Label(self.root, text="Welcome to the To-Do List Application", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333333")
        self.title_label.pack(pady=10)

        self.add_task_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.add_task_frame.pack(pady=10)

        self.task_label = tk.Label(self.add_task_frame, text="Task:", font=("Helvetica", 12), bg="#f0f0f0")
        self.task_label.grid(row=0, column=0, padx=10)

        self.task_entry = tk.Entry(self.add_task_frame, font=("Helvetica", 12), width=30)
        self.task_entry.grid(row=0, column=1, padx=10)

        self.add_button = tk.Button(self.add_task_frame, text="Add Task", font=("Helvetica", 12), command=self.add_task, bg="#4caf50", fg="white")
        self.add_button.grid(row=0, column=2, padx=10)

        self.action_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.action_frame.pack(pady=10)

        self.finish_label = tk.Label(self.action_frame, text="Finish Task Code:", font=("Helvetica", 12), bg="#f0f0f0")
        self.finish_label.grid(row=0, column=0, padx=10)

        self.finish_entry = tk.Entry(self.action_frame, font=("Helvetica", 12), width=10)
        self.finish_entry.grid(row=0, column=1, padx=10)

        self.finish_button = tk.Button(self.action_frame, text="Finish Task", font=("Helvetica", 12), command=self.finish_task, bg="#2196f3", fg="white")
        self.finish_button.grid(row=0, column=2, padx=10)

        self.delete_label = tk.Label(self.action_frame, text="Delete Task Code:", font=("Helvetica", 12), bg="#f0f0f0")
        self.delete_label.grid(row=1, column=0, padx=10)

        self.delete_entry = tk.Entry(self.action_frame, font=("Helvetica", 12), width=10)
        self.delete_entry.grid(row=1, column=1, padx=10)

        self.delete_button = tk.Button(self.action_frame, text="Delete Task", font=("Helvetica", 12), command=self.delete_task, bg="#f44336", fg="white")
        self.delete_button.grid(row=1, column=2, padx=10)

        self.view_button = tk.Button(self.root, text="View Tasks", font=("Helvetica", 12), command=self.view_tasks, bg="#ff9800", fg="white")
        self.view_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", font=("Helvetica", 12), command=self.root.quit, bg="#9e9e9e", fg="white")
        self.stop_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            code = code_gen()
            self.to_do.append({"code": code, "task": task, "status": "pending"})
            messagebox.showinfo("Success", f"Task '{task}' added successfully with code {code}!")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Task cannot be empty!")

    def finish_task(self):
        if not self.to_do:
            messagebox.showwarning("Warning", "Your to-do list is empty.")
            return
        
        try:
            finish_code = int(self.finish_entry.get().strip())
            if finish_entity(self.to_do, finish_code):
                messagebox.showinfo("Success", f"Task with code {finish_code} marked as completed!")
            else:
                messagebox.showerror("Error", "The provided code does not exist in the list.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid code.")
        self.finish_entry.delete(0, tk.END)

    def delete_task(self):
        if not self.to_do:
            messagebox.showwarning("Warning", "Your to-do list is empty.")
            return
        
        try:
            delete_code = int(self.delete_entry.get().strip())
            if delete_entity(self.to_do, delete_code):
                messagebox.showinfo("Success", f"Task with code {delete_code} deleted successfully!")
            else:
                messagebox.showerror("Error", "The provided code does not exist in the list.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid code.")
        self.delete_entry.delete(0, tk.END)

    def view_tasks(self):
        if not self.to_do:
            messagebox.showinfo("Info", "Your to-do list is empty.")
            return
        
        view_window = tk.Toplevel(self.root)
        view_window.title("View Tasks")
        view_window.geometry("400x300")
        view_window.configure(bg="#f0f0f0")

        view_text = tk.Text(view_window, font=("Helvetica", 12), bg="#ffffff", fg="#000000", wrap="word")
        view_text.pack(expand=True, fill="both", padx=10, pady=10)
        
        for task in self.to_do:
            view_text.insert(tk.END, f"Code: {task['code']}, Task: {task['task']}, Status: {task['status']}\n")
        view_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()