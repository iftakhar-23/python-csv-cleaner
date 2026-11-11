
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import csv

from main import clean_csv


def choose_file():
    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[
            ("CSV files", "*.csv"),
            ("All files", "*.*")
        ]
    )

    if file_path:
        selected_file.set(file_path)
        status_text.set("File selected. Ready to clean.")


def run_cleaner():
    file_path = selected_file.get().strip()

    if not file_path:
        messagebox.showwarning(
            "No file selected",
            "Please select a CSV file first."
        )
        return

    try:
        output_file = clean_csv(file_path)

        status_text.set("Cleaning completed successfully!")

        messagebox.showinfo(
            "Cleaning Complete",
            f"Your CSV file has been cleaned!\n\n"
            f"Output file:\n{output_file}"
        )

    except (FileNotFoundError, ValueError, PermissionError,
            OSError, csv.Error) as error:

        status_text.set("Cleaning failed.")

        messagebox.showerror(
            "Cleaning Error",
            str(error)
        )


# Create the main window
root = tk.Tk()

root.title("Python CSV Cleaner")
root.geometry("650x390")
root.minsize(550, 350)
root.configure(bg="#F4F6FA")

# Configure application styling
style = ttk.Style(root)
style.theme_use("clam")

style.configure(
    "TFrame",
    background="#F4F6FA"
)

style.configure(
    "TLabel",
    background="#F4F6FA",
    foreground="#1F2937",
    font=("Segoe UI", 10)
)

style.configure(
    "Title.TLabel",
    font=("Segoe UI", 23, "bold"),
    foreground="#172554"
)

style.configure(
    "Subtitle.TLabel",
    font=("Segoe UI", 10),
    foreground="#64748B"
)

style.configure(
    "TEntry",
    padding=10,
    font=("Segoe UI", 10)
)

style.configure(
    "Primary.TButton",
    font=("Segoe UI", 10, "bold"),
    padding=11,
    background="#2563EB",
    foreground="white"
)

style.map(
    "Primary.TButton",
    background=[("active", "#1D4ED8")]
)

style.configure(
    "Secondary.TButton",
    font=("Segoe UI", 10),
    padding=9
)

# Main layout
main_frame = ttk.Frame(root, padding=35)
main_frame.pack(fill="both", expand=True)

# Application heading
ttk.Label(
    main_frame,
    text="CSV Cleaner",
    style="Title.TLabel"
).pack(anchor="center", pady=(15, 5))

ttk.Label(
    main_frame,
    text="Clean and organize your CSV files easily.",
    style="Subtitle.TLabel"
).pack(anchor="center", pady=(0, 30))

# File selection
ttk.Label(
    main_frame,
    text="Select your CSV file"
).pack(anchor="w", pady=(0, 8))

selected_file = tk.StringVar()

file_frame = ttk.Frame(main_frame)
file_frame.pack(fill="x", pady=(0, 22))

file_entry = ttk.Entry(
    file_frame,
    textvariable=selected_file
)
file_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

ttk.Button(
    file_frame,
    text="Browse Files",
    command=choose_file,
    style="Secondary.TButton"
).pack(side="right")

# Clean button
ttk.Button(
    main_frame,
    text="Clean CSV File",
    command=run_cleaner,
    style="Primary.TButton"
).pack(fill="x", pady=5)

# Status information
status_text = tk.StringVar(
    value="Waiting for a CSV file..."
)

ttk.Label(
    main_frame,
    textvariable=status_text,
    style="Subtitle.TLabel"
).pack(pady=(20, 10))

ttk.Label(
    main_frame,
    text="Your data is processed locally. Original files remain unchanged.",
    style="Subtitle.TLabel"
).pack(pady=(10, 0))

# Start the application
root.mainloop()
