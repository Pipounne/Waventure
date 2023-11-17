from numpy import * as np 

#We create a character class to gather all the data extracted from the game
class character:
    def __init__(self,name,ID,ally,PV,atk,PM,position) -> None:
        self.name = name            #The name of the cbaracter
        self.ID = ID                #An ID to easily distinguish all characters
        self.ally = ally            #A boolean to divide character into allies and enemies
        self.PV = PV                #The health points of the character
        self.atk = atk              #The attack value of the character
        self.PM = PM                #The movement point of the character
        self.position = position    #The position of the character on the board as a tuple (x,y)
        pass


exemple = [['/' for j in range (7)] for i in range(7)]

exemple[0][0] = character("Arti Ficelle","0",True,391,35,3,(0,0))
exemple[5][4] = character("Tofu 1","1",False,120,30,3,(5,4))
exemple[4][5] = character("Tofu 2","2",False,110,32,3,(4,5))

exemple2 = [['/' for j in range (7)] for i in range(7)]

exemple2[0][1] = character("Arti Ficelle","0",True,391,35,3,(0,1))
exemple2[6][5] = character("Tofu 1","1",False,120,30,3,(6,5))
exemple2[4][6] = character("Tofu 2","2",False,110,32,3,(4,6))

#For debug purpose
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

#???
def remplissage(character) :
    characters = character[7][7]
    for i in range(7):
        for j in range(7):
            characters[i][j] = character[i*j]

#This function test if a chosen cell is free to move on
def IsCellFree(wanted_cell,board):
    available = True
    if(board[wanted_cell[0]][wanted_cell[1]] != '/' and board[wanted_cell[0]][wanted_cell[1]].ID != "0" ):
        available = False
    return available

#A function to calcul all available deplacements
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

#A function to know how many foes are in the melee kayword
def melee_count(board):
    for i in range(7):
        for j in range(7):
            try:
                board[i][j].ally
            except AttributeError:
                pass
            else:
                if(board[i][j].ID=="0"):
                    cpt = 0
                    for k in range (3):
                        for l in range (3):
                            try:
                                board[i+k-1][j+l-1].ally
                            except AttributeError:
                                pass
                            else:
                                if board[i+k-1][j+l-1].ally == False:
                                    cpt+=1
                    return cpt


mouvment = [[0 for j in range (7)] for i in range(7)]    

TheoricalMovment((4,4),exemple,mouvment)

for i in range(7):
        for j in range(7):
            print(mouvment[i][j],end = "")
        print("")

print(melee_count(exemple))


def calcul(board,newboard) :
    result = 0
    for i in range(board.len):
        if (i == 1):
            if(newboard[i].PV <= 0):
                result = result-10000
            else:
                result = result - (board[i].PV - newboard[i].PV)
        else:
            if(newboard[i].PV <= 0):
                result = result + 2000 + newboard[i].atk
            else:
                result = result + 5*(board[i].PV - newboard[i].PV )
    return result


def attack(board,perso):
    mainpos = perso[0].position
    for i in range(perso.len000):
        if (i!=0):
            TheoricalMovment(perso[i].position,board,mouvment,n=perso[i].PM)
            if(mouvment[mainpos[0] + 1][mainpos[1]] == 1):
                board[mainpos[0] + 1][mainpos[1]] = board[perso[i].position[0]][perso[i].position[1]]
                board[perso[i].position[0]][perso[i].position[1]] = 0
                perso[0].PV = perso[0].PV-perso[i].atk
            elif(mouvment[mainpos[0]][mainpos[1]+1] == 1):
                board[mainpos[0]][mainpos[1]+1] = board[perso[i].position[0]][perso[i].position[1]]
                board[perso[i].position[0]][perso[i].position[1]] = 0
                perso[0].PV = perso[0].PV-perso[i].atk
            elif(mouvment[mainpos[0] - 1][mainpos[1]] == 1):
                board[mainpos[0] - 1][mainpos[1]] = board[perso[i].position[0]][perso[i].position[1]]
                board[perso[i].position[0]][perso[i].position[1]] = 0
                perso[0].PV = perso[0].PV-perso[i].atk
            elif(mouvment[mainpos[0] - 1][mainpos[1]] == 1):
                board[mainpos[0] - 1][mainpos[1]] = board[perso[i].position[0]][perso[i].position[1]]
                board[perso[i].position[0]][perso[i].position[1]] = 0
                perso[0].PV = perso[0].PV-perso[i].atk
    