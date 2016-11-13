from square import Square
from copy import deepcopy


class soduku_board:

    """ A class for the soduku board. The actual board is represented by the self.board
     attribute. The self.board attribute is a list of 81 instances of the Square class
    """

    def __init__(self):
        self.board =[]
          
    def initialise(self):
    
        """This function creates 81 instances of the Square class and gives them their
            ID, row, column, and block attributes.
        """
    
        square_ID = 1
        
        for row in range(1,10):
            for column in range(1,10):
                
                self.board.append(Square(square_ID, column, row))
                
                square_ID = square_ID +1
                
        for created_square in self.board:
            created_square.assign_block()
            
        return
        
    def print_board(self):
    
        """
        Does what it says - prints board with some nice formatting.
        
        """
    
        rows =[[],[],[],[],[],[],[],[],[]]
        
        i =0
        
        for square in self.board:
        
            #This loop just organises the squares into rows for printing.
            
            rows[i].append(str(square.solved_value))
            
            if square.ID %9 == 0: # if there is a new row - increment i
                i=i+1
        
        print "+-----------+-----------+-----------+"
        
        for num,row in enumerate(rows):
        
            if num in [3,6]: # so we can put the --+-- on every 3rd row
            
                print "+-----------+-----------+-----------+"
                
            print "|",
        
            print " | ".join(row),
            
            print "|"
            
        print "+-----------+-----------+-----------+" 
                
    def import_board_from_file(self,filepath):
    
        """imports a board from a text file. For a successful import the file must be
            formatted as a 9x9 grid e.g: 400000805
                                         030000000
                                         000700000
                                         020000060
                                         000080400
                                         000010000
                                         000603070
                                         500200000
                                         104000000
            
            Unknown values can be represented by either a "0", "." or "x".
        
        """
        
        file = open(filepath, "r")
        
        char_counter =0
        
        for line in file:
            
            for char in line.strip():
                
                if char =="0" or char =="." or char =="x":
                
                    self.board[char_counter].solved_value = "."
                    
                elif char in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                
                    self.board[char_counter].solved_value = char
                    self.board[char_counter].possible_values =[char]
                    
                else:
                
                    print "An import error has occured"
                    return
                
                char_counter = char_counter +1
        return
                            
    def print_board_data(self):
    
        """de-bugging function for printing board data"""
    
        for square in self.board:
        
            print square.ID, square.row, square.column, square.block, square.possible_values
        
    def update_all_possibilities(self):
    
        """Goes through every square and calls the update_possibilities function"""
        
    
        if len(self.board) <> 81:
        
            print "Error -  board not initialised"
            
        else:
    
            for square in self.board:
            
                if square.solved_value == ".": #If the square is not solved

                    neighbours = set(square.get_all_neighbours(self.board)) 
                    
                    all_possibilities = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
                    
                    new_possibilities = list(all_possibilities-neighbours)
                    
                    if len(new_possibilities) < len(square.possible_values):
                    
                        square.possible_values = new_possibilities
                
                        if square.is_solved() == True:
                
                            square.update_solved_value()
                                 
    def is_valid(self):
    
        """Utility function that goes though every unit (row,column,block) and checks
         whether if there is there are any duplicate digits i.e the same digit appears
          twice in the same unit
        """
        
        rows =[[],[],[],[],[],[],[],[],[]]
        
        columns =[[],[],[],[],[],[],[],[],[]]
        
        blocks = [[],[],[],[],[],[],[],[],[]]
        
        for square in self.board: #loop assigns each square to its correct row.column and block
            
            rows[square.row-1].append(square.solved_value)
            columns[square.column-1].append(square.solved_value)
            blocks[square.block-1].append(square.solved_value)
        
        
        valid = True
        
        #Go through each row, column ad block and check if any digit appears more than once.
        #If it does set valid to False.
    
        for row in rows:
        
            if any(row.count(x) >1 and x <>"." for x in row) == True:
            
                valid = False
                
                
        for column in columns:
        
            if any(column.count(x) >1 and x <>"." for x in column) == True:
            
                valid = False
        
        for block in blocks:
        
            if any(block.count(x) >1 and x <>"." for x in block) == True:
            
                valid = False
                
        return valid
        
    def is_solved(self):
    
        """ checks all solved values are not "." and that the board is valid"""
    
        return (not any(square.solved_value == "." for square in self.board)) and self.is_valid()
                  
    def repeat_solve(self):
    
        """ 
        This function calls update_all_possibilities until no further assignments can 
        be made.
        
        """
        change = True

        while True:

            old_board = deepcopy(self.board)
  
            self.update_all_possibilities()
    
            change = False
    
            for square1, square2 in zip(self.board, old_board):
            
                #Loop through the new board and the old board
                #If the squares values are not equal then
                #set change to True
    
                if set(square1.possible_values) <> set(square2.possible_values):
        
                    change = True
            
            
            if change == False: #If the boards have not changed after calling update_all_possibilities 
                break           #then break

        return
        
    def get_fewest_possibilities_square(self):
    
        """ Function to find square with the fewest remaining possibilities
            It returns a list containing the square.ID and the squares's possible_values list
            
            This function is called in the depth first search solver in the solver.py file.
            
            Trying the square with the least remaining possibilities helps optimise the algorithm. 
            
        """
        
        least =[False,["1", "2", "3", "4", "5", "6", "7", "8", "9"]]
        
        for square in self.board:
        
            #for each square if the length of its possible_values list is less than the 
            #previously found length then re-assign .
            
            if len(square.possible_values) < len(least[1])  and square.solved_value == ".":
            
                least = [square.ID, square.possible_values]
          
          
        return least
        
        
        
        
        
        
        
        
        
        