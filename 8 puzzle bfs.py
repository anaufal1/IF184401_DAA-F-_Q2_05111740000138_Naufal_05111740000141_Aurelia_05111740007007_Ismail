import string
import random
import sys
   
#------------------ to get input -------------------
game_on = True
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
print("Insert Start State (e.g '1 2 3 4 5 6 7 8 0')")
list1 = [int(x) for x in input().split()]
move = 0
starting_state = list1.copy()
#------------------ to make list of lists -----------
matrix=[]
while list1 !=[]:
    matrix.append(list1[:3])
    list1 = list1[3:]
#------------------- function to find where the zero is ------
def zero(board):
    global empty_space
    for x in range (len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                empty_space = (x,y)
    return empty_space
#----------------------- function to draw the board -----------
def draw_board(board):
    print('\n\t+-------+-------+-------|')
    for x in range (len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                print('\t|  0' , end='')
            else:
                 print('\t|  ' + '{:d}' .format(board[x][y]), end=' ') 
        print('\n\t+-------+-------+-------|')
# ------------------------ function to ask for the number to move ---------- 
def ask_number():
    global num , piece 
    num = input('\nplease type the number of the piece to move : (q) to give up and show the solver (bfs) : ')
    if num in ['q','Q']:
        print('\ngame over\n')
        sys.exit()

    num = int(num)
    piece=()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if num == matrix[i][j]:
                piece = (i,j)
    return piece , num
#---------------------------------------------- game starts here -------------
zero(matrix)
while game_on:
    draw_board(matrix)      
    ask_number()         
    if num > 8:
        print('illegal move , try again  ')
    else:
        if(empty_space==(piece[0]-1,piece[1]))\
           or(empty_space==(piece[0]+1,piece[1]))\
           or(empty_space==(piece[0],piece[1]-1))\
           or(empty_space==(piece[0],piece[1]+1)):
            matrix[empty_space[0]][empty_space[1]]=num
            matrix[piece[0]][piece[1]]=0
            empty_space=(piece[0],piece[1])
            move = move +1
            print()
            print('you have made ',move , 'moves so far ')
            print('\n')
        else:
            print('illegal move , try again ')
