"""
A program to solve soduku by Joseph Halstead

The solving algorithm works in two main parts:

Part 1: Loading the soduku board

1) Create an instance of the soduku board class.
2) Call the initialise function on the soduku board which fills its .board attribute
   with 81 instances of the Square class.
3) Load a board from a text file using the import_board_from_file function. The text file
   should be formatted as a 9x9 grid. See examples in the /tests folder.

Part 2: Depth First Search

1) Create a stack and push the inital soduku board onto it.
2) Enter a while loop
3) Load the next node soduku board to try by popping the stack.
4) If the soduku is solved - break the while loop and print the completed puzzle.
5) If the soduku is not solved attempt to fill in the remaining digits by iteratively
   eliminating the possibilities that each square can take (repeat_solve function).
6) If the soduku is valid after the possibility elimination i.e there are no logical
   contradictions then get the square with the lowest remaining possibilities and create
   child node soduku boards where these possibilities are guessed.
7) Push these child node soduku boards onto the stack.
8) Loop
   
"""

from board import soduku_board
from square import Square
from copy import deepcopy
from sys import argv

class Node:

    def __init__(self,board):
        self.board = board
   
   
#Main program begins here   

my_board = soduku_board()
my_board.initialise()


try:
    my_board.import_board_from_file(argv[1])
except:
    print ("Could not load a soduku board")
    quit()  

my_board.print_board()                                  
root_node = Node(my_board) #create a node that holds the initial soduku board
stack =[root_node] #add this initial root node to the stack

while True:

    if len(stack) ==0:
        print ("Could not solve this board")
        break

    new_node = stack.pop()
    x = new_node.board.is_solved()
    new_node.board.print_board()
    if x == True: #If soduku is solved print the board and break the while loop
        new_node.board.print_board()
        break           
    else:
    
        new_node.board.repeat_solve() #iteratively eliminate possible values from each square
        
        if new_node.board.is_valid() == True: #If this hasn't led to a logical contradiction
        
            #get the square with the lowest number of remaining possibiities 
    
            to_try = new_node.board.get_fewest_possibilities_square()
    
            for pos_num in to_try[1]:
                #create a copy of the soduku board and guess the values the to_try function
                #has returned.
                board = deepcopy(new_node.board)
        
                board.board[to_try[0]-1].solved_value = pos_num
                #Add these boards to the stack
                stack.append(Node(board))
        
        else:
        
            pass