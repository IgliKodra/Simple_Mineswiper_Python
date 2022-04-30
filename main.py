class tile:
    def __init__(self):
        self.symbol='◙'
        self.type=""
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

def main(W,H):
    # Krijon fushen e lojes dhe e mushe me objektet qe do jete tile-at e lojes
    field=[]
    for i in range(0, H):
        row=[]
        for j in range(0, W):
            row+=[tile()]
        field+=[list(row.copy())].copy()
   
    # Loop-i krysor i lojes
    alive=True
    while(alive):
        printBoard(W,H,field)
        cord=input("Input the cords: ")
        cord.split(',')
        field[int(cord[2])][int(cord[0])].symbol='+'

if __name__=="__main__":
    main(10,10)