import pyautogui
import tkinter as tk
from PIL import Image
import time

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print("Width =", screen_width)
print("Height =", screen_height)

def getCardName(card, eck, kreuz, herz, schaufel):
    for i in range (len(kreuz)):
        if card == kreuz[i]:
            if i == 0:
                card = 'Kreuz Ass'
            elif i == 10:
                card = 'Kreuz Bauer'
            elif i == 11:
                card = 'Kreuz Dame'
            elif i == 12:
                card = 'Kreuz König'
            else:
                card = 'Kreuz ' + str(i + 1)
        
        elif card == herz[i]:
            if i == 0:
                card = 'Herz Ass'
            elif i == 10:
                card = 'Herz Bauer'
            elif i == 11:
                card = 'Herz Dame'
            elif i == 12:
                card = 'Herz König'
            else:
                card = 'Herz ' + str(i + 1)
        elif card == eck[i]:
            if i == 0:
                card = 'Eck Ass'
            elif i == 10:
                card = 'Eck Bauer'
            elif i == 11:
                card = 'Eck Dame'
            elif i == 12:
                card = 'Eck König'
            else:
                card = 'Eck ' + str(i + 1)
        elif card == schaufel[i]:
            if i == 0:
                card = 'Schaufel Ass'
            elif i == 10:
                card = 'Schaufel Bauer'
            elif i == 11:
                card = 'Schaufel Dame'
            elif i == 12:
                card = 'Schaufel König'
            else:
                card = 'Schaufel ' + str(i + 1)


    
    return card

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

    return kreuz, eck, herz, schaufel

def getCardTopRight():
    kreuz, eck, herz, schaufel = generateCards()

    card1 = 'Unknown'
    card1Name = 'Unknown'
    for card in range (len(kreuz)):
        if kreuz[card] != 0:
            card1 = kreuz[card]
            break
        elif eck[card] != 0:
            card1 = eck[card]
            break
        elif herz[card] != 0:
            card1 = herz[card]
            break
        elif schaufel[card] != 0:
            card1 = schaufel[card]
            break

    card1Name = getCardName(card1, eck, kreuz, herz, schaufel)

    for card in range (len(eck)):
        if eck[card] != 0:
            if card1.x > eck[card].x or card1.y > eck[card].y:
                card1 = eck[card]
                card1Name = getCardName(eck[card], eck, kreuz, herz, schaufel)
        
        if herz[card] != 0:
            if card1.x > herz[card].x or card1.y > herz[card].y:
                card1 = herz[card]
                card1Name = getCardName(herz[card], eck, kreuz, herz, schaufel)
        
        if schaufel[card] != 0:
            if card1.x > schaufel[card].x or card1.y > schaufel[card].y:
                card1 = schaufel[card]
                card1Name = getCardName(schaufel[card], eck, kreuz, herz, schaufel)
        
        if kreuz[card] != 0:
            if card1.x > kreuz[card].x or card1.y > kreuz[card].y:
                card1 = kreuz[card]
                card1Name = getCardName(kreuz[card], eck, kreuz, herz, schaufel)

    
    print(card1)
    print(card1Name)
    pyautogui.click(card1.x, card1.y)


genCards=tk.Button(root, text='Karten', fg='black', command=getCardTopRight)

btn=tk.Button(root, text="ok", fg='blue', command=codeablaufen)
btn.place(x=80, y=100)
genCards.place(x=80, y=20)
root.title('Hello Python')
root.geometry("300x200")
root.mainloop()