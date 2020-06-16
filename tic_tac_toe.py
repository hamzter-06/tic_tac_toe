import os

print("Welcome to Tic Tac Toe!!")
# Declare global parameters for player choices
# Gameboard
p ={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
pc = {'Player1':" ","Player2":" "}
game_on = False

def board():
    os.system('cls')
    print(p[7] + ' | ' +  p[8] + ' | ' + p[9])
    print('---------')
    print(p[4] + ' | ' + p[5] + ' | ' + p[6])
    print('---------')
    print(p[1] + ' | ' + p[2] + ' | ' + p[3])

def win_combos():
    pass

def play_assignments():
# Creating Dictionary for Player X and O assignments
    p1_ans = input('Player1 do you want to be X? yes or no:  ')
    if p1_ans.lower() == 'yes':
        play_assign['Player1'] = 'X'
        play_assign['Player2'] = 'O'
    else:
        play_assign['Player1'] = 'O'
        play_assign['Player2'] = 'X'
        print(play_assign)

board()
while game_on:
    try:
        result = int(input("Player 1 Choose a number 1-9? "))
        if p[result] != " ":
            print('play_again')
            continue
        elif p[result] == " ":
            p[result] = 'X'
            board()
        #else:
        #    game_on = False
        #    break
    except:
        break
    #if result == 1 and p[1] == " ":
    #    p[1] = 'X'
    #    board()
    #else:
    #    game_on = False1
