import pyautogui
import tkinter as tk
from PIL import Image
import time

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print("Width =", screen_width)
print("Height =", screen_height)

def codeablaufen():
    # eck6 = pyautogui.center(pyautogui.locateOnScreen('karten/eck/6.png'))
    # print(eck6.x, ",", eck6.y)

    stack = pyautogui.center(pyautogui.locateOnScreen('karten/back.png', confidence=0.9))

    pyautogui.click(stack.x, stack.y)

def searchCard(card, color):
    try:
        info = pyautogui.center(pyautogui.locateOnScreen('karten/' + color + '/' + str(card) + '.png', confidence=0.9))
        return info
    except:
        return 0

def generateCards():
    color = 'eck'
    eck = [None] * 13
    for card in range (13):
        eck[card] = searchCard(card, color)
    
    color = 'schaufel'
    schaufel = [None] * 13
    for card in range (13):
        schaufel[card] =  searchCard(card, color)

    
    color = 'herz'
    herz = [None] * 13
    for card in range (13):
        herz[card] = searchCard(card, color)

    color = 'kreuz'
    kreuz = [None] * 13
    for card in range (13):
        kreuz[card] = searchCard(card, color)

    print(eck)
    print(herz)
    print(schaufel)
    print(kreuz)

genCards=tk.Button(root, text='Karten', fg='black', command=generateCards)

btn=tk.Button(root, text="ok", fg='blue', command=codeablaufen)
btn.place(x=80, y=100)
genCards.place(x=80, y=20)
root.title('Hello Python')
root.geometry("300x200")
root.mainloop()
