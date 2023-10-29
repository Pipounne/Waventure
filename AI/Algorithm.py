class character:
    def __init__(self,name,ID,ally,PV,atk,PM,position) -> None:
        self.name = name
        self.ID = ID
        self.ally = ally
        self.PV = PV
        self.atk = atk
        self.PM = PM
        self.position = position
        pass


exemple = [['/' for j in range (7)] for i in range(7)]

exemple[0][0] = character("Arti Ficelle","0",True,391,35,3,(0,0))
exemple[5][4] = character("Tofu 1","1",False,120,30,3,(5,4))
exemple[4][5] = character("Tofu 2","2",False,110,32,3,(4,5))

exemple2 = [['/' for j in range (7)] for i in range(7)]

exemple2[0][1] = character("Arti Ficelle","0",True,391,35,3,(0,1))
exemple2[6][5] = character("Tofu 1","1",False,120,30,3,(6,5))
exemple2[4][6] = character("Tofu 2","2",False,110,32,3,(4,6))

def print_board(board):
    for i in range(7):
        for j in range(7):
            try:
                board[i][j].ally
            except AttributeError:
                print(board[i][j],end = "")
            else:
                if(board[i][j].ally):
                    print("\033[92m" + board[i][j].ID + "\033[0m",end = "")
                else:
                    print("\033[91m" + board[i][j].ID + "\033[0m",end = "")
        print("")


def remplissage(character) :
    characters = character[7][7]
    for i in range(7):
        for j in range(7):
            characters[i][j] = character[i*j]

def IsCellFree(wanted_cell,board):
    available = True
    if(board[wanted_cell[0]][wanted_cell[1]] != '/' and board[wanted_cell[0]][wanted_cell[1]].ID != "0" ):
        available = False
    return available

def TheoricalMovment(starting_pos,board,mouvment,n = 4):
    if (n != 0) :
        if(-1<starting_pos[0]<7 and -1<starting_pos[1]<7):
            if(IsCellFree(starting_pos,board)):
                mouvment[starting_pos[0]][starting_pos[1]] = 1
                TheoricalMovment((starting_pos[0]+1,starting_pos[1]),board,mouvment,n-1)
                TheoricalMovment((starting_pos[0]-1,starting_pos[1]),board,mouvment,n-1)
                TheoricalMovment((starting_pos[0],starting_pos[1]+1),board,mouvment,n-1)
                TheoricalMovment((starting_pos[0],starting_pos[1]-1),board,mouvment,n-1)
            else:
                mouvment[starting_pos[0]][starting_pos[1]] = 2


mouvment = [[0 for j in range (7)] for i in range(7)]    

TheoricalMovment((0,0),exemple,mouvment)

for i in range(7):
        for j in range(7):
            print(mouvment[i][j],end = "")
        print("")
