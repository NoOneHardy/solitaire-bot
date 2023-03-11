import pyautogui
import tkinter as tk
from PIL import Image
import time

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

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
    conf = 1
    info = None
    while info == None and conf >= 0.9:
        try:
            info = pyautogui.center(pyautogui.locateOnScreen('karten/' + color + '/' + str(card) + '.png', confidence=conf))
        except:
            conf -= 0.01
    
    if info != None:
        print(str(color) + ", " + str(card) + ": " + str(conf))
        return info
    else:
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
        #time.sleep(2)
        #pyautogui.click(eck[i].x, eck[i].y)
        print(eck[i])
    
    print()
    print('Herz:')
    for i in range(len(herz)):
        #time.sleep(2)
        #pyautogui.click(herz[i].x, herz[i].y)
        print(herz[i])

    print()
    print('Schaufel:')
    for i in range(len(schaufel)):
        #time.sleep(2)
        #pyautogui.click(schaufel[i].x, schaufel[i].y)        
        print(schaufel[i])

    print()
    print('Kreuz:')
    for i in range(len(kreuz)):
        #time.sleep(2)
        #pyautogui.click(kreuz[i].x, kreuz[i].y)
        print(kreuz[i])

    return kreuz, eck, herz, schaufel

def getCardTopLeft(kreuz, eck, herz, schaufel):

    cardTopLeft = 'Unknown'
    card1Name = 'Unknown'
    for card in range (len(kreuz)):
        if kreuz[card] != 0:
            cardTopLeft = kreuz[card]
            break
        elif eck[card] != 0:
            cardTopLeft = eck[card]
            break
        elif herz[card] != 0:
            cardTopLeft = herz[card]
            break
        elif schaufel[card] != 0:
            cardTopLeft = schaufel[card]
            break

    card1Name = getCardName(cardTopLeft, eck, kreuz, herz, schaufel)

    for card in range (len(eck)):
        if eck[card] != 0:
            if cardTopLeft.x > eck[card].x or cardTopLeft.y > eck[card].y:
                cardTopLeft = eck[card]
                card1Name = getCardName(eck[card], eck, kreuz, herz, schaufel)
        
        if herz[card] != 0:
            if cardTopLeft.x > herz[card].x or cardTopLeft.y > herz[card].y:
                cardTopLeft = herz[card]
                card1Name = getCardName(herz[card], eck, kreuz, herz, schaufel)
        
        if schaufel[card] != 0:
            if cardTopLeft.x > schaufel[card].x or cardTopLeft.y > schaufel[card].y:
                cardTopLeft = schaufel[card]
                card1Name = getCardName(schaufel[card], eck, kreuz, herz, schaufel)
        
        if kreuz[card] != 0:
            if cardTopLeft.x > kreuz[card].x or cardTopLeft.y > kreuz[card].y:
                cardTopLeft = kreuz[card]
                card1Name = getCardName(kreuz[card], eck, kreuz, herz, schaufel)

    
    print(cardTopLeft)
    print(card1Name)
    return cardTopLeft

def getFirstCards():
    #kreuz, eck, herz, schaufel = generateCards()

    cards = [[None] * 24] * 8
    cards[1][0] = 'Test' #getCardTopLeft(kreuz, eck, herz, schaufel)
    print(cards)
    
genCards=tk.Button(root, text='Karten', fg='black', command=getFirstCards)

btn=tk.Button(root, text="ok", fg='blue', command=codeablaufen)
btn.place(x=80, y=100)
genCards.place(x=80, y=20)
root.title('Hello Python')
root.geometry("300x200")
root.mainloop()