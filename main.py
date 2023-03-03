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
    eck = [None] * 13
    schaufel = [None] * 13
    herz = [None] * 13
    kreuz = [None] * 13

    for card in range (1, 14):
        eck[card - 1] = searchCard(card, 'eck')
        schaufel[card - 1] = searchCard(card, 'schaufel')
        herz[card - 1] = searchCard(card, 'herz')
        kreuz[card - 1] = searchCard(card, 'kreuz')

    print()
    print('Eck:')
    for i in range(len(eck)):
        print(eck[i])
    
    print()
    print('Herz:')
    for i in range(len(herz)):
        print(herz[i])

    print()
    print('Schaufel:')
    for i in range(len(schaufel)):
        print(schaufel[i])

    print()
    print('Kreuz:')
    for i in range(len(kreuz)):
        print(kreuz[i])

genCards=tk.Button(root, text='Karten', fg='black', command=generateCards)

btn=tk.Button(root, text="ok", fg='blue', command=codeablaufen)
btn.place(x=80, y=100)
genCards.place(x=80, y=20)
root.title('Hello Python')
root.geometry("300x200")
root.mainloop()
