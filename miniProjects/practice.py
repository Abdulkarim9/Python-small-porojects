import random
import time
import os

def animate_text(text, delay=0.05, animation_style="typewriter"):
    """Animates text output with various styles."""

    if animation_style == "typewriter":
        for char in text:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()  # Newline at the end
    elif animation_style == "fade_in":
        for i in range(len(text) + 1):
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
            print(text[:i])
            time.sleep(delay * 2)
    elif animation_style == "random_reveal":
        indices = list(range(len(text)))
        random.shuffle(indices)
        revealed = [" "] * len(text)
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in indices:
          revealed[i] = text[i]
          print("".join(revealed))
          time.sleep(delay)
    else:
      print(text)


def generate_starfield(width, height, density=0.05):
    """Generates a simple starfield as a list of strings."""
    starfield = []
    for _ in range(height):
        row = "".join("*" if random.random() < density else " " for _ in range(width))
        starfield.append(row)
    return starfield

def display_starfield(starfield):
    """Displays the starfield with scrolling effect."""
    for row in starfield:
        print(row)
        time.sleep(0.1)
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    animate_text("Welcome to the Python Starry Night!", animation_style="typewriter")
    time.sleep(1)
    animate_text("Preparing for launch...", animation_style="fade_in")
    time.sleep(1)

    width = 40
    height = 10

    for _ in range(3): #Animate Starfield three times
        starfield = generate_starfield(width, height)
        display_starfield(starfield)

    animate_text("Behold!", animation_style="random_reveal")

    message = "A Pythonic Constellation!"
    animate_text(message, delay=0.03, animation_style="typewriter")
    time.sleep(1)
    print("\n")
    animate_text("Thank you for watching!", animation_style="fade_in")

if __name__ == "__main__":
    main()