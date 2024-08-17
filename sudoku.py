from enum import Enum
from math import sqrt
import time
 
# puzzle for testing

# puzzle =     [[1,0,0,6,0,0,0,9,0],
#               [0,0,0,0,0,1,0,8,0],
#               [4,0,3,2,0,7,6,1,5],
#               [0,7,0,0,0,8,1,0,3],
#               [3,0,0,7,0,2,0,0,6],
#               [6,0,1,9,0,0,0,7,0],
#               [8,6,5,3,0,9,4,0,1],
#               [0,1,0,8,0,0,0,0,0],
#               [0,3,0,0,0,4,0,0,9]]


# puzzle = [[5,3,0,0,7,0,0,0,0],
#           [6,0,0,1,9,5,0,0,0],
#           [0,9,8,0,0,0,0,6,0],
#           [8,0,0,0,6,0,0,0,3],
#           [4,0,0,8,0,3,0,0,1],
#           [7,0,0,0,2,0,0,0,6],
#           [0,6,0,0,0,0,2,8,0],
#           [0,0,0,4,1,9,0,0,5],
#           [0,0,0,0,8,0,0,7,9]]

# puzzle = [[4,3,5,2,6,0,7,8,1],
#           [6,8,2,5,7,1,4,9,3],
#           [1,9,7,8,3,4,5,6,2],
#           [8,2,6,1,9,0,3,4,7],
#           [3,7,4,6,8,2,9,1,5],
#           [9,5,1,7,4,3,6,2,8],
#           [5,1,9,3,2,6,8,7,4],
#           [2,4,8,9,5,7,1,3,6],
#           [7,6,3,4,1,8,2,5,9]]

puzzle = [[0,6,2,0,0,0,0,5,7],
          [0,0,0,0,0,0,0,0,4],
          [3,0,0,6,0,2,8,0,0],
          [0,0,0,0,6,4,0,0,0],
          [0,5,0,9,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,3,0,0,0,0,0],
          [8,1,0,0,0,0,0,0,6],
          [0,4,9,7,5,0,0,0,0]]

# contains representation of Sudoku puzzle
# 
class Puzzleboard:

    def __init__(self, size=9):
        # set all squares to zero & maybe
        self.size = size
        self.boxsize = int(sqrt(size))
        self.puzzle = dict()
        self.zeros = set()
        self.allnums = set(range(10))

    def __str__(self):
        line = '-' * (4 * self.size + 5) + '\n'
        rstr = ''
        for row in range(self.size):
            if row % self.boxsize == 0:
                rstr = rstr + line
            for col in range(self.size):
                if col % self.boxsize == 0:
                    rstr = rstr + '|'
                rstr = rstr + '| ' + str(self.puzzle[(row, col)]) + ' '
            rstr = rstr + '||\n'
        rstr = rstr + line
        return rstr
    
    # return list of whole puzzleboard
    def makelist(self):
        return [[self.puzzle[(r, c)] for c in range(self.size)] for r in range(self.size)]
        
    def putentry(self, loc, num):
        #print('called putentry loc:', loc, ' num ', num)
        #print('at putentry setzeros lengh:', len(self.zeros))
        self.puzzle[loc] = num
        if num == 0:
            self.zeros.add(loc)
            #print('adding zero ', loc)
        else:
            self.zeros.discard(loc)
            #print('discarding zero ', loc)
        

    def listentry(self, list):
        for r in range(self.size):
            for c in range(self.size):
                self.putentry((r, c), list[r][c])
    
    def getbox(self, loc):
        rowstart = self.boxsize * (loc[0] // self.boxsize)
        colstart = self.boxsize * (loc[1] // self.boxsize)
        return_set = set()
        for r in range(rowstart, rowstart + self.boxsize):
            for c in range(colstart, colstart + self.boxsize):
                return_set.add(self.puzzle[(r, c)])
        return return_set

    def getrow(self, row):
        return {self.puzzle[(row, c)] for c in range(self.size)}
    
    def getcol(self, col):
        return {self.puzzle[(r, col)] for r in range(self.size)}
    
    def get_possibles(self, loc):
        return self.allnums - (self.getbox((loc[0], loc[1])) | self.getrow(loc[0]) | self.getcol(loc[1]))

    def findzero1(self):
        if len(self.zeros) > 0:
            zitem = min(self.zeros)
            return zitem
        else:
            return (self.size, self.size)
            
    
    def solve(self):
        testloc = self.findzero1()
        #print("entering solve, testloc: ", testloc)
        #print("zerolist: ", self.zeros)
        # if no more zeros we're done
        if testloc[0] == self.size:
            return True
        # try each testnum in possibles
        list_of_possibles = self.get_possibles(testloc)
        for testnum in list_of_possibles:
            self.putentry(testloc, testnum)
            # print('filled ', testloc, ' with ', testnum)            
            # now try to solve rest of puzzle with that element filled in
            result = self.solve()
            if result:
                # if we solved it, return True
                return True
            else:
                # if not, return element to 0
                self.putentry(testloc, 0)
        # if we reached here, no number in possibles works
        return False

def sudoku(puzzle):
    # create board
    P = Puzzleboard(9)
    P.listentry(puzzle)
    result = P.solve()
    if not result:
        print("unable to solve")
    else:
        print(P)
    return P.makelist()

if __name__ == '__main__':
    start = time.time()
    sudoku(puzzle)
    end = time.time()
    print("Time: ", end-start)