def Display(board):
    print(' {} | {} | {} \n-----------\n {} | {} | {} \n-----------\n {} | {} | {} '.format(board[7],board[8],board[9],board[4],board[5],board[6],board[1],board[2],board[3]))

def Choose_Marker():
    x = input("Please choose a Marker X or O ")
    if x in ['X','O']:
        player1 = 'X'
        player2 = 'Y'
    else:
        print("Please enter Correct Marker!")
        Choose_Marker()

def Place_Marker(board, marker, location):
    board[location] = marker
    return board

def Has_Won(board, mark):
    
    if(board[1]==board[2]==board[3]!=' ' or board[1]==board[5]==board[9]!=' ' or board[1]==board[4]==board[7]!=' ' or board[2]==board[5]==board[8]!=' ' or board[3]==board[6]==board[9]!=' ' or board[4]==board[5]==board[6]!=' ' or board[7]==board[8]==board[9]!=' ' ):
        print("Congratulations {} is the Winner".format(mark))
        return True

import random

def choose_first():
    if random.randint(0,1):
        print("Player {} goes first!".format('X'))
        return ['X','O']
    else:
        print("Player {} goes first!".format('O'))
        return ['O','X']

def space_check(board, location):
    if board[location]==' ':
        return True
    else:
        return False

def Board_Check(board):
    return not ' ' in board

def player_choice(board):
    global location
    while True:
        x = input("Choose your Next Move! ")
        if x.isnumeric():
            location = int(x)
            if 0 < location < 10:

                if space_check(board, location):
                    return location

        print('Please Choose a Correct Move!')
        continue
        

def replay():
    return input("You wanna play again? (Yes or No)") == "Yes"

print('Tic Tac Toe!')
location = int()
while True:
    board = ['#']+[' ']*9
    location = 0
    Choose_Marker()
    marker = choose_first()
    while True:
        #Player 1
        player_choice(board)
        board = Place_Marker(board, marker[0], location)
        Display(board)
        if Has_Won(board, marker[0]) or Board_Check(board):
            break
        # Player 2
        player_choice(board)
        board = Place_Marker(board, marker[1], location)
        Display(board)
        Has_Won(board, marker[1])
        if Has_Won(board, marker[1]) or Board_Check(board):
            break

    if not replay():
        break