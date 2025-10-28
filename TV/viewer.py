import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window title
root.title("My First Tkinter Window")

# Set window dimensions (width x height)
root.geometry("500x400")

# Prevent window from being resized
root.resizable(False, False)

# Start the Tkinter event loop
root.mainloop()