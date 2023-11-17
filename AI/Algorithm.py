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
    def _init_(self,board_ID,char_list,instruction_list,score = 0) -> None:
        self.board_ID = board_ID                    #The unique ID of the board build on parents boards if any
        self.char_list = char_list                  #The list of all charcaters on board
        self.instruction_list = instruction_list    #The list of instructions required to reach the board
        self.score = score
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

def launch_simulation(previous_boards = [],n = 1):
    if(n>0):    
        all_boards = move_simulation(previous_boards)
        all_boards = spell_simulation(all_boards)
        all_boards = foes_simulation(all_boards)
        for i in all_boards:
            i.score = score_calcul(i)
        launch_simulation(all_boards,n-1)
    else:
        if(len(previous_boards)>0):
            best_board = previous_boards[0]
            for i in range (1,len(previous_boards)):
                if(previous_boards[i].score > best_board.score):
                    best_board = previous_boards[i]
            return best_board.instruction_list
        else:
            print("error, no board generated")
        

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

def score_calcul(board,newboard) :
    result = 0
    for i in range(board.len):
        if (board[i].ID == 0):
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

def foes_simulation(board,perso):
    mainpos = perso[0].position
    for i in range(perso.len):
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

def move_simulation(previous_boards):