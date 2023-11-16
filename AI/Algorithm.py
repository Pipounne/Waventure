
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

#We create a board class to set a template for all our generated boards
class board:
    def _init_(self,board_ID,char_list,instruction_list) -> None:
        self.board_ID = board_ID                    #The unique ID of the board build on parents boards if any
        self.char_list = char_list                  #The list of all charcaters on board
        self.instruction_list = instruction_list    #The list of instructions required to reach the board
        pass


exemple = []

exemple.append(character("Arti Ficelle","0",True,391,35,3,(0,0)))
exemple.append(character("Tofu 1","1",False,120,30,3,(5,4)))
exemple.append(character("Tofu 2","2",False,110,32,3,(4,5)))

exemple2 = []

exemple2.append(character("Arti Ficelle","0",True,391,35,3,(4,4)))
exemple2.append(character("Tofu 1","1",False,120,30,3,(5,4)))
exemple2.append(character("Tofu 2","2",False,110,32,3,(4,5)))

#For debug purpose
def print_board(board):
    tab = [['/' for i in range (7)] for j in range (7)]
    for i in range(len(board)):
        if(board[i].ally):
            tab[board[i].position[0]][board[i].position[1]]="\033[92m" + board[i].ID + "\033[0m"
        else:
            tab[board[i].position[0]][board[i].position[1]]="\033[91m" + board[i].ID + "\033[0m"
    return tab

#???
def remplissage(character) :
    characters = character[7][7]
    for i in range(7):
        for j in range(7):
            characters[i][j] = character[i*j]

#This function test if a chosen cell is free to move on
def IsCellFree(wanted_cell,char_list,ID):
    available = True
    for i in range (len(char_list)):
        if(ID != char_list[i].ID):
            if(wanted_cell == char_list[i].position):
                available = False
    return available

#A function to calcul all available deplacements
def TheoricalMovment(starting_pos,char_list,mouvment,ID,n = 4):
    if (n != 0) :
        if(-1<starting_pos[0]<7 and -1<starting_pos[1]<7):
            if(IsCellFree(starting_pos,exemple,ID)):
                mouvment[starting_pos[0]][starting_pos[1]] = 1
                TheoricalMovment((starting_pos[0]+1,starting_pos[1]),char_list,mouvment,ID,n-1)
                TheoricalMovment((starting_pos[0]-1,starting_pos[1]),char_list,mouvment,ID,n-1)
                TheoricalMovment((starting_pos[0],starting_pos[1]+1),char_list,mouvment,ID,n-1)
                TheoricalMovment((starting_pos[0],starting_pos[1]-1),char_list,mouvment,ID,n-1)
            else:
                mouvment[starting_pos[0]][starting_pos[1]] = 2

#A function to know how many foes are in the melee kayword
def melee_count(position,char_list,ID):
    cpt = 0
    for i in range (len(char_list)):
        if (ID != char_list[i].ID):
            if (abs(char_list[i].position[0]-position[0])<=1) and (abs(char_list[i].position[1]-position[1])<=1):
                cpt +=1
    return cpt

mouvment = [[0 for j in range (7)] for i in range(7)]    

TheoricalMovment(exemple2[0].position,exemple2,mouvment,"0")
for i in range (7):
    for j in range (7):
        print(mouvment[i][j],end="")
    print("")

tab = print_board(exemple2)
for i in range (7):
    for j in range (7):
        print(tab[i][j],end="")
    print("")

print(melee_count(exemple2[0].position,exemple2,"0"))

