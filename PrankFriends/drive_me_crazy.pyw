import pyautogui
from time import sleep
from random import randint
from pynput import keyboard

# Function to generate random coordinates between x=1919 and y=1079
def generate_random():
	x = randint(1, 1919)
	y = randint(1, 1079)
	return x, y

def on_press(key):
	if key == keyboard.Key.esc:
		return False  # Stop the listener loop

# Connect the on_press function to the listener
with keyboard.Listener(on_press=on_press) as listener:
	# Enter the infinite loop that clicks on random coordinates
	while True:
		x, y = generate_random()
		pyautogui.click(x=x, y=y)
		sleep(0.5)
		if not listener.running:
			break 
