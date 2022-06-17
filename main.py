#field[height value][width value]
from random import randint as ri
import os
import sys
class tile:
    def __init__(self):
        self.symbol='◙'
        self.Tvalue=0
        self.h=0
        self.w=0

    def explode(self):
        if (self.Tvalue==9):
            os.system('cls')
            print(f"BOOM")
            
def printBoard(gridsize,field):
    print("  ║",end="")
    for i in range(gridsize):
        print(i,end="")

    print("\n══╬",end="")
    for i in range(gridsize):
        print("═",end="")

    print()

    for i in range(gridsize):
        print(str(i)+" ║",end="")
        for j in range(gridsize):
            # print(field[i][j].symbol, end="")
            print(field[i][j].symbol, end="")
            # print(field[i][j], end="")
        print()

def openBlank(field,gridsize,i,j):
    for k in neighbor(field,gridsize,i,j):
        if (k.Tvalue==0 and k.symbol != " "):
            k.symbol=" "
            openBlank(field,gridsize,k.h,k.w)
        elif (0<k.Tvalue<9):
            k.symbol=str(k.Tvalue)
                        
def check(x,y,field,gridsize):
    if field[x][y].Tvalue==9:
        field[x][y].explode()
    elif (field[x][y].Tvalue==0):
        field[x][y].symbol=" "
        openBlank(field,gridsize,x,y)
    else:
        field[x][y].symbol=str(field[x][y].Tvalue)
        
    printBoard(10,field)

def neighbor(field,gridsize,h,w):
    neighbors=[]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            elif -1 < (h + i) < gridsize and -1 < (w + j) < gridsize:
                neighbors.append(field[h + i][w + j])
    return neighbors

def setTvalue(gridsize,field):
    for i in range (gridsize):
        for j in range (gridsize):
            if (field[i][j].Tvalue == 0):
                for k in neighbor(field,gridsize,i,j):
                    if (k.Tvalue==9):
                        field[i][j].Tvalue+=1

def main(gridsize,B):
    # Krijon fushen e lojes dhe e mbushe me objektet qe do jete tile-at e lojes
    field=[]
    for i in range(0, gridsize):
        row=[]
        for j in range(0, gridsize):
            row+=[tile()]
        field+=[list(row.copy())].copy()


    for i in range(B):
        # field[ri(0,gridsize-1)][ri(0,gridsize-1)].symbol='☺'
        field[ri(0,gridsize-1)][ri(0,gridsize-1)].Tvalue=9
    # Loop-i krysor i lojes
    alive=True
    setTvalue(gridsize,field)
    # for i in range(gridsize):
    #     for j in range(gridsize):
    #         field[i][j].h=i
    #         field[i][j].w=j
    #         field[i][j].symbol=str(field[i][j].Tvalue)
    printBoard(gridsize,field)
    while(alive):
        cord=input("Input the cords: ")
        if cord=='p':
            break
        cord.split(',')
        check(int(cord[2]),int(cord[0]),field,gridsize)

        # field[int(cord[2])][int(cord[0])].symbol='+'

if __name__=="__main__":
    # sys.setrecursionlimit(2000)
    # print(sys.getrecursionlimit())
    main(10,15)