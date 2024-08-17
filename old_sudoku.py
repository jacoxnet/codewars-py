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
          [3,0,0,6,0,2,8,0,1],
          [0,0,0,0,6,4,0,0,0],
          [0,5,0,9,0,0,0,0,0],
          [0,0,0,0,0,0,2,0,0],
          [0,0,0,3,0,0,0,0,0],
          [8,1,0,0,0,0,0,0,6],
          [0,4,9,7,5,0,0,0,0]]

class Puzzleboard:

    def __init__(self, size=9):
        # set all squares to zero & maybe
        self.size = size
        self.boxsize = int(sqrt(size))
        self.puzzle = {}
        self.first_zero = (0, 0)
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
        
    def putentry(self, row, col, num):
        self.puzzle[(row, col)] = num
        if num == 0:
            if row <= self.first_zero[0] and col < self.first_zero[1]:
                self.first_zero = (row, col)
    
    def listentry(self, list):
        for r in range(self.size):
            for c in range(self.size):
                self.putentry(r, c, list[r][c])


    def getbox(self, row, col):
        rowstart = self.boxsize * (row // self.boxsize)
        colstart = self.boxsize * (col//self.boxsize)
        return_set = set()
        for r in range(rowstart, rowstart + self.boxsize):
            for c in range(colstart, colstart + self.boxsize):
                return_set.add(self.puzzle[(r, c)])
        return return_set

    def getrow(self, row):
        return {self.puzzle[(row, c)] for c in range(self.size)}
    
    def getcol(self, col):
        return {self.puzzle[(r, col)] for r in range(self.size)}
    
    def get_possibles(self, row, col):
        return self.allnums - (self.getbox(row, col) | self.getrow(row) | self.getcol(col))


    def findzero1(self):
        if self.puzzle[self.first_zero] == 0:
            return self.first_zero
        for r in range(self.first_zero[0], self.size):
            c_start = self.first_zero[1] if r == self.first_zero[0] else 0
            for c in range(c_start, self.size):
                if self.puzzle[(r, c)] == 0:
                    return (r, c)
        return (self.size, self.size)
    
    def solve(self):
        # print('trying to solve\n', self)
        testloc = self.findzero1()
        # print('found zero at ', testloc)
        # if no more zeros we're done
        if testloc[0] == self.size:
            return True
        # try each testnum in possibles
        for testnum in self.get_possibles(testloc[0], testloc[1]):
            self.putentry(testloc[0], testloc[1], testnum)
            # print('filled ', testloc, ' with ', testnum)            
            # now try to solve rest of puzzle with that element filled in
            result = self.solve()
            if result:
                # if we solved it, return True
                return True
            else:
                # if not, return element to 0
                self.putentry(testloc[0], testloc[1], 0)
        # if we reached here, no number in possibles works
        return False


def solve(board):
    # create board
    P = Puzzleboard(9)
    P.listentry(board)
    P.solve()
    print(P)
    return P.makelist()

if __name__ == '__main__':
    start = time.time()
    solve(puzzle)
    end = time.time()
    print("Time: ", end-start)