#field[height value][width value]
from random import randint as ri
import os
class tile:
    def __init__(self):
        self.symbol='■'
        self.Tvalue=0
        self.h=0
        self.w=0
        self.isOpen=False

    def explode(self):
        if (self.Tvalue==9):
            os.system('cls')
            print(f"BOOM")
            
def printBoard(gridsize,field):
    print("  ║",end="")
    for i in range(gridsize):
        print(i,end=" ")

    print("\n══╬",end="")
    for i in range(gridsize):
        print("══",end="")

    print()

    for i in range(gridsize):
        print(str(i)+" ║",end="")
        for j in range(gridsize):
            if field[i][j].isOpen==True:
                if field[i][j].Tvalue==0:
                    print(" ", end=" ")
                else:
                    print(field[i][j].Tvalue, end=" ")
            else:
                # print(field[i][j].symbol, end=" ")
                print("■", end=" ")
        print()

def openT(field,gridsize,i,j):
    for k in neighbor(field,gridsize,i,j):
        if (k.Tvalue==0 and k.isOpen==False):
            k.isOpen=True
            openT(field,gridsize,k.h,k.w)
        elif (0<k.Tvalue and k.Tvalue<9 and k.isOpen==False):
            k.isOpen=True
                        
def check(cell,field,gridsize):
    if cell.Tvalue==9:
        cell.explode()
    elif (cell.Tvalue==0):
        cell.isOpen=True
        openT(field,gridsize,cell.h,cell.w)
    else:
        cell.isOpen=True
        openT(field,gridsize,cell.h,cell.w)

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
    for i in range(0, gridsize):
        for j in range(0, gridsize):
            field[i][j].h=i
            field[i][j].w=j


    for i in range(B):
        field[ri(0,gridsize-1)][ri(0,gridsize-1)].Tvalue=9
    # Loop-i krysor i lojes
    setTvalue(gridsize,field)
    printBoard(gridsize,field)
    while(True):
        os.system("cls")
        printBoard(gridsize,field)
        cord=input("Input the cords: ")
        if cord=='p':
            break
        cord.split(',')
        try:
            check(field[int(cord[2])][int(cord[0])],field,gridsize)
        except:
            print(f"Please input some correct coordinates")

if __name__=="__main__":
    main(10,10)