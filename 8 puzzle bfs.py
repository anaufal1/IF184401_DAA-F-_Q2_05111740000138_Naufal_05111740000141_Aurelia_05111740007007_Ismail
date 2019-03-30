import string
import random
import sys

def is_solveable():
    count=0
    for x in range(8):
        if(list1[x+1] and list1[x] and list1[x] > list1[x+1]):
            count+=1
    if(count%2==0):
        return True
    else:
        print("The Puzzle is not soveable")
        sys.exit()        

game_on = True
move = 0
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
print("Insert Start State (e.g '1 2 3 4 5 6 7 8 0')")
list1 = [int(x) for x in input().split()]
is_solveable()
starting_state = list1.copy()

matrix=[]
while list1 !=[]:
    matrix.append(list1[:3])
    list1 = list1[3:]

def check(state):
    if (state == goal_state):
        print('you did it!\n')
        sys.exit()
    else:
        print("saya")

class Node:
	def __init__( self, state, parent, operator, depth, cost ):
		self.state = state
		self.parent = parent
		self.operator = operator
		self.depth = depth
		self.cost = cost

def display_board( state ):
	print ("-------------")
	print ("| %i | %i | %i |" % (state[0], state[1], state[2]))
	print ("-------------")
	print ("| %i | %i | %i |" % (state[3], state[4], state[5]))
	print ("-------------")
	print ("| %i | %i | %i |" % (state[6], state[7], state[8]))
	print ("-------------\n")

def move_up( state ):
    new_state = state[:]
    index = new_state.index( 0 )

    if index not in [0, 1, 2]:
        temp = new_state[index - 3]
        new_state[index - 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None

def move_down( state ):
    new_state = state[:]
    index = new_state.index( 0 )

    if index not in [6, 7, 8]:
        temp = new_state[index + 3]
        new_state[index + 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None

def move_left( state ):
    new_state = state[:]
    index = new_state.index( 0 )

    if index not in [0, 3, 6]:
        temp = new_state[index - 1]
        new_state[index - 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None

def move_right( state ):
    new_state = state[:]
    index = new_state.index( 0 )

    if index not in [2, 5, 8]:
        temp = new_state[index + 1]
        new_state[index + 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None

def create_node( state, parent, operator, depth, cost ):
	return Node( state, parent, operator, depth, cost )

def expand_node( node, nodes ):
	expanded_nodes = []
	expanded_nodes.append( create_node( move_up( node.state ), node, "up", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_down( node.state ), node, "down", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_left( node.state ), node, "left", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_right( node.state), node, "right", node.depth + 1, 0 ) )
	expanded_nodes = [node for node in expanded_nodes if node.state != None]
	return expanded_nodes

def bfs( start, goal ):
    nodes = []
    nodes.append( create_node( start, None, None, 0, 0 ) )
    
    while True:
        if len( nodes ) == 0: return None
        
        node = nodes.pop(0)
        stack = []

        if node.state == goal:
            moves = []
            temp = node
            while True:
                moves.insert(0, temp.operator)
                if temp.depth == 1: break
                temp = temp.parent
                stack.append(temp.state)
            i = len(stack) - 1
            while i != -1:
                display_board(stack[i])
                i -= 1
            return moves				

        nodes.extend( expand_node( node, nodes ) )

def nyerah():
    display_board(starting_state)
    result = bfs( starting_state, goal_state )
    display_board(goal_state)

    if result == None:
        print ("No solution found")
    elif result == [None]:
        print ("Start node was the goal!")
    else:
        print (result)
        print (len(result), " moves")

def zero(board):
    global empty_space
    for x in range (len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                empty_space = (x,y)
    return empty_space

def draw_board(board):
    if(board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]):
        print('you did it!\n')
        sys.exit()
    print('\n\t+-------+-------+-------|')
    for x in range (len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                print('\t|  0' , end='')
            else:
                 print('\t|  ' + '{:d}' .format(board[x][y]), end=' ') 
        print('\n\t+-------+-------+-------|')

def ask_number():
    global num , piece 
    num = input('\nplease type the number of the piece to move : (q) to give up and show the solver (bfs) : ')
    if num in ['q','Q']:
        print('\ngame over\n')
        nyerah()
        sys.exit()

    num = int(num)
    piece=()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if num == matrix[i][j]:
                piece = (i,j)
    return piece , num

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
            print('you have made ',move , 'moves so far ')
            print('\n')
        else:
            print('illegal move , try again ')
