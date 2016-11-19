class Square:
            
    """A class for each square that exists in the soduku board"""

    def __init__(self, ID, column, row):
        self.ID = ID   #ID for square from 1-81
        self.solved_value = "."  
        self.possible_values =["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.column = column
        self.row = row
        self.block = False 
        
    def is_solved(self):
        """returns True if square is solved , False if not."""
        if len(self.possible_values) ==1 or self.solved_value != ".":
            return True
        else:
            return False
            
    def update_solved_value(self):
        """If square is now solved this function collects the solved value from length 1
            possible values list and places it in the solved value attribute."""       
        self.solved_value = self.possible_values[0]
        return
    
    def assign_block(self):
        """assigns the square to one of the 9 3x3 blocks on a soduku board"""
    
    
        if self.ID in [1,2,3,10,11,12,19,20,21]:
            self.block = 1
        elif self.ID in [4,5,6,13,14,15,22,23,24]:
            self.block =2
        elif self.ID in [7,8,9,16,17,18,25,26,27]:
            self.block =3
        elif self.ID in [28,29,30,37,38,39,46,47,48]:
            self.block =4
        elif self.ID in [31,32,33,40,41,42,49,50,51]:
            self.block =5
        elif self.ID in [34,35,36,43,44,45,52,53,54]:
            self.block = 6
        elif self.ID in [55,56,57,64,65,66,73,74,75]:
            self.block=7
        elif self.ID in [58,59,60,67,68,69,76,77,78]:
            self.block =8
        elif self.ID in [61,62,63,70,71,72,79,80,81]:
            self.block =9
        else:
            print ("A block assignment error has occured")
            
    def get_row_neighbours(self, board):
        """for a given square on a given board returns all squares that are solved
         in that same row"""
        
        row_neighbours =[]
        
        for square in board:
        
            if self.row == square.row and square.is_solved() == True:
        
                row_neighbours.append(square.solved_value)

            else:
            
                pass
                
        return row_neighbours
                  
    def get_column_neighbours(self, board):
    
        """for a given square on a given board returns all squares that are solved
         in that same column"""
    
        column_neighbours =[]
            
        for square in board:
    
            if self.column == square.column and square.is_solved() == True:
    
                column_neighbours.append(square.solved_value)

            else:
        
                pass
                
        return column_neighbours
      
    def get_block_neighbours(self, board):
    
        """for a given square on a given board returns all squares that are solved
         in that same block"""

        block_neighbours =[]
        
        for square in board:
    
            if self.block == square.block and square.is_solved() == True:
    
                block_neighbours.append(square.solved_value)

            else:
        
                pass
            
        return block_neighbours
            
    def get_all_neighbours(self, board):
    
        """calls the get row/column/block functions and returns concatenated list of all 3"""
    
        row_neighbours = self.get_row_neighbours(board)
        column_neighbours = self.get_column_neighbours(board)
        block_neighbours = self.get_block_neighbours(board)
        
        return list(set(row_neighbours + column_neighbours + block_neighbours)) #set() to remove duplicates
            
    def update_possibilities(self, neighbours):
    
        """This function has two parts:
        
        1 - Subtracts the set of all possible 1-9 digits from the set of the square's neighbours.
            This leaves behind the set of digits that the square could possibly take e.g - 
            (1,2,3,4,5,6,7,8,9) - (1,2) leaves (3,4,5,6,7,8,9).
        2- Simbly updates the squares possible_values attribute to a list of the possibilities.
        
        """
    
        all_possibilities = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        
        neighbours = set(neighbours)
        
        self.possible_values = list(all_possibilities-neighbours)
    
    
    
    
    
    
    
    
    
       