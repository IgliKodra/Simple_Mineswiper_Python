from random import randint as ri
import os
class tile:
    def __init__(self):
        self.symbol='◙'
        self.type="safe"
        self.value=0

def printBoard(W,H,field):
    print("  ║",end="")
    for i in range(W):
        print(i,end="")

    print("\n══╬",end="")
    for i in range(W):
        print("═",end="")

    print()

    for i in range(H):
        print(str(i)+" ║",end="")
        for j in range(W):
            print(field[i][j].symbol, end="")
            # print(field[i][j], end="")

        print()

def explode():
    os.system('cls')
    print(f"BOOM")

def check(x,y,field):
    if field[x][y].type=="bomb":
        explode()
    field[x][y].symbol='+'
    printBoard(10,10,field)

def main(W,H,B):
    # Krijon fushen e lojes dhe e mushe me objektet qe do jete tile-at e lojes
    field=[]
    for i in range(0, H):
        row=[]
        for j in range(0, W):
            row+=[tile()]
        field+=[list(row.copy())].copy()

    for i in range(B):
        field[ri(0,H-1)][ri(0,W-1)].type="bomb"
        field[ri(0,H-1)][ri(0,W-1)].symbol='☺'
   
    # Loop-i krysor i lojes
    alive=True
    printBoard(W,H,field)
    while(alive):
        cord=input("Input the cords: ")
        if cord=='p':
            break
        cord.split(',')
        check(int(cord[2]),int(cord[0]),field)
        # field[int(cord[2])][int(cord[0])].symbol='+'

if __name__=="__main__":
    main(10,10,10)