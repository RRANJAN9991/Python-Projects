import random
import curses
board = [] #Using array as the game board.

#We will have dictionaries storing sublists. (Keys will be the name of the ship and the values will be the sublists.)
#Each subllist contains the coordinates for a ship.
size5 = [ [ [] for i in range(2) ] for i in range(5) ]
size4 = [ [ [] for i in range(2) ] for i in range(4) ]
size3 = [ [ [] for i in range(2) ] for i in range(3) ]
size3_ = [ [ [] for i in range(2) ] for i in range(3) ]
size2 = [ [ [] for i in range(2) ] for i in range(2) ]
dict = {"Carrier": size5, "Battleship": size4, "Cruiser": size3,"Submarine": size3_, "Destroyer": size2}


#Initialize the game board to all O's.
for x in range(10):
    board.append(["O"] * 10)

def EmptyBoard():
    b = []
    i = 1
    for x in range(10):
        b.append(['{:>2}'.format(str(i)), '\x1b[2;34;44m' + 'O' + '\x1b[0m', '\x1b[2;34;44m' + 'O' + '\x1b[0m', '\x1b[2;34;44m' + 'O' + '\x1b[0m',
                  '\x1b[2;34;44m' + 'O' + '\x1b[0m', '\x1b[2;34;44m' + 'O' + '\x1b[0m', '\x1b[2;34;44m' + 'O' + '\x1b[0m',
                  '\x1b[2;34;44m' + 'O' + '\x1b[0m', '\x1b[2;34;44m' + 'O' + '\x1b[0m', '\x1b[2;34;44m' + 'O' + '\x1b[0m',
                  '\x1b[2;34;44m' + 'O' + '\x1b[0m'])
        #b.append(['\x1b[2;34;44m' + 'O' + '\x1b[0m'] * 10)
        i += 1
    indices = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    b.append(['{:>1.2} {:>2} {:>1.2} {:>1.2} {:>1.2} {:>1.2} {:>1.2} {:>1.2} {:>1.2} {:>1.2} {:>1.2}'.format(*indices)])
    return b

#console = curses.initscr()

#Prints the game board.
def printBoard(board):

    for row in board:
        print((" ").join(row))

#Checks whether or not a ship is already present when generating new ships. Upon genration of the indices of a new ship,
#this function will be called and if an old ship is already present in the same spot of the new ship, then
#this function will return false. (And the new ship will be regenerated.)
def checkboard(rowNumStart, colNumStart, rowNum, colNum, chooseHorVert, chooseLeftRightUpDown):
    if chooseHorVert == 0: #horizontal check
        for i in range(colNumStart, colNum + 1):
            if board[rowNum][i] != "O":
                return False
    else: #vertical check
         for i in range(rowNumStart, rowNum + 1):
            if board[i][colNum] != "O":
                return False
    return True

#Inserts all the ships on the game board. (Marked as an X) Also adds all the coordinates to each of the sublists
#in the respective values in the dictionary.
def assignFunction(rowNumStart, colNumStart, rowNum, colNum, sizeShip, size3ship):
    counter = 0
    if rowNumStart == rowNum: #Inserting horizontal
        
        if sizeShip == 5:
            for i in range(colNumStart, colNum + 1):
                board[rowNum][i] = "X"
                dict["Carrier"][counter][0] = rowNum
                dict["Carrier"][counter][1] = i
                counter = counter + 1
        elif sizeShip == 4:
            for i in range(colNumStart, colNum + 1):
                board[rowNum][i] = "X"
                dict["Battleship"][counter][0] = rowNum
                dict["Battleship"][counter][1] = i
                counter = counter + 1
        elif sizeShip == 3:
            if size3ship == 0:
                for i in range(colNumStart, colNum + 1):
                    board[rowNum][i] = "X"
                    dict["Cruiser"][counter][0] = rowNum
                    dict["Cruiser"][counter][1] = i
                    counter = counter + 1
            else:
                for i in range(colNumStart, colNum + 1):
                    board[rowNum][i] = "X"
                    dict["Submarine"][counter][0] = rowNum
                    dict["Submarine"][counter][1] = i
                    counter = counter + 1
        elif sizeShip == 2:
            for i in range(colNumStart, colNum + 1):
                board[rowNum][i] = "X"
                dict["Destroyer"][counter][0] = rowNum
                dict["Destroyer"][counter][1] = i
                counter = counter + 1

    else: #Inserting vertically
        
        if sizeShip == 5:
            for i in range(rowNumStart, rowNum + 1):
                board[i][colNum] = "X"
                dict["Carrier"][counter][0] = i
                dict["Carrier"][counter][1] = colNum
                counter = counter + 1
        elif sizeShip == 4:
            for i in range(rowNumStart, rowNum + 1):
                board[i][colNum] = "X"
                dict["Battleship"][counter][0] = i
                dict["Battleship"][counter][1] = colNum
                counter = counter + 1
        elif sizeShip == 3:
            if size3ship == 0:
                for i in range(rowNumStart, rowNum + 1):
                    board[i][colNum] = "X"
                    dict["Cruiser"][counter][0] = i
                    dict["Cruiser"][counter][1] = colNum
                    counter = counter + 1
                
            else:
                for i in range(rowNumStart, rowNum + 1):
                    board[i][colNum] = "X"
                    dict["Submarine"][counter][0] = i
                    dict["Submarine"][counter][1] = colNum
                    counter = counter + 1
        elif sizeShip == 2:
            for i in range(rowNumStart, rowNum + 1):
                board[i][colNum] = "X"
                dict["Destroyer"][counter][0] = i
                dict["Destroyer"][counter][1] = colNum
                counter = counter + 1
        
    
        
#Randomizes the generation of the ships on the game board. Either horizontally left/right or vertically down/up. (All equal chance)
#If the size of the ship is 3, then enter 0 next to it for the cruiser, or 1 next to it for the submarine.(Otherwise if the size of the ship is not 3, then enter
#-1 next to the size parameter.)
#For example, to generate the size 5 ship (Carrier), use generateShips(5,-1). To generate the size 2 ship (Destroyer), use generateShips(2,-1).
#To generate the size 3 ship (Carrier), use generateShips(3,0). To generate the size 3 ship (Submarine), use generateShips(3,1).

def generateShips(sizeShip, size3ship):
   
    shipGen = False
    while shipGen == False:
        rowNum = random.randint(1,9)
        colNum= random.randint(1,9)
        chooseHorVert = random.randint(0,1)
        chooseLeftRightUpDown = random.randint(0,1)

        if chooseHorVert == 0: #Go horizontally
            if chooseLeftRightUpDown == 0: 
                colNumStart = colNum - sizeShip + 1
                if (colNumStart >= 0): #Go left horizontally
                    if checkboard(rowNum, colNumStart, rowNum, colNum, chooseHorVert, chooseLeftRightUpDown) == True:
                        assignFunction(rowNum, colNumStart, rowNum, colNum,sizeShip, size3ship)
                    else:
                        continue
                else: #Go right horizontally
                    colNumEnd = colNum + sizeShip - 1
                    if checkboard(rowNum, colNum, rowNum, colNumEnd, chooseHorVert, chooseLeftRightUpDown) == True:
                        assignFunction(rowNum, colNum, rowNum, colNumEnd,sizeShip, size3ship)
                    else:
                        continue
            else: 
                colNumEnd = colNum + sizeShip - 1
                if colNumEnd <= 9: #Go right horizontally
                    if checkboard(rowNum, colNum, rowNum, colNumEnd, chooseHorVert, chooseLeftRightUpDown) == True:
                        assignFunction(rowNum, colNum, rowNum, colNumEnd,sizeShip, size3ship)
                    else:
                        continue
                else: #Go left horizontally
                    colNumStart = colNum - sizeShip + 1
                    if checkboard(rowNum, colNumStart, rowNum, colNum, chooseHorVert, chooseLeftRightUpDown) == True:
                        assignFunction(rowNum, colNumStart, rowNum, colNum,sizeShip, size3ship)
                    else:
                        continue
            
        else: #Go vertically
            if chooseLeftRightUpDown == 0:
                rowNumStart = rowNum - sizeShip + 1
                if rowNumStart >= 0: #Go vertically up
                    if checkboard(rowNumStart, colNum, rowNum, colNum, chooseHorVert, chooseLeftRightUpDown) == True:
                       
                        assignFunction(rowNumStart, colNum, rowNum, colNum,sizeShip, size3ship)
                    else:
                        continue    
                else: #Go vertically down
                    rowNumEnd = rowNum + sizeShip - 1
                    if checkboard(rowNum, colNum, rowNumEnd, colNum, chooseHorVert, chooseLeftRightUpDown) == True:
                        assignFunction(rowNum, colNum, rowNumEnd, colNum,sizeShip, size3ship)
                    else:
                        continue
            else: 
                rowNumEnd = rowNum + sizeShip - 1
                if rowNumEnd <= 9: #Go vertically down
                    if checkboard(rowNum, colNum, rowNumEnd, colNum, chooseHorVert, chooseLeftRightUpDown) == True:
                        assignFunction(rowNum, colNum, rowNumEnd, colNum,sizeShip, size3ship)
                    else:
                        continue
                else: #go vertically up
                    rowNumStart = rowNum - sizeShip + 1
                    if checkboard(rowNumStart, colNum, rowNum, colNum, chooseHorVert, chooseLeftRightUpDown) == True:
                        assignFunction(rowNumStart, colNum, rowNum, colNum,sizeShip, size3ship)
                    else:
                        continue
        
        shipGen = True
generateShips(5,-1)
generateShips(4,-1)
generateShips(3,0)
generateShips(3,1)
generateShips(2,-1)
#print(dict)
#printBoard(board)

#parses a user's input, and marks an empty game board according to the generated random board. The board starts off
#fully blue, and a tile turns red if a ship exists there, and white if not. You have 5 guesses; if you guess correctly
#you do not lose a guess.
def parser(board, dictionary):
    total_guesses = 0
    newboard = EmptyBoard()
    prev_guesses = []

    while (total_guesses < 5):
        user_guess = raw_input("Enter your guess by row and column separated by a space " )
        user_list = user_guess.split()
        try:
            r = int(user_list[0])
            c = int(user_list[1])
        except ValueError:
            print("Those aren't integers! Try again.")
            continue
        #check that user input is valid and readable
        if not any(dictionary.values()):
            print("Game over. You Win!")
            break

        if int(user_list[0]) and int(user_list[1]) and int(user_list[0]) in range(1,11) and \
            int(user_list[1]) in range(1,11) and [int(user_list[0]),int(user_list[1])] not in prev_guesses and \
            any(dictionary.values()):

            row = int(user_list[0])
            col = int(user_list[1])
            res = True

            #print([row, col])
            #print(dictionary.values())
            #iterate through ship coordinates, and if guess matches one of these, change guess's coordinates to red
            for (key,val) in dictionary.items():
                #print(key, val)
                if [row,col] in val:
                    newboard[row-1][col] = '\x1b[2;31;41m' + 'Y' + '\x1b[0m'
                    print("Good guess! You just hit my " + key + ".")
                    val.remove([row,col])
                    printBoard(newboard)
                else:
                    res = not res
                prev_guesses.append([row, col])

            #otherwise, if the guess is incorrect, change guess's coordinates to white and increment total guesses by 1
            if not res:
                print("Incorrect, you have " + str(5 - total_guesses - 1) + " guesses left.")
                newboard[row-1][col] = '\x1b[2;37;47m' + 'N' + '\x1b[0m'
                total_guesses += 1
                printBoard(newboard)
        elif [int(user_list[0]),int(user_list[1])] in prev_guesses:
            print("You already guessed those coordinates, please retry.")
        else:
            print("Invalid coordinates. Please retry.")

    if total_guesses == 5:
        print("Game Over! You Lose")
    exit()

parser(board,dict)