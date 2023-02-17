import pyautogui
import tkinter as tk

img1 = pyautogui.screenshot('screenshot.png')



root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print("Width =", screen_width)
print("Height =", screen_height)