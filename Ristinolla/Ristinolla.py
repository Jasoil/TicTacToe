from array import *
from multiprocessing.sharedctypes import Value

#interface

#print("Tervetuloa")
token = input("Valitse symboli x tai 0: ")
#uinput = input("Syötä numero, jonka paikalle haluat sijoittaa symbolin: ")
#board
numbers = [1,2,3,4,5,6,7,8,9]
board = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
columns = 3


def printboard():
    for r in board:
        print(end="\n")
        print("_____")
        for c in r:
            print(c,end = " ")
    print()
    
#change board
board[0][0] = token


printboard()