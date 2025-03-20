import numpy as np # we'll use numpy arrays as the basis for our grids. 

# Set up a random number generator from numpy.
RNG = np.random.default_rng()
NUM_STATES = 2


class Grid:
    # Note that the first index in a 2D array refers to the row (vertical) coordinate
    # while the second index refers to the column (horizontal) coordinate
    # That order is opposite our normal (x,y) coordinate system, so we need to remember
    # to use (y,x) when indexing into the data.
    gridSize: tuple[int, int] # rows, columns == y,x
    data: np.ndarray 
    generations: int 

    def __init__(self, size, setup):
        self.gridSize = gridSize
        self.data = data 
        self.size = size
        self.setup = randStart(size)
        # Remember to set object attributes self.gridSize and self.data.
        self.generations = 0

def randStart(size):
    return RNG.integers(0, NUM_STATES, size=size)
    # To get your random numbers, you must use the generator from numpy.random which 
    # is stored in the global variable RNG defined above.
    # See https://numpy.org/doc/stable/reference/random/index.html#random-quick-start   
    
    
RNG = np.random.default_rng()


def glideStart(size):
    arr = np.zeros(size)
    arr[2][0] = 1
    arr[0][1] = 1
    arr[2][1] = 1
    arr[1][2] = 1
    arr[2][2] = 1
    return arr

print(randStart([10,10])) 
print(glideStart([10,10])) 
print(RNG)