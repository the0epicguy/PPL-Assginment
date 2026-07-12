import tkinter as tk
from tkinter import messagebox
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple To-Do List")
        self.root.geometry("400x500")
        self.root.config(bg="#f7f7f7")

        # Title
        title = tk.Label(root, text="My To-Do List", font=("Arial", 20, "bold"), bg="#f7f7f7", fg="#333")
        title.pack(pady=10)

        # Input field
        self.task_entry = tk.Entry(root, font=("Arial", 14), width=26, bd=2, relief="groove")
        self.task_entry.pack(pady=10)

        # Button frame
        button_frame = tk.Frame(root, bg="#f7f7f7")
        button_frame.pack(pady=10)

        # Load button images
        self.add_icon = tk.PhotoImage(file="add-button_592324-22497.png")
        self.delete_icon = tk.PhotoImage(file="delete-button_592324-8378.png")
        self.clear_icon = tk.PhotoImage(file="reset-button_592324-8776.png")

        # Add button (image + optional text)
        add_btn = tk.Button(button_frame, text="Add", image=self.add_icon, compound="left",
                            command=self.add_task, bd=0, bg="#f7f7f7", cursor="hand2")
        add_btn.grid(row=0, column=0, padx=5)

        # Delete button (image + optional text)
        del_btn = tk.Button(button_frame, text="Delete", image=self.delete_icon, compound="left",
                            command=self.delete_task, bd=0, bg="#f7f7f7", cursor="hand2")
        del_btn.grid(row=0, column=1, padx=5)

        # Clear all button (image + optional text)
        clear_btn = tk.Button(button_frame, text="Clear", image=self.clear_icon, compound="left",
                              command=self.clear_tasks, bd=0, bg="#f7f7f7", cursor="hand2")
        clear_btn.grid(row=0, column=2, padx=5)

        # Task list
        self.listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12),
                                  bd=2, relief="groove", selectbackground="#a0d8ef")
        self.listbox.pack(pady=10)

        # File buttons
        file_frame = tk.Frame(root, bg="#f7f7f7")
        file_frame.pack(pady=5)

        save_btn = tk.Button(file_frame, text="Save", font=("Arial", 11),
                             bg="#2196F3", fg="white", width=10, relief="flat",
                             cursor="hand2", command=self.save_tasks)
        save_btn.grid(row=0, column=0, padx=5)

        load_btn = tk.Button(file_frame, text="Load", font=("Arial", 11),
                             bg="#FF9800", fg="white", width=10, relief="flat",
                             cursor="hand2", command=self.load_tasks)
        load_btn.grid(row=0, column=1, padx=5)

    # Add a new task
    def add_task(self):
        task = self.task_entry.get().strip()
        try:
            if not task:
                raise ValueError("Task cannot be empty.")
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))

    # Delete selected task
    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()
            if not selected_index:
                raise IndexError("No task selected.")
            self.listbox.delete(selected_index)
        except IndexError as e:
            messagebox.showwarning("Selection Error", str(e))

    # Clear all tasks
    def clear_tasks(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
            self.listbox.delete(0, tk.END)

    # Save tasks to file
    def save_tasks(self):
        try:
            tasks = self.listbox.get(0, tk.END)
            with open("tasks.txt", "w") as f:
                for task in tasks:
                    f.write(task + "\n")
            messagebox.showinfo("Success", "Tasks saved successfully.")
        except Exception as e:
            messagebox.showerror("File Error", f"Could not save tasks:\n{e}")

    # Load tasks from file
    def load_tasks(self):
        try:
            if not os.path.exists("tasks.txt"):
                raise FileNotFoundError("No saved tasks found.")
            self.listbox.delete(0, tk.END)
            with open("tasks.txt", "r") as f:
                for line in f:
                    self.listbox.insert(tk.END, line.strip())
            messagebox.showinfo("Loaded", "Tasks loaded successfully.")
        except FileNotFoundError as e:
            messagebox.showwarning("Load Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
