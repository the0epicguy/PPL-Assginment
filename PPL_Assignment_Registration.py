import tkinter as tk
from tkinter import messagebox
import re
from datetime import datetime


class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("User Registration System")
        self.root.geometry("700x800+200+50")
        self.root.resizable(False, False)

        # Configure colors
        self.bg_color = "#f0f4f8"
        self.primary_color = "#4a90e2"
        self.secondary_color = "#2c5aa0"
        self.success_color = "#27ae60"
        self.error_color = "#e74c3c"

        self.root.configure(bg=self.bg_color)
        self.create_widgets()

    def create_widgets(self):
        # Main container
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(expand=True, fill='both', padx=30, pady=20)

        # Title
        title_label = tk.Label(
            main_frame,
            text="Create Account",
            font=("Helvetica", 28, "bold"),
            bg=self.bg_color,
            fg=self.secondary_color
        )
        title_label.pack(pady=(0, 10))

        subtitle_label = tk.Label(
            main_frame,
            text="Fill in the details to register",
            font=("Helvetica", 11),
            bg=self.bg_color,
            fg="#7f8c8d"
        )
        subtitle_label.pack(pady=(0, 30))

        # Form fields
        self.create_input_field(main_frame, "Full Name", "name_entry")
        self.create_input_field(main_frame, "Email Address", "email_entry")
        self.create_input_field(main_frame, "Phone Number", "phone_entry")
        self.create_input_field(main_frame, "Age", "age_entry")
        self.create_input_field(main_frame, "Password", "password_entry", show="*")

        # Register Button
        self.register_btn = tk.Button(
            main_frame,
            text="REGISTER",
            font=("Helvetica", 12, "bold"),
            bg=self.primary_color,
            fg="white",
            relief="flat",
            borderwidth=0,
            padx=40,
            pady=12,
            cursor="hand2",
            command=self.handle_registration
        )
        self.register_btn.pack(pady=(30, 10))

        # Hover effects
        self.register_btn.bind("<Enter>", self.on_button_hover)
        self.register_btn.bind("<Leave>", self.on_button_leave)

        # Clear Button
        self.clear_btn = tk.Button(
            main_frame,
            text=" CLEAR FORM",
            font=("Helvetica", 11, "bold"),
            bg=self.error_color,
            fg="white",
            relief="flat",
            borderwidth=0,
            padx=50,
            pady=20,
            cursor="hand2",
            command=self.clear_form
        )
        self.clear_btn.pack(pady=(10, 10))

        # Hover effects for clear button
        self.clear_btn.bind("<Enter>", self.on_clear_hover)
        self.clear_btn.bind("<Leave>", self.on_clear_leave)

        # Status Label
        self.status_label = tk.Label(
            main_frame,
            text="",
            font=("Helvetica", 10),
            bg=self.bg_color,
            wraplength=400
        )
        self.status_label.pack(pady=10)

    def create_input_field(self, parent, label_text, entry_name, show=None):
        field_frame = tk.Frame(parent, bg=self.bg_color)
        field_frame.pack(fill='x', pady=8)

        label = tk.Label(
            field_frame,
            text=label_text,
            font=("Helvetica", 10, "bold"),
            bg=self.bg_color,
            fg=self.secondary_color,
            anchor='w'
        )
        label.pack(fill='x', pady=(0, 5))

        entry = tk.Entry(
            field_frame,
            font=("Helvetica", 11),
            bg="white",
            relief=tk.FLAT,
            bd=2,
            highlightthickness=2,
            highlightbackground="#dfe6e9",
            highlightcolor="#dfe6e9",
            show=show
        )
        entry.pack(fill='x', ipady=8)

        setattr(self, entry_name, entry)

        # Focus events
        entry.bind("<FocusIn>", lambda e: self.on_entry_focus(e))
        entry.bind("<FocusOut>", lambda e: self.on_entry_unfocus(e))

    # --- Event Handlers ---

    def on_button_hover(self, event):
        self.register_btn.config(bg=self.secondary_color)

    def on_button_leave(self, event):
        self.register_btn.config(bg=self.primary_color)

    def on_clear_hover(self, event):
        self.clear_btn.config(bg="#c0392b")

    def on_clear_leave(self, event):
        self.clear_btn.config(bg=self.error_color)

    def on_entry_focus(self, event):
        event.widget.config(highlightbackground=self.primary_color, highlightcolor=self.primary_color)

    def on_entry_unfocus(self, event):
        event.widget.config(highlightbackground="#dfe6e9", highlightcolor="#dfe6e9")

    # --- Validation and Exception Handling ---

    def handle_registration(self):
        try:
            name = self.name_entry.get().strip()
            email = self.email_entry.get().strip()
            phone = self.phone_entry.get().strip()
            age = self.age_entry.get().strip()
            password = self.password_entry.get()

            # Validate Name
            if not name:
                raise ValueError("Name cannot be empty!")
            if len(name) < 3:
                raise ValueError("Name must be at least 3 characters long!")

            # Validate Email
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, email):
                raise ValueError("Invalid email format! Example: user@example.com")

            # Validate Phone
            phone_pattern = r'^\d{10}$'
            if not re.match(phone_pattern, phone):
                raise ValueError("Phone number must be exactly 10 digits!")

            # Validate Age
            try:
                age_int = int(age)
            except ValueError:
                raise ValueError("Age must be a valid number!")
            if age_int < 18 or age_int > 100:
                raise ValueError("Age must be between 18 and 100!")

            # Validate Password
            if len(password) < 6:
                raise ValueError("Password must be at least 6 characters long!")
            if not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password):
                raise ValueError("Password must include both letters and numbers!")

            # If all validations pass
            self.show_success_message(name, email)

        except ValueError as ve:
            self.show_error_message(str(ve))
        except Exception as e:
            self.show_error_message(f"Unexpected error: {str(e)}")

    def show_success_message(self, name, email):
        self.status_label.config(
            text=f"✓ Registration Successful!\nWelcome, {name}!",
            fg=self.success_color,
            font=("Helvetica", 11, "bold")
        )

        messagebox.showinfo(
            "Success",
            f"Account created successfully!\n\nName: {name}\nEmail: {email}\n\nYou can now log in."
        )

        # Save to local file (optional)
        with open("registrations.txt", "a") as f:
            f.write(f"{datetime.now()} | {name}, {email}\n")

        self.clear_form()

    def show_error_message(self, message):
        self.status_label.config(
            text=f"✗ {message}",
            fg=self.error_color,
            font=("Helvetica", 10, "bold")
        )
        messagebox.showerror("Validation Error", message)

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.status_label.config(text="")
        self.name_entry.focus()


# --- Main Application ---
if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()
