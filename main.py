import random
import time
import sys

boardPos = {'a1': ' ', 'a2': ' ', 'a3': ' ',
            'b1': ' ', 'b2': ' ', 'b3': ' ',
            'c1': ' ', 'c2': ' ', 'c3': ' '}


def preventwin():
    for i in boardPos.keys():
        preventboard = boardPos
        if preventboard[i] == " ":
            preventboard[i] = playerLetter
            if checkwin(preventboard, playerLetter) == 'no':
                preventboard[i] = ' '
            if checkwin(preventboard, playerLetter) == 'won':
                boardPos[i] = aiLetter
                playermove(playerLetter)
                break
        else:*
            continue


def checkcorners():
    corner = random.randint(1, 4)
    corners = ['a1', 'a3', 'c1', 'c3']
    for i in corners:
        if boardPos[i] == ' ':
            boardPos[i] = aiLetter
            break


def fullboard():
    a1 = False
    a2 = False
    a3 = False
    b1 = False
    b2 = False
    b3 = False
    c1 = False
    c2 = False
    c3 = False
    if boardPos['a1'] == playerLetter or boardPos['a1'] == aiLetter:
        a1 = True
    if boardPos['a2'] == playerLetter or boardPos['a2'] == aiLetter:
        a2 = True
    if boardPos['a3'] == playerLetter or boardPos['a3'] == aiLetter:
        a3 = True
    if boardPos['b1'] == playerLetter or boardPos['b1'] == aiLetter:
        b1 = True
    if boardPos['b2'] == playerLetter or boardPos['b2'] == aiLetter:
        b2 = True
    if boardPos['b3'] == playerLetter or boardPos['b3'] == aiLetter:
        b3 = True
    if boardPos['c1'] == playerLetter or boardPos['c1'] == aiLetter:
        c1 = True
    if boardPos['c2'] == playerLetter or boardPos['c2'] == aiLetter:
        c2 = True
    if boardPos['c3'] == playerLetter or boardPos['c3'] == aiLetter:
        c3 = True

    if a1 and a2 and a3 and b1 and b2 and b3 and c1 and c2 and c3:
        tiegame()
    else:
        return False


def printboard(board):
    # prints board
    print(board['a1'] + "|" + board['a2'] + "|" + board['a3'])
    print("-+-+-")
    print(board['b1'] + "|" + board['b2'] + "|" + board['b3'])
    print("-+-+-")
    print(board['c1'] + "|" + board['c2'] + "|" + board['c3'])


def aimovefirst(letter):
    time.sleep(0.5)
    space = random.randint(1, 5)
    if space == 1:
        boardPos['b2'] = letter
    if space == 2:
        boardPos['a1'] = letter
    if space == 3:
        boardPos['a3'] = letter
    if space == 4:
        boardPos['c1'] = letter
    if space == 5:
        boardPos['c3'] = letter
    playermove(playerLetter)


def clearboard(board):
    board['a1'] = ' '
    board['b1'] = ' '
    board['c1'] = ' '
    board['a2'] = ' '
    board['b2'] = ' '
    board['c2'] = ' '
    board['a3'] = ' '
    board['b3'] = ' '
    board['c3'] = ' '


def tiegame():
    printboard(boardPos)
    time.sleep(0.5)
    print("Tie!")
    print("Keep playing? (Y/N)")
    yn = input()
    if yn == "y":
        clearboard(boardPos)
        startgame()
    if yn == "n":
        sys.exit()


def wincondition():
    printboard(boardPos)
    time.sleep(0.5)
    print("_____ won!")
    print("Keep playing? (Y/N)")
    yn = input()
    if yn == "y":
        clearboard(boardPos)
        startgame()
    if yn == "n":
        sys.exit()


def playermove(letter):
    if checkwin(boardPos, aiLetter) == "won":
        wincondition()
    fullboard()
    printboard(boardPos)
    print("Make your move! (Use the numpad.)")
    move = input()
    while True:
        if move == "1":
            if boardPos['c1'] == "X" or boardPos['c1'] == "O":
                print("You can't choose there! Try again.")
                continue
            else:
                boardPos['c1'] = letter
                time.sleep(0.5)
                break
        if move == "2":
            if boardPos['c2'] == "X" or boardPos['c2'] == "O":
                print("You can't choose there! Try again.")
                continue
            else:
                boardPos['c2'] = letter
                time.sleep(0.5)
                break
        if move == "3":
            if boardPos['c3'] == "X" or boardPos['c3'] == "O":
                print("You can't choose there! Try again.")
                continue
            else:
                boardPos['c3'] = letter
                time.sleep(0.5)
                break
        if move == "4":
            if boardPos['b1'] == "X" or boardPos['b1'] == "O":
                print("You can't choose there! Try again.")
                continue
            else:
                boardPos['b1'] = letter
                time.sleep(0.5)
                break
        if move == "5":
            if boardPos['b2'] == "X" or boardPos['b2'] == "O":
                print("You can't choose there! Try again.")
                continue
            else:
                boardPos['b2'] = letter
                time.sleep(0.5)
                break
        if move == "6":
            if boardPos['b3'] == "X" or boardPos['b3'] == "O":
                print("You can't choose there! Try again.")
                continue
            else:
                boardPos['b3'] = letter
                time.sleep(0.5)
                break
        if move == "7":
            if boardPos['a1'] == "X" or boardPos['a1'] == "O":
                print("You can't choose there! Try again.")
                continue
            else:
                boardPos['a1'] = letter
                time.sleep(0.5)
                break
        if move == "8":
            if boardPos['a2'] == "X" or boardPos['a2'] == "O":
                print("You can't choose there! Try again.")
                continue
            else:
                boardPos['a2'] = letter
                time.sleep(0.5)
                break
        if move == "9":
            if boardPos['a3'] == "X" or boardPos['a3'] == "O":
                print("You can't choose there! Try again.")
                continue
            else:
                boardPos['a3'] = letter
                time.sleep(0.5)
                break
    aimove()


def testempty():
    if boardPos['b2'] == aiLetter:
        while True:
            move = random.randint(1, 4)
            if move == 1:
                if boardPos['a1'] == "X" or boardPos['a1'] == "O":
                    continue
                else:
                    boardPos['a1'] = aiLetter
                    break
            if move == 2:
                if boardPos['a3'] == "X" or boardPos['a3'] == "O":
                    continue
                else:
                    boardPos['a3'] = aiLetter
                    break
            if move == 3:
                if boardPos['c1'] == "X" or boardPos['c1'] == "O":
                    continue
                else:
                    boardPos['c1'] = aiLetter
                    break
            if move == 4:
                if boardPos['c3'] == "X" or boardPos['c3'] == "O":
                    continue
                else:
                    boardPos['c3'] = aiLetter
                    break
        playermove(playerLetter)
    elif boardPos['b2'] == playerLetter:
        while True:
            move = random.randint(1, 4)
            if move == 1:
                if boardPos['a1'] == "X" or boardPos['a1'] == "O":
                    continue
                else:
                    boardPos['a1'] = aiLetter
                    break
            if move == 2:
                if boardPos['a3'] == "X" or boardPos['a3'] == "O":
                    continue
                else:
                    boardPos['a3'] = aiLetter
                    break
            if move == 3:
                if boardPos['c1'] == "X" or boardPos['c1'] == "O":
                    continue
                else:
                    boardPos['c1'] = aiLetter
                    break
            if move == 4:
                if boardPos['c3'] == "X" or boardPos['c3'] == "O":
                    continue
                else:
                    boardPos['c3'] = aiLetter
                    break
        playermove(playerLetter)
    elif boardPos['b2'] == ' ':
        boardPos['b2'] = aiLetter
        playermove(playerLetter)


def checkmiddle():
    if boardPos['b2'] == " ":
        return True
    else:
        return False


def trywin():
    for i in boardPos.keys():
        winBoard = boardPos
        if winBoard[i] == " ":
            winBoard[i] = aiLetter
            if checkwin(winBoard, aiLetter) == 'no':
                winBoard[i] = ' '
            else:
                boardPos[i] = aiLetter
                playermove(playerLetter)
                break
        else:
            continue


def aimove():
    if checkwin(boardPos, playerLetter) == "won":
        wincondition()
    preventwin()
    trywin()
    if checkmiddle():
        boardPos['b2'] = aiLetter
    else:
        checkcorners()
    playermove(playerLetter)


def checkwin(board, letter):
    if board['a1'] == letter and board['a2'] == letter and board['a3'] == letter:
        return 'won'
    elif board['b1'] == letter and board['b2'] == letter and board['b3'] == letter:
        return 'won'
    elif board['c1'] == letter and board['c2'] == letter and board['c3'] == letter:
        return 'won'
    elif board['a1'] == letter and board['b1'] == letter and board['c1'] == letter:
        return 'won'
    elif board['a2'] == letter and board['b2'] == letter and board['c2'] == letter:
        return 'won'
    elif board['a3'] == letter and board['b3'] == letter and board['c3'] == letter:
        return 'won'
    elif board['a1'] == letter and board['b2'] == letter and board['c3'] == letter:
        return 'won'
    elif board['a3'] == letter and board['b2'] == letter and board['c1'] == letter:
        return 'won'
    else:
        return 'no'


def startgame():
    global aiLetter
    global playerLetter
    while True:
        gameOrder = random.randint(1, 2)
        if gameOrder == 1:
            print("The AI will move first!")
            print("The AI is X's, you are O's.")
            aiLetter = 'X'
            playerLetter = 'O'
            aimovefirst(aiLetter)
            break
        if gameOrder == 2:
            print("You will move first!")
            print("The AI is O's, you are X's.")
            aiLetter = 'O'
            playerLetter = 'X'
            playermove(playerLetter)
            break


startgame()