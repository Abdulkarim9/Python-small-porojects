import pyautogui
import time

# Open Notepad
pyautogui.hotkey('win', 'r')
pyautogui.typewrite('notepad')
pyautogui.hotkey('enter')
time.sleep(1)

# Type text letter by letter
text = """
My love, my heart, my shining star,
You light up my life, near and far.
Your beauty, grace, and gentle touch,
Make my heart flutter, my love for you so much.

With each beat of my heart, I long,
To hold you close, where you belong.
In your arms, my world is complete,
With you by my side, my life is sweet.

Your smile, your laugh, your tender kiss,
Fill my soul with an unending bliss.
I promise to love you, now and always,
Through the good times, and through the days.

You are my love, my heart, my all,
Together forever, we will stand tall.
My dear, I love you more than words can say,
Forever and always, my love will stay.

With this poem, my heart I bare,
To you my love, forever to share.
"""

for letter in text:
    pyautogui.typewrite(letter)
