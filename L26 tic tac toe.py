# tic tac toe

'''
    We will make board using dictionary
    in which keys will be the loction(i.e : top-left, mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choies of move  
'''

TheBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in TheBoard:
    board_keys.append(key)

'''
    we will have to print the updated borad after every move in the gam and thus we wll make function
    in which   we'll define the printBoard function so that we can easily print the board everytime by 
    calling this function.
'''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(TheBoard)
        print("It' your turn,"+ turn + ".move to which place?")

        move = input()

        if TheBoard[move] == ' ':
            TheBoard[move] = turn 
            count += 1
        else:
            print("that place is already filled. \nMove to which place?")
            continue

        #now we will check if player x or o has won for every move sfter 5 move
        if count >= 5:
            if TheBoard['7'] == TheBoard['8'] == TheBoard['9'] != ' ': #across the top
                printBoard(TheBoard)
                print("\n Gameover .\n")
                print(" **** " + turn + " won. ****")
                break
            elif TheBoard['4'] == TheBoard['5'] == TheBoard['6'] != ' ': #across the middle
                printBoard(TheBoard)
                print("\n Gameover .\n")
                print(" **** " + turn + " won. ****")
                break
            elif TheBoard['1'] == TheBoard['2'] == TheBoard['3'] != ' ': #across the 
                printBoard(TheBoard)
                print("\n Gameover .\n")
                print(" **** " + turn + " won. ****")
                break
            elif TheBoard['1'] == TheBoard['4'] == TheBoard['7'] != ' ': #across the top
                printBoard(TheBoard)
                print("\n Gameover .\n")
                print(" **** " + turn + " won. ****")
                break
            elif TheBoard['2'] == TheBoard['5'] == TheBoard['8'] != ' ': #across the top
                printBoard(TheBoard)
                print("\n Gameover .\n")
                print(" **** " + turn + " won. ****")
                break
            elif TheBoard['3'] == TheBoard['6'] == TheBoard['9'] != ' ': #across the top
                printBoard(TheBoard)
                print("\n Gameover .\n")
                print(" **** " + turn + " won. ****")
                break
            elif TheBoard['7'] == TheBoard['5'] == TheBoard['3'] != ' ': #across the top
                printBoard(TheBoard)
                print("\n Gameover .\n")
                print(" **** " + turn + " won. ****")
                break
            elif TheBoard['1'] == TheBoard['5'] == TheBoard['9'] != ' ': #across the top
                printBoard(TheBoard)
                print("\n Gameover .\n")
                print(" **** " + turn + " won. ****")
                break
          
        #if neither X nor o win and the board is full we'll declare the result as tie
        if count == 9:
            print("\nGame over")
            print("it a tie")

        #now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("do you want to play again?(y/n)")
    if restart == "y" or restart =="Y":
        for key in board_keys:
            TheBoard[key] = " "

        game()

if __name__=="__main__":
    game()