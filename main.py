import pyautogui
from PIL import Image

import tkinter as tk
import time

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print("Width =", screen_width)
print("Height =", screen_height)

def codeablaufen():
    eckAss = Image.open('karten/eck/6.png')

    height = eckAss.height * 1080 / screen_height
    width = eckAss.width * 1920 / screen_width

    print("New:", height, width)

    eckAss.resize((int(width), int(height)))

    # eckAss.save('karten/eck/6.png')

    eck6 = pyautogui.center(pyautogui.locateOnScreen(eckAss))
    print(eck6.x, ",", eck6.y)

    stack = pyautogui.center(pyautogui.locateOnScreen('karten/back.png'))

    pyautogui.click(stack.x, stack.y)



btn=tk.Button(root, text="ok", fg='blue', command=codeablaufen)
btn.place(x=80, y=100)
root.title('Hello Python')
root.geometry("300x200")
root.mainloop()
