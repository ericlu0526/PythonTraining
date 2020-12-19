#A simple tic tac toe game
#input and output for player to type in
#visualize the console
#Error handling, make sure the moves are valid
#Determine is there is a winner

print("Here is your tic tac toe game")
gameBoard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#functions declaration here
def gameBoardShow():
    try:
        count = 0
        print("   0  1  2")
        for row in  gameBoard:
            print(count, row)
            count= count+1
        return True
    except:
        print("A bad thing just happened.")
        return False



def setValOfBoard(row, col, val):
    try:
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

def checkVerWin():
    for col in range(len(gameBoard[0])):
        checkArr = []
        for row in gameBoard:
            checkArr.append(row[col])
            #print(row[col])
        if checkArr[0] == checkArr[1]==checkArr[2] and checkArr[0]!=0:
            print(f"Player {checkArr[0]} is the winner!")
            return False

def checkDia1Win():
     check = []
     for i in range(len(gameBoard[0])):
         check.append(gameBoard[i][len(gameBoard[0])-i-1])
     if check[0] == check[1]==check[2] and check[0]!=0:
         print(f"Player {check[0]} is the winner!(DIA /)")

def checkDia2Win():
     check = []
     for i in range(len(gameBoard[0])):
         check.append(gameBoard[i][i])
     if check[0] == check[1]==check[2] and check[0]!=0:
         print(f"Player {check[0]} is the winner!(DIA \)")



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