from enum import Enum
from math import sqrt

class Puzzleboard:

    def __init__(self, puzzle_list, size=9):
        # set all squares to zero & maybe
        self.size = size
        self.boxsize = int(sqrt(size))
        self.puzzle = {}
        self.first_zero = (-1, -1)
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
            if self.first_zero == (-1, -1):
                self.first_zero = (row, col)
            else:
                if row <= self.first_zero[0] and col < self.first_zero[1]:
                    self.first_zero = (row, col)
    
    def listentry(self, list):
        for r in range(self.size):
            for c in range(self.size):
                self.putentry(r, c, list[r][c])
    
    def getentry(self, row, col):
        return self.puzzle[(row, col)]

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
            try:
                col = [self.puzzle[(r, col)] for col in range(self.size)].index(0)
                return (r, col)
            except ValueError:
                pass
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
    return P.makelist()

