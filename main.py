import pyautogui
<<<<<<< Updated upstream
import tkinter as tk
=======
import time
>>>>>>> Stashed changes

time.sleep(3)
img1 = pyautogui.screenshot('screenshot.png')

<<<<<<< Updated upstream


root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print("Width =", screen_width)
print("Height =", screen_height)
=======
koenig1 = pyautogui.center(pyautogui.locateOnScreen('karten/kreuz/koenig.png'))

print(koenig1.x)
>>>>>>> Stashed changes
