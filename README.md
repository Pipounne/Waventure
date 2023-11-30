This project is only educational and is created in the context of a school project, we do not aim to actively use bot on Waven or sell any bot software to other players.

# Waventure

CARRE Arthur - Engineering college Leonard De Vinci - arthur@carreo.fr  
LEDRU Solal - Engineering college Leonard De Vinci - solal.ledru@edu.devinci.fr  
HIRTH Quentin - Engineering college Leonard De Vinci - quentin.hirth@edu.devinci.fr  
LEFEBVRE Romain - Engineering college Leonard De Vinci - romain.lefebvre@edu.devinci.fr  

# Abstract :

Our project would be software that the user would launch at the start of a battle in the game Waven. The software would aim to see and understand the placement of enemies as well as their types and statistics. He must also be able to read and know the cards he has available to play. His mission will then be to play against the enemies. To play, he will have to perform two actions: move/attack (in Waven the attack is an extension of the movement) as well as cast cards (spells) to overcome enemies. In addition, he must respect the rules imposed by the game to succeed in the daily quest.
If we succeed in the project, there are two very similar ways to improve it. The first is to ensure that the software can launch itself into the game and that it can navigate the menus on its own to choose which fight to carry out. The second would be that he can repeat the same mission a defined number of times to collect rewards in large quantities.
It would also be interesting to teach our project to play with characters that have more complex gameplay.

# A quick look at Waven :

"Waven" is a video game released on June 19, 2023. This game is free and developed by Ankama, continuing the storyline of the company's previous works such as the MMO Dofus or the animated serie Wakfu.

The game exclusively focus on his turn by turn combat system, giving player 20 classes and dozens of spell and gears to defeat all challenges available, alone or in team with one or two other players. It's this combat systeme we will be trying to automate.

The downside for our software is that trying to automate a game with so much customisation is gargantuan, so we only provide the software for a specific class, the Brutal Fairblade, and build.

For more informations concerning the comabt system and scope of the project, please look at the documentation file.

# Methodology :

To find the optimal turn to make, the software will read all the needed informations by analysing screenshots taken from your screen in game. All the data extracted will go in specific objects to get the basic understanding of the overall challenge to solve.

Then we begin the simulation, we first observe all cells we can reach and choose the ones that allows melee attack. If no melee attack can be land, we choose all possible mouvement. Then, we test all combinations of spells we can cast this turn, try to naivly predict foes' mouvements and grade our calculated outcomes. 

To grade our outcomes and choose the best ones we compare the simulated boards with the initial situation and see how many damages were dealt, receives, if ennemies were defeated or if you was defeated yourself. We obviously want to make a maximum of damages while taking the less and not being defeated.

# How to run

- Install Waven from Ankama official website ( https://www.waven-game.com/en/download )
- log in with the appropriate character (please contact us if you need the test account)
- launch the software and Waven
- Use the "refresh" button to assure the software recognize your game
- Enter any fight on Waven and click on the software "start" button
- Enjoy
