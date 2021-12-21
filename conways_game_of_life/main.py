# Conway's Game of Life written by Andrew Combs
import numpy as np
import os

FAST_IO = [" ", "#"]
IO = [u"\u001b[30m\u001b[40m \u001b[0m", u"\u001b[37;1m\u001b[47;1m \u001b[0m"]\

# Optional Faster Version
IO = FAST_IO

# Main function
def iterate(buffer, w, h):

    tmp_buffer = np.empty(shape=(h+2, w+2))  # Creating a new empty buffer is significantly faster than copying the old one
    strb = u"\u001b[41m\u001b[37;1mConway's Game Of Life\u001b[0m"

    for x in range(1, h-1):
        strb += "\n"
        for y in range(1, w-1):
            alive = buffer[x, y]
            neighbors = np.sum(buffer[x-1:x+2, y-1:y+2])-int(alive) 
            tmp_buffer[x, y] = int(neighbors==3) + int((neighbors==2)*alive)
            strb += IO[int(tmp_buffer[x, y])]
            
    os.system('cls' if os.name == 'nt' else 'clear')  # This line makes escape codes work in the windows command line?? What??
    print(u"{}\u001b[0m".format(strb))
    
    return tmp_buffer

# Main code
def main():
    # 12x7 ratios give a bounding box, since characters are not perfectly square
    w, h = 120, 70
    buffer = np.zeros(shape=(h+2, w+2))
    buffer = np.random.randint(5, size=(h+2, w+2))
    buffer = np.where(buffer==0, 1, 0)

    # Setting outlines
    buffer[0, 0:w] = 0
    buffer[h, 0:w] = 0
    buffer[0:h, 0] = 0
    buffer[0:h, w] = 0

    
    cycles = int(input("Run for how many cycles? "))
    for _ in range(cycles):
        buffer = iterate(buffer, w, h)

if __name__ == "__main__":
    main()