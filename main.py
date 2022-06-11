#field[height value][width value]
from random import randint as ri
import os
class tile:
    def __init__(self):
        self.symbol='◙'
        self.type="safe"
        self.value=0

    def explode(self):
        if (self.type=="bomb"):
            os.system('cls')
            print(f"BOOM")

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
            # print(field[i][j].symbol, end="")
            print(field[i][j].value, end="")
            # print(field[i][j], end="")

        print()

def check(x,y,field):
    if field[x][y].type=="bomb":
        field[x][y].explode()
    field[x][y].symbol='+'
    printBoard(10,10,field)

def setValue(W,H,field):
    for i in range (H):
        for j in range (W):
            if (field[i][j].type == "safe"):
                # field[i][j].value+=8
                if (i+1<H and j+1<W):
                    if (field[i+1][j+1].type=="bomb"):
                        field[i][j].value+=1
                if(j+1<W):
                    if (field[i][j+1].type=="bomb"):
                        field[i][j].value+=1
                if(i-1>=0 and j+1<W):
                    if (field[i-1][j+1].type=="bomb"):
                        field[i][j].value+=1
                if(i+1<H):
                    if (field[i+1][j].type=="bomb"):
                        field[i][j].value+=1
                if(i-1>=0):
                    if (field[i-1][j].type=="bomb"):
                        field[i][j].value+=1
                if(i+1<H and j-1>=0):
                    if (field[i+1][j-1].type=="bomb"):
                        field[i][j].value+=1
                if(j-1>=0):
                    if (field[i][j-1].type=="bomb"):
                        field[i][j].value+=1
                if(i+1<H and j-1>=0):
                    if (field[i+1][j-1].type=="bomb"):
                        field[i][j].value+=1

def main(W,H,B):
    # Krijon fushen e lojes dhe e mbushe me objektet qe do jete tile-at e lojes
    field=[]
    for i in range(0, H):
        row=[]
        for j in range(0, W):
            row+=[tile()]
        field+=[list(row.copy())].copy()

    for i in range(B):
        field[ri(0,H-1)][ri(0,W-1)].type="bomb"
        field[ri(0,H-1)][ri(0,W-1)].symbol='☺'
        field[ri(0,H-1)][ri(0,W-1)].value=9
   
    # Loop-i krysor i lojes
    alive=True
    setValue(W,H,field)
    # field[0][0].type="bomb"
    # if (field[0][0].type=="bomb"):
    #     field[5][5].value+=1
    printBoard(W,H,field)
    while(alive):
        cord=input("Input the cords: ")
        if cord=='p':
            break
        cord.split(',')
        check(int(cord[2]),int(cord[0]),field)

        # field[int(cord[2])][int(cord[0])].symbol='+'

if __name__=="__main__":
    main(5,5,15)