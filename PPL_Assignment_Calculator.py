import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("360x550")
        self.root.config(bg="#000000")
        self.root.resizable(False, False)

        self.expression = ""

        # Create display
        self.display = tk.Entry(
            root, font=("Helvetica", 32, "bold"), bd=0, relief="flat",
            bg="#000000", fg="white", justify="right"
        )
        self.display.pack(padx=15, pady=30, fill="x")
        self.display.insert(0, "0")

        # Key bindings for event handling
        root.bind("<Return>", self.evaluate_expression)
        root.bind("<BackSpace>", self.delete_last)

        # Button layout like iPhone calculator
        buttons = [
            ["C", "±", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        # Create button frames
        frame = tk.Frame(root, bg="#000000")
        frame.pack(expand=True, fill="both")

        for r, row in enumerate(buttons):
            frame_row = tk.Frame(frame, bg="#000000")
            frame_row.pack(expand=True, fill="both")
            for c, char in enumerate(row):
                # Decide button color
                if char in {"÷", "×", "-", "+", "="}:
                    bg_color = "#FF9500"
                    fg_color = "white"
                elif char in {"C", "±", "%"}:
                    bg_color = "#A5A5A5"
                    fg_color = "black"
                else:
                    bg_color = "#333333"
                    fg_color = "white"

                # Create buttons
                btn = tk.Button(
                    frame_row, text=char, font=("Helvetica", 22, "bold"),
                    bg=bg_color, fg=fg_color, bd=0, relief="flat",
                    activebackground=bg_color, activeforeground="white",
                    command=lambda ch=char: self.on_button_click(ch)
                )
                # Adjust width for "0" button (double width)
                if char == "0":
                    btn.pack(side="left", expand=True, fill="both", padx=2, pady=2, ipadx=30)
                else:
                    btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)


    # Event Handlers

    def on_button_click(self, char):
        """Handles button click events"""
        try:
            if char == "C":
                self.expression = ""
                self.display.delete(0, tk.END)
                self.display.insert(0, "0")
            elif char == "±":
                # Toggle sign
                value = self.display.get()
                if value.startswith("-"):
                    self.display.delete(0)
                    self.display.insert(0, value[1:])
                else:
                    if value != "0":
                        self.display.delete(0)
                        self.display.insert(0, "-" + value)
            elif char == "=":
                self.evaluate_expression()
            else:
                if self.display.get() == "0" and char not in {".", "÷", "×", "+", "-", "%"}:
                    self.display.delete(0)
                self.expression += char
                self.display.insert(tk.END, char)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")

    def evaluate_expression(self, event=None):
        """Safely evaluate the expression with exception handling"""
        try:
            expression = self.display.get().replace("÷", "/").replace("×", "*")
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.expression = str(result)
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Cannot divide by zero!")
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")
            self.expression = ""
        except Exception:
            messagebox.showerror("Input Error", "Invalid Expression!")
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")
            self.expression = ""

    def delete_last(self, event=None):
        """Handles backspace key event"""
        value = self.display.get()
        if len(value) > 1:
            self.display.delete(len(value) - 1)
        else:
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")



# Run the Application

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
