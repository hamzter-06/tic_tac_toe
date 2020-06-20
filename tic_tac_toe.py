import os

print("Welcome to Tic Tac Toe!!")
# Declare global parameters for player choices
# Gameboard
p ={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
pc = {'Player1':" ","Player2":" "}
game_on = True
turn = ''

def board():
    #os.system('cls')
    print(p[7] + ' | ' + p[8] + ' | ' + p[9])
    print('---------')
    print(p[4] + ' | ' + p[5] + ' | ' + p[6])
    print('---------')
    print(p[1] + ' | ' + p[2] + ' | ' + p[3])

def win_check():

    ## Define and Create winning combos in a list
    winning =[p[1] + p[2] + p[3],
    p[4] + p[5] + p[6],
    p[7] + p[8] + p[9],
    p[1] + p[5] + p[9],
    p[7] + p[5] + p[3],
    p[1] + p[4] + p[7],
    p[2] + p[5] + p[8],
    p[3] + p[6] + p[9]]

    print(winning)
    
    if 'XXX' in winning:
        val = 'X'
        for key,value in pc.items():
            if val == value:
                print(key + ' Wins the game')
                play_again()
    elif 'OOO' in winning:
        val = 'O'
        for key,value in pc.items():
            if val == value:
                print(key + ' Wins the game')
                play_again()
    #elif '' or 'XO' or 'OX' in winning:
    #    pass
    elif '000' and 'XXX' not in winning:
        for i in winning:
            if len(i) == 3:
                print('its a tie')
                break
            else:
                continue
        play_again()

def player():
    global pc
    global turn

# Creating Dictionary for Player X and O assignments
    answer1 = input('Player1 do you want to be X? yes or no:  ')
    if answer1.lower() == 'yes' or answer1.lower() == 'y':
        pc['Player1'] = 'X'
        pc['Player2'] = 'O'
    else:
        pc['Player1'] = 'O'
        pc['Player2'] = 'X'
    
    answer2 = input('Player1 do you want to go first? yes or no: ')
    if answer2.lower() == 'yes' or answer2.lower() == 'y':
        turn = 'Player1'
    else:
        turn = 'Player2'

def place_marker(player,position):
    p[position] = pc[turn]
   

def change_player():
    global turn
    if turn == 'Player1':
        turn = 'Player2'
    else:
        turn = 'Player1'

def play_again():
    global game_on
    global turn
    global p
    
    answer_3 = input("Do you want to play again? yes or no ")
    if answer_3.lower() == 'yes' or answer_3.lower() == 'y':
        game_on = True
        for k,v in p.items():
            p[k] = ' '
    elif answer_3.lower() == 'no' or answer_3.lower() == 'n':
        game_on = False

player()
board()

while game_on:
    try:
        position = int(input(f"{turn} Choose a number 1-9? "))
        if p[position] != " ":
            print('please choose a open place on the board')
            continue
        elif p[position] == " ":
            place_marker(turn,position)
            board()
            win_check()
            change_player()
    except:
        print("An Error Occured I am exiting program")
        break