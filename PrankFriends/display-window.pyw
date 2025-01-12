import tkinter as tk
import random



def create_window():
    # Generate random x and y coordinates for the window
    while True:
        x = random.randint(0, 1000)
        y = random.randint(0, 600)

        # Create the window
        window = tk.Tk()
        window.geometry(f"+{x}+{y}")
        window.title("\U0001F600")
        window.mainloop()

if __name__ == "__main__":
    create_window()

