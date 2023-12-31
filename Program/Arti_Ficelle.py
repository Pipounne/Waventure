from numpy import *

#We create a character class to gather all the data extracted from the game
class character:
    def __init__(self,name,ID,ally,max_health,PV,armor,atk,init_atk,PM,PA,position,flags = {}) -> None:
        self.name = name            #The name of the cbaracter
        self.ID = ID                #An ID to easily distinguish all characters
        self.ally = ally            #A boolean to divide character into allies and enemies
        self.max_health = max_health#The maximum value for PV
        self.PV = PV                #The health points of the character
        self.armor = armor          #The armor points of the character
        self.atk = atk              #The attack value of the character
        self.init_atk = init_atk
        self.PA = PA
        self.PM = PM                #The movement point of the character
        self.position = position    #The position of the character on the board as a tuple (x,y)
        self.flags = {}
        for cle,valeur in flags.items():
            self.flags[cle] = valeur


#We create a board class to set a template for all our generated boards
class board:
    def __init__(self,board_ID,char_list,instruction_list,spell_list,deck = {},score = 0) -> None:
        self.board_ID = board_ID                        #The unique ID of the board build on parents boards if any
        self.char_list = []                             #The list of all charcaters on board
        for i in range (len(char_list)):
            self.char_list.append(character(char_list[i].name,char_list[i].ID,char_list[i].ally,char_list[i].max_health,char_list[i].PV,char_list[i].armor,char_list[i].atk,char_list[i].init_atk,char_list[i].PM,char_list[i].PA,char_list[i].position,char_list[i].flags))
        self.instruction_list = instruction_list[:]     #The list of instructions required to reach the board
        self.score = score                              #The score of the board, calculated later
        self.deck = {}
        for cle,valeur in deck.items():
            self.deck[cle] = [spell(valeur[0].ID,valeur[0].name,valeur[0].cost,valeur[0].dmg,valeur[0].extra_effect),valeur[1]]
        self.spell_list = []
        for i in range (len(spell_list)):
            self.spell_list.append(deck[spell_list[i].name][0])              #The spells available to the player, maximum of 7

#We create a spell class to store all informations about spells
class spell:
    def __init__(self,ID,name,cost,dmg,extra_effect) -> None:
        self.ID=ID
        self.name=name
        self.cost=cost
        self.dmg=dmg
        self.extra_effect=extra_effect
    
spells = {}

spells["Fulgur"]=[(spell("0","Fulgur",3,14,("single_dmg_melee",4))),[(185,62,10)]]
spells["Touche Enflammée"]=[(spell("1","Touche Enflammée",3,9,("square_dmg_hero_melee",5))),[(255,158,34),(255,194,50),(254, 103, 13)]]
spells["Nouvelle Vague"]=[(spell("2","Nouvelle Vague",6,36,("None"))),[(0,236,155),(0,236,255)]]
spells["Onde de Choc"]=[(spell("3","Onde de Choc",8,38,("cost_reduce_melee",8))),[(12, 135, 187),(34, 46, 51)]]
spells["Armure Brutale"]=[(spell("4","Armure Brutale",3,0,("dmg_equal_armor"))),[(243, 243, 245)]]
spells["Heurt de Gloire"]=[(spell("5","Heurt de Gloire",3,8,("armor_add_melee",3))),[(264, 264, 251),(250, 253, 174),(248, 253, 145)]]
spells["Touche Aqueuse"]=[(spell("6","Touche Aqueuse",4,18,("heal_melee",6))),[(3, 105, 145)]]
spells["Dag"]=[(spell("7","Dag",4,17,("None"))),[(121, 246, 253),(64, 241, 252)]]
spells["Touche Terrestre"]=[(spell("8","Touche Terrestre",5,26,("armor_add_melee",8))),[(95, 148, 8)]]
spells["Butoir"]=[(spell("9","Butoir",5,30,("None"))),[(69, 104, 7)]]
spells["Foudroyer"]=[(spell("10","Foudroyer",5,29,("None"))),[(75,2,227)]]
spells["Touche Venteuse"]=[(spell("11","Touche Venteuse",6,27,("single_dmg_melee",7))),[(196,115,255),(184, 87, 255)]]
spells["Sentence"]=[(spell("12","Sentence",6,0,("dmg_equal_atk"))),[(220, 130, 84),(240, 199, 141),(227, 154, 95),(233, 175, 114)]]
spells["Accumulation"]=[(spell("13","Accumulation",6,0,("dmg_equal_atk_stack_melee",0))),[(239, 210, 108)]]
spells["Demonstration Brutale"]=[(spell("14","Demonstration Brutale",7,0,("dmg_equal_atk_cost_reduce_melee",7))),[(242, 224, 116),(89, 87, 78)]]


#For debug purpose
def print_board(board):
    tab = [['/' for i in range (7)] for j in range (7)]
    for i in range(len(board)):
        if(board[i].ally):
            tab[board[i].position[0]][board[i].position[1]]="\033[92m" + board[i].ID + "\033[0m"
        else:
            tab[board[i].position[0]][board[i].position[1]]="\033[91m" + board[i].ID + "\033[0m"
    return tab

#This function test if a chosen cell is free to move on
def IsCellFree(wanted_cell,char_list,ID):
    available = True
    for i in range (len(char_list)):
        if(ID != char_list[i].ID):
            if(wanted_cell == char_list[i].position):
                available = False
    return available

#A function to calcul all available deplacements
def TheoricalMovment(starting_pos,char_list,mouvment,ID,n = 5):
    if (n != 0) :
        if(-1<starting_pos[0]<7 and -1<starting_pos[1]<7):
            if(IsCellFree(starting_pos,char_list,ID)):
                mouvment[starting_pos[0]][starting_pos[1]] = 1
                TheoricalMovment((starting_pos[0]+1,starting_pos[1]),char_list,mouvment,ID,n-1)
                TheoricalMovment((starting_pos[0]-1,starting_pos[1]),char_list,mouvment,ID,n-1)
                TheoricalMovment((starting_pos[0],starting_pos[1]+1),char_list,mouvment,ID,n-1)
                TheoricalMovment((starting_pos[0],starting_pos[1]-1),char_list,mouvment,ID,n-1)
            else:
                mouvment[starting_pos[0]][starting_pos[1]] = 2

#A function to know how many foes are in the melee keyword
def melee_count(position,char_list,ID):
    cpt = 0
    for i in range (len(char_list)):
        if (ID != char_list[i].ID):
            if (abs(char_list[i].position[0]-position[0])<=1) and (abs(char_list[i].position[1]-position[1])<=1):
                cpt +=1
    return cpt

#create all simulations
def launch_simulation(previous_boards,return_tab,n = 1):
    if(n>0):    
        all_boards = move_simulation(previous_boards[-1])
        all_boards = spell_simulation(all_boards)
        for i in range(len(all_boards)):
            all_boards[i] = foes_simulation(all_boards[i])
        for i in range(len(all_boards)):
            all_boards[i].score = score_calcul(previous_boards[0][0],all_boards[i])
        previous_boards.append(all_boards)  
        launch_simulation(previous_boards,return_tab,n-1)
    else:
        if(len(previous_boards[1])>0):
            best_board = previous_boards[1][0]
            for i in range (1,len(previous_boards[1])):
                if(previous_boards[1][i].score > best_board.score):
                    best_board = previous_boards[1][i]
            for x in range (len(best_board.instruction_list)):
                return_tab.append([])
                for y in range (len(best_board.instruction_list[x])):
                    return_tab[x].append(best_board.instruction_list[x][y])

#Calcul the sscore of a given board
def score_calcul(board,newboard) :
    result = 0
    for i in range(len(newboard.char_list)):
        if (i == 0):
            if(newboard.char_list[i].PV <= 0):
                result = result-10000
            else:
                result = result - (board.char_list[i].PV - newboard.char_list[i].PV)
        else:
            if(newboard.char_list[i].PV <= 0):
                result = result + 2000 + newboard.char_list[i].atk
            else:
                result = result + 5*(board.char_list[i].PV - newboard.char_list[i].PV )
    return result

def foes_simulation(board,k = 1):
    mainpos = board.char_list[0].position
    n = len(board.char_list)
    newboard = board
    result = [board,board,board,board]
    score1 = 0
    score2 = 0
    temp = 0
    mouvment = [[0 for i in range (7)] for j in range (7)]
    if (k<n):
        TheoricalMovment(board.char_list[k].position,board.char_list, mouvment,str(k))
        if( mainpos[0]<5 and mouvment[ mainpos[0] + 1][mainpos[1]] == 1 ):
            newboard = board
            newboard.char_list[k].position = (mainpos[0] + 1,mainpos[1])
            result[0] = foes_simulation(newboard, k+1)
        if(mainpos[1]<5 and mouvment[ mainpos[0]][mainpos[1]+1] == 1 ):
            newboard = board
            newboard.char_list[k].position = (mainpos[0],mainpos[1]+1)
            result[1] = foes_simulation(newboard, k+1)
        if(mainpos[0]>0 and mouvment[ mainpos[0] - 1][mainpos[1]] == 1 ):
            newboard = board
            newboard.char_list[k].position = (mainpos[0] - 1,mainpos[1])
            result[2] = foes_simulation(newboard, k+1)
        if( mainpos[1]>0 and mouvment[  mainpos[0]][mainpos[1]-1] == 1):
            newboard = board
            newboard.char_list[k].position = (mainpos[0],mainpos[1]-1)
            result[3] = foes_simulation(newboard, k+1)
        for i in range(4):
            for j in range(1,n):
                if (result[i].char_list[j].position in [(mainpos[0] - 1,mainpos[1]),(mainpos[0],mainpos[1]-1),(mainpos[0] + 1,mainpos[1]),(mainpos[0],mainpos[1]+1)]):
                    score2 = score2+1
            if (score2 > score1):
                score1 = score2
                temp = i
            score2 = 0
        return result[temp]
        
    else:
        return board
      
def damage(char_list, damages, defender_ID):
    char_list[int(defender_ID)].armor = char_list[int(defender_ID)].armor - damages
    if(char_list[int(defender_ID)].armor <= 0):
        char_list[int(defender_ID)].PV = char_list[int(defender_ID)].PV + char_list[int(defender_ID)].armor
        char_list[int(defender_ID)].armor = 0
    
    if(char_list[int(defender_ID)].PV <= 0 ):
        char_list.pop(int(defender_ID))

def heal(char, value):
    char.PV += value
    if(char.PV>char.max_health):
        char.PV = char.max_health

def update_armor_bonus(char_list):
    if(char_list[0].armor > 0):
        char_list[0].atk = char_list[0].init_atk + 0.6 * char_list[0].armor


def move_simulation(previous_boards):
    for i in range (len(previous_boards)):
        update_armor_bonus(previous_boards[i].char_list)
        cpt = 1
        return_boards = []
        mouvment = [[0 for j in range (7)] for i in range(7)]
        TheoricalMovment(previous_boards[i].char_list[0].position,previous_boards[i].char_list,mouvment,"0")
        for x in range (7):
            for y in range (7):
                if(mouvment[x][y]==2):
                    if((x-1>=0) and mouvment[x-1][y] == 1):
                        return_boards.append(board(previous_boards[i].board_ID+"/"+str(cpt),previous_boards[i].char_list,previous_boards[i].instruction_list,previous_boards[i].spell_list,previous_boards[i].deck))
                        return_boards[-1].instruction_list += [[2,previous_boards[i].char_list[0].position,(x-1,y),(x,y)]]
                        return_boards[-1].char_list[0].position = (x-1,y)
                        cpt+=1
                        j = 0
                        while j < len(return_boards[-1].char_list):
                            if(return_boards[-1].char_list[j].position == (x,y)):
                                damage(return_boards[-1].char_list,return_boards[-1].char_list[0].atk+(0.6*return_boards[-1].char_list[0].armor),return_boards[-1].char_list[j].ID)
                            j+=1    
                    
                    
                    if((x+1<7) and (mouvment[x+1][y] == 1)):
                        return_boards.append(board(previous_boards[i].board_ID+"/"+str(cpt),previous_boards[i].char_list,previous_boards[i].instruction_list,previous_boards[i].spell_list,previous_boards[i].deck))
                        return_boards[-1].instruction_list += [[2,previous_boards[i].char_list[0].position,(x+1,y),(x,y)]]
                        return_boards[-1].char_list[0].position = (x+1,y)
                        cpt+=1
                        j = 0 
                        while j < len(return_boards[-1].char_list):
                            if(return_boards[-1].char_list[j].position == (x,y) ):
                                damage(return_boards[-1].char_list,return_boards[-1].char_list[0].atk+(0.6*return_boards[-1].char_list[0].armor),return_boards[-1].char_list[j].ID)
                            j+=1
                    if((y-1>=0)  and (mouvment[x][y-1] == 1)):
                        return_boards.append(board(previous_boards[i].board_ID+"/"+str(cpt),previous_boards[i].char_list,previous_boards[i].instruction_list,previous_boards[i].spell_list,previous_boards[i].deck))
                        return_boards[-1].instruction_list += [[2,previous_boards[i].char_list[0].position,(x,y-1),(x,y)]]
                        return_boards[-1].char_list[0].position = (x,y-1)
                        cpt+=1
                        j = 0
                        while j < len(return_boards[-1].char_list):
                            if(return_boards[-1].char_list[j].position == (x,y)):
                                damage(return_boards[-1].char_list,return_boards[-1].char_list[0].atk+(0.6*return_boards[-1].char_list[0].armor),return_boards[-1].char_list[j].ID)
                            j+=1
                    if((y+1<7) and (mouvment[x][y+1] == 1)):
                        return_boards.append(board(previous_boards[i].board_ID+"/"+str(cpt),previous_boards[i].char_list,previous_boards[i].instruction_list,previous_boards[i].spell_list,previous_boards[i].deck))
                        return_boards[-1].instruction_list += [[2,previous_boards[i].char_list[0].position,(x,y+1),(x,y)]]
                        return_boards[-1].char_list[0].position = (x,y+1)
                        cpt+=1
                        j = 0
                        while j < len(return_boards[-1].char_list):
                            if(return_boards[-1].char_list[j].position == (x,y)):
                                damage(return_boards[-1].char_list,return_boards[-1].char_list[0].atk+(0.6*return_boards[-1].char_list[0].armor),return_boards[-1].char_list[j].ID)
                            j+=1

        if(len(return_boards) == 0):
            for x in range (7):
                for y in range (7):
                    if(mouvment[x][y]==1):
                        return_boards.append(board(previous_boards[i].board_ID+"/"+str(cpt),previous_boards[i].char_list,previous_boards[i].instruction_list,previous_boards[i].spell_list,previous_boards[i].deck))
                        return_boards[-1].instruction_list += [[1,previous_boards[i].char_list[0].position,(x,y)]]
                        return_boards[-1].char_list[0].position = (x,y)
                        cpt+=1
                        
        return return_boards
   
def precast(board):
    for i in range(len(board.spell_list)):
        if(board.spell_list[i].extra_effect=="cost_reduce_melee"):
            board.spell_list[i].cost = board.spell_list[i].extra_effet[1]-melee_count(board.char_list[0].position,board.char_list,0)
        elif(board.spell_list[i].extra_effect=="dmg_equal_armor"):
            board.spell_list[i].dmg = board.char_list[0].armor
        elif(board.spell_list[i].extra_effect=="dmg_equal_atk"):
            board.spell_list[i].dmg = board.char_list[0].atk
        elif(board.spell_list[i].extra_effect==" dmg_equal_atk_cost_reduce_melee"):
            board.spell_list[i].dmg = board.char_list[0].atk
            board.spell_list[i].cost = board.spell_list[i].extra_effet[1]-melee_count(board.char_list[0].position,board.char_list,0)
        elif(board.spell_list[i].extra_effect=="dmg_equal_atk_stack_melee"):
            board.spell_list[i].dmg = (board.char_list[0].atk/4)*board.spell_list[i].extra_effet[1] + board.char_list[0].atk
            

def cast_spell(board,target_ID,spell):
    board.char_list[0].PA -= spell.cost
    if (melee_count(board.char_list[0].position,board.char_list,0)>0) and (spell.extra_effect[0][-5:]=="melee"):
        if (board.char_list[0].flags["passif_Justelame"]):
            board.char_list[0].armor += 0.5 * board.char_list[0].atk
            board.char_list[0].flags["passif_Justelame"] = False
        board.char_list[0].armor += 0.15*board.char_list[0].atk*melee_count(board.char_list[0].position,board.char_list,0)
        board.deck["Accumulation"][0].extra_effect=(board.deck["Accumulation"][0].extra_effect[0],board.deck["Accumulation"][0].extra_effect[1]+1)
        if(spell.extra_effect[0] == "single_dmg_melee"):
            damage(board.char_list,spell.extra_effect[1]+spell.dmg,target_ID)
        else:
            if(spell.extra_effect[0] == "square_dmg_hero_melee"):
                i=1
                while i < len(board.char_list):
                    if(abs(board.char_list[i].position[0]-board.char_list[0].position[0])<=1) and (abs(board.char_list[i].position[1]-board.char_list[0].position[1])<=1):
                        damage(board.char_list,spell.extra_effect[1],i)
                    i+=1
            elif(spell.extra_effect[0] == "heal_melee"):
                heal(board.char_list[0],spell.extra_effect[1])
            elif(spell.extra_effect[0] == "armor_add_melee"):
                board.char_list[0].armor += spell.extra_effect[1]
        #ne pas oublier de boost le sort de ces morts
    else:
         damage(board.char_list,spell.dmg,target_ID)
    
    board.char_list[0].PA -= spell.cost

def spell_simulation(current_boards):
    cpt = 1
    return_boards = current_boards
    for i in range (len(current_boards)):
        update_armor_bonus(current_boards[i].char_list)
        precast(current_boards[i])
        for j in range (len(current_boards[i].spell_list)):
            if(current_boards[i].char_list[0].PA>=current_boards[i].spell_list[j].cost):
                for k in range (1,len(current_boards[i].char_list)):       
                    return_boards.append(board(current_boards[i].board_ID+"."+str(cpt),current_boards[i].char_list,current_boards[i].instruction_list,current_boards[i].spell_list,current_boards[i].deck))
                    return_boards[-1].instruction_list+=([[3,j,return_boards[-1].char_list[k].position]])
                    cast_spell(return_boards[-1],k,return_boards[-1].spell_list[j])
                    return_boards[-1].spell_list.pop(j)
                    for l in range (len(return_boards[-1].spell_list)):
                        update_armor_bonus(return_boards[-1].char_list)
                        if(return_boards[-1].char_list[0].PA>=return_boards[-1].spell_list[l].cost):
                            for m in range (1,len(current_boards[i].char_list)):       
                                return_boards.append(board(return_boards[-1].board_ID+"+"+str(cpt),return_boards[-1].char_list,return_boards[-1].instruction_list,return_boards[-1].spell_list,return_boards[i].deck))
                                return_boards[-1].instruction_list+=([[3,l,return_boards[-1].char_list[m].position]])
                                cast_spell(return_boards[-1],m,return_boards[-1].spell_list[l])
                                return_boards[-1].spell_list.pop(l)
    return return_boards
