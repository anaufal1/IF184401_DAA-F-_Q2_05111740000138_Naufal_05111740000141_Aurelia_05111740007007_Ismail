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
matrix=[]
while list1 !=[]:
    matrix.append(list1[:3])
    list1 = list1[3:]
#----------------------------------------------------

class Node:
	def __init__( self, state, parent, operator, depth, cost ):
		# Contains the state of the node
		self.state = state
		# Contains the node that generated this node
		self.parent = parent
		# Contains the operation that generated this node from the parent
		self.operator = operator
		# Contains the depth of this node (parent.depth +1)
		self.depth = depth
		# Contains the path cost of this node from depth 0. Not used for depth/breadth first.
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
	# """Moves the blank tile up on the board. Returns a new state as a list."""
	# Perform an object copy
    new_state = state[:]
    index = new_state.index( 0 )
    # Sanity check
    if index not in [0, 1, 2]:
        # Swap the values.
        temp = new_state[index - 3]
        new_state[index - 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        # Can't move, return None (Pythons NULL)
        return None

def move_down( state ):
	# """Moves the blank tile down on the board. Returns a new state as a list."""
    # Perform object copy
    new_state = state[:]
    index = new_state.index( 0 )
    # Sanity check
    if index not in [6, 7, 8]:
        # Swap the values.
        temp = new_state[index + 3]
        new_state[index + 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        # Can't move, return None.
        return None

def move_left( state ):
	# """Moves the blank tile left on the board. Returns a new state as a list."""
    new_state = state[:]
    index = new_state.index( 0 )
    # Sanity check
    if index not in [0, 3, 6]:
        # Swap the values.
        temp = new_state[index - 1]
        new_state[index - 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        # Can't move it, return None
        return None

def move_right( state ):
	# """Moves the blank tile right on the board. Returns a new state as a list."""
	# Performs an object copy. Python passes by reference.
    new_state = state[:]
    index = new_state.index( 0 )
    # Sanity check
    if index not in [2, 5, 8]:
        # Swap the values.
        temp = new_state[index + 1]
        new_state[index + 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        # Can't move, return None
        return None

def create_node( state, parent, operator, depth, cost ):
	return Node( state, parent, operator, depth, cost )

def expand_node( node, nodes ):
	# """Returns a list of expanded nodes"""
	expanded_nodes = []
	expanded_nodes.append( create_node( move_up( node.state ), node, "up", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_down( node.state ), node, "down", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_left( node.state ), node, "left", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_right( node.state), node, "right", node.depth + 1, 0 ) )
	# Filter the list and remove the nodes that are impossible (move function returned None)
	expanded_nodes = [node for node in expanded_nodes if node.state != None] #list comprehension!
	return expanded_nodes

def bfs( start, goal ):
	# """Performs a breadth first search from the start state to the goal"""
	# A list (can act as a queue) for the nodes.
    nodes = []
	# Create the queue with the root node in it.
    nodes.append( create_node( start, None, None, 0, 0 ) )
    while True:
        # We've run out of states, no solution.
        if len( nodes ) == 0: return None
        # take the node from the front of the queue
        node = nodes.pop(0)
        # Append the move we made to moves
        # if this node is the goal, return the moves it took to get here.
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
        # Expand the node and add all the expansions to the front of the stack
        nodes.extend( expand_node( node, nodes ) )

# Main method
def nyerah():
	# starting_state = [1, 8, 2, 0, 4, 3, 7, 6, 5]
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
        nyerah()
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
            print('you have made ',move , 'moves so far ')
            print('\n')
        else:
            print('illegal move , try again ')



