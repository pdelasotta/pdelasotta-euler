# -*- coding: utf-8 -*-
# time 45656.95 real     43165.66 user       235.95 sys
# over 12 hours!
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?
import sys
def main():
    movesDown = sys.argv[1]
    movesRight = sys.argv[2]
    paths = countPaths(int(movesDown), int(movesRight))
    print "Paths for", movesDown, "x",movesRight,"square is",paths


# gets the ammount of down and right moves remaining
# implicitly stating the grid's dimensions
def countPaths(downMoves, rightMoves):
    if(downMoves == 0 or rightMoves == 0):
        return 1
    else:
        pathsAfterDownMove = countPaths(downMoves-1, rightMoves)
        pathsAfterRightMove = countPaths(downMoves, rightMoves-1)
        return pathsAfterDownMove + pathsAfterRightMove


if __name__ == '__main__':
    main()
