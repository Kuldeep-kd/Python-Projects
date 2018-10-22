#Draws Game Board using a list
def Display(board):
    print(' {} | {} | {} \n-----------\n {} | {} | {} \n-----------\n {} | {} | {} '.format(board[7],board[8],board[9],board[4],board[5],board[6],board[1],board[2],board[3]))

#Marks the location with the current player`s Marker
def Place_Marker(board, marker, location):
    board[location] = marker
    return board

#Checks if Player Wins or the Game Ties
def Has_Won(board, mark):
    
    if(board[1]==board[2]==board[3]!=' ' or board[1]==board[5]==board[9]!=' ' or board[1]==board[4]==board[7]!=' ' or board[2]==board[5]==board[8]!=' ' or board[3]==board[6]==board[9]!=' ' or board[4]==board[5]==board[6]!=' ' or board[7]==board[8]==board[9]!=' ' ):
        print("Congratulations {} is the Winner".format(mark))
        return True
    elif (Board_Check(board)):
        print('Ohh! The Game is Tie!')
        return True

#Randomly selects which player will go first
def choose_first():
    if random.randint(0,1):
        print("Player {} goes first!".format('X'))
        return ['X','O']
    else:
        print("Player {} goes first!".format('O'))
        return ['O','X']

#Checks for free space at specified location
def space_check(board, location):
    return board[location]==' '

#Checks if Board has any places left
def Board_Check(board):
    return not ' ' in board

#Checks if the location on Board is available
def player_choice(board):
    global location
    while True:
        x = input("Choose your Next Move! ")
        if x.isnumeric():
            location = int(x)
            if 0 < location < 10:

                if space_check(board, location):
                    os.system('cls')
                    return location

        print('Please Choose a Correct Move!')
        continue
        
#Asks user if they want to play again
def replay():
    return input("You wanna play again? (Yes or No)") == "Yes"


#Main Program
import os
import random

print('Tic Tac Toe!')
location = int()
while True:
    board = ['#']+[' ']*9 #This # is to keep out the 0th index
    location = 0
    marker = choose_first()
    while True:
        #Player 1
        player_choice(board)
        board = Place_Marker(board, marker[0], location)
        Display(board)
        if Has_Won(board, marker[0]):
            break
        # Player 2
        player_choice(board)
        board = Place_Marker(board, marker[1], location)
        Display(board)
        Has_Won(board, marker[1])
        if Has_Won(board, marker[1]):
            break

    if not replay():
        os.system('cls')
        print('Thank You for playing!')
        break