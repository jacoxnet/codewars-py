GRIDSIZE = 4
SOURCE_LOC = 1
SOURCE_SIZE = float(6)
OBSTACLES = set([(0, 1), (1,2), (2,1)])
BUCKETS = {0, 1, 2, 3}
# GRID dict with index tuple and contents of cell
#   'B' - bucket
#   int - water quantity
#   'O' - obstacle

class Grid:
    def __init__(self, GRIDSIZE, SOURCE_LOC, OBSTACLES, BUCKETS):
        self.size = GRIDSIZE



def setup_grid():
    for row in range(0, GRIDSIZE):
        for col in range(0, GRIDSIZE):
            if (row, col) in OBSTACLES:
                GRID[(row, col)] = 'O'
            else:
                GRID[(row, col)] = float(0)
    GRID[(SOURCE_LOC, GRIDSIZE-1)] = SOURCE_SIZE

def move_water(tick):
    for row in range(1, GRIDSIZE):
            for col in range(1, GRIDSIZE):
                contents = GRID[(row, col)]
                if isinstance(contents, float) and contents > 0:
                    GRID[(row, col)] = 0
                    if GRID[(row, col-1)] != 'O':
                        GRID[(row, col-1)] = contents
                    else:






if __name__ == '__main__':
    setup_grid()
    tick = 1
    while move_water(tick):
        tick += 1
    print(GRID)
