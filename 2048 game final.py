
import random
import copy
boardsize = 4


def display():
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element
    numSpace = len(str(largest))
    for row in board:
        currentRow = "|"
        for element in row:
            if element == 0:
                currentRow += " " * numSpace + "|"
            else:
                currentRow += (" "*(numSpace-len(str(element)))) + \
                    str(element)+"|"
        print(currentRow)




def mergeOnerowL(row):
    for j in range(boardsize):
        for i in range(boardsize-1, 0, -1):
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0
        for i in range(boardsize-1):
            if row[i] == row[i+1]:
                row[i] *= 2
                row[i+1] = 0
        for i in range(boardsize-1, 0, -1):
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0
    return row


def merge_left(currentboard):
    for i in range(boardsize):
        currentboard[i] = mergeOnerowL(currentboard[i])
    return currentboard

def reverse(row):
  new=[]
  for i in range(boardsize-1,-1,-1):
    new.append(row[i])
  return new
def merge_Right(currentboard):
    for i in range(boardsize):
       currentboard[i]=reverse(currentboard[i])
       currentboard[i]=mergeOnerowL(currentboard[i])
       currentboard[i]=reverse(currentboard[i])
    return currentboard
def transpose(currentboard):
    for j in range(boardsize):
        for i in range(j,boardsize):
            if not i==j:
                temp=currentboard[j][i]
                currentboard[j][i]=currentboard[i][j]
                currentboard[i][j]=temp
    return currentboard
def merge_up(currentboard):
    currentboard=transpose(currentboard)
    currentboard=merge_left(currentboard)
    currentboard=transpose(currentboard)
    return currentboard
def merge_down(currentboard):
    currentboard=transpose(currentboard)
    currentboard=merge_Right(currentboard)
    currentboard=transpose(currentboard)
    return currentboard
def picknewvalue():
    if random.randint(1,8)==1:
        return 4
    else:
        return 2
def addnewvalue():
    rownum=random.randint(0,boardsize-1)
    colnum=random.randint(0,boardsize-1)
    while not board[rownum][colnum]==0:
        rownum=random.randint(0,boardsize-1)
        colnum=random.randint(0,boardsize-1)
    board[rownum][colnum]=picknewvalue()
def won():
    for row in board:
        if 2048 in row:
            return True
    return False
def noMoves():
    tempboard1=copy.deepcopy(board)
    tempboard2=copy.deepcopy(board)
    tempboard1=merge_down(tempboard1)
    if tempboard1==tempboard2:
        tempboard1=merge_up(tempboard1)
        if tempboard1==tempboard2:
            tempboard1=merge_Right(tempboard1)
            if tempboard1==tempboard2:
                tempboard1=merge_left(tempboard1)
                if tempboard1==tempboard2:
                    return True
    return False

board = []
for i in range (boardsize):
    row=[]
    for j in range(boardsize):
        row.append(0)
    board.append(row)
numneeded=2
while numneeded>0:
    rownum=random.randint(0,boardsize-1)
    colnum=random.randint(0,boardsize-1)
    if board[rownum][colnum]==0:
       board[rownum][colnum]=picknewvalue()
       numneeded-=1

print("Welcome to 2048 game , in this game you have to merge NUMBERS and combine them to 2048. USE 'D' 'W' 'A' 'S' TO MERGE THE NUMBERS RIGHT , UP , LEFT , DOWN respectively \n\n HERE IS THE STARTING BOARD")
display()
gameover=False
while not gameover:
    move=input("which way do you want to merge?")
    validinput=True
    tempboard=copy.deepcopy(board)
    if move=="d":
        board=merge_Right(board)
    elif move=="w":
        board=merge_up(board)
    elif move=="a":
        board=merge_left(board)
    elif move=="s":
        board=merge_down(board)
    else :
        validinput=False
    if not validinput:
        print("you have not entered a valid input , please try again")
    else :
        if board==tempboard:
            print("please try a different direction!")
        else:
            if won():
                display()
                print("You won!")
                gameover=True
            else:
             addnewvalue()
             display()
             if noMoves():
                 print("Sorry , you have no moves left!")
                 gameover=True            
   

