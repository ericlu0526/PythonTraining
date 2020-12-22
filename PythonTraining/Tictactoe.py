#A simple tic tac toe game
#input and output for player to type in
#visualize the console
#Error handling, make sure the moves are valid
#Determine is there is a winner
from colorama import Fore, Back, Style, init
import itertools


init()
print("Here is your tic tac toe game")
#gameBoard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#functions declaration here
def gameBoardShow():
    try:
        count = 0
        print("   0  1  2")
        for row in  gameBoard:
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + " X " + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.MAGENTA + " O "+Style.RESET_ALL
            print(count, colored_row)
            count= count+1
        return True
    except:
        print("A bad thing just happened.")
        return False



def setValOfBoard(row, col, val):
    try:
        if gameBoard[row][col]!=0:
            print("The space is occupied!")
            return False
        else:
            gameBoard[row][col] = val
            return True
    except IndexError:
        print("Did you attempt to play a row or column outside the range of 0,1 or 2? (IndexError) ")
        return False
    except Exception as e:
        print(str(e))
        return False

def checkHoriWin():
    for row in  gameBoard:
        elem1 = row[0]
        elem2 = row[1]
        elem3 = row[2]
        if elem1 == elem2 == elem3 and elem1!=0:
            print("Get winner")
            print(f"Player {row[0]} is the winner!")
            return True
    return False

def checkVerWin():
    for col in range(len(gameBoard[0])):
        checkArr = []
        for row in gameBoard:
            checkArr.append(row[col])
            #print(row[col])
        if checkArr[0] == checkArr[1]==checkArr[2] and checkArr[0]!=0:
            print(f"Player {checkArr[0]} is the winner!")
            return True
    return False

def checkDia1Win():
     check = []
     for i in range(len(gameBoard[0])):
         check.append(gameBoard[i][len(gameBoard[0])-i-1])
     if check[0] == check[1]==check[2] and check[0]!=0:
         print(f"Player {check[0]} is the winner!(DIA /)")
         return True
     return False

def checkDia2Win():
     check = []
     for i in range(len(gameBoard[0])):
         check.append(gameBoard[i][i])
     if check[0] == check[1]==check[2] and check[0]!=0:
         print(f"Player {check[0]} is the winner!(DIA \)")
         return True
     return False

"""

gameBoardShow()
setValOfBoard(1,0,2)
setValOfBoard(1,1,2)
setValOfBoard(1,2,2)
setValOfBoard(2,2,1)
setValOfBoard(1,2,1)
setValOfBoard(0,2,1)
setValOfBoard(0,2,2)
setValOfBoard(2,0,2)

print("After some action")
gameBoardShow()
checkHoriWin()
checkVerWin()
checkDia1Win()

"""
play = True
players = [1,2]

while play:
    gameBoard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    game_won = False
    player_cycle = itertools.cycle([1, 2])
    gameBoardShow()
    while not game_won:
        current_player =next(player_cycle)
        moveValid = False
        while not moveValid:
            print(f"Player: {current_player}")
            column_choice = int(input("Which column?"))
            row_choice = int(input("Which row?"))
            moveValid = setValOfBoard(row_choice, column_choice, current_player)
        
        print("After setting")
        gameBoardShow()
        horRet = verRet = dia1Ret = dia2Ret = False
        horRet = checkHoriWin()
        verRet = checkVerWin()
        dia1Ret = checkDia1Win()
        dia2Ret = checkDia2Win()

        if(dia1Ret or dia2Ret or horRet or verRet):
            game_won = True
            print("End game")
    again = input("Do you want to play again")
    if again.lower() == "y":
        print("restarting , here we go")
    elif again.lower() == "n":
        print("Bye")
        play = False
    else:
        print("not a valid answer, but c ya")
        play = False