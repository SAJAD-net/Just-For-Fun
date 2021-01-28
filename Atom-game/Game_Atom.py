# import  module os and random
from colorama import init
init()
from colorama import Fore,Back,Style
import random 
import os
#craete a list of locations a player on the grid
cellse=[
    (0,0),(1,0),(2,0),(3,0),(4,0),
    (0,1),(1,1),(2,1),(3,1),(4,1),
    (0,2),(1,2),(2,2),(3,2),(4,2),
    (0,3),(1,3),(2,3),(3,3),(4,3),
    (0,4),(1,4),(2,4),(3,4),(4,4),
]
def clear_screen():
    os.system('cls')
##########################################################
def grt_locations():
    return random.sample(cellse,3)
###########################################################
# function a move the locations of player
def move_player(player, move):
    x,y = player
    
    if move =='LEFT':
        x -= 1
    if move == 'RIGHT':
        x += 1
    if move =='UP':
        y -= 1
    if move =='DOWN':
        y += 1        
    return x,y
# function a mvoe
def get_move(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    x,y = player
    if x == 0:
        moves.remove('LEFT')
    if x == 4:
        moves.remove('RIGHT')
    if y == 0:
        moves.remove('UP')
    if y == 4:
        moves.remove('DOWN')
    return moves            
# func a map is game
def draw_map(player):
    print(Fore.RED+" _"*5)
    tile = "|{}"
    
    for cell in cellse:
        x,y = cell
        if x < 4:
            line_end=""
            if cell == player :
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end='\n'
            if cell == player :
                output = tile.format("X|")            
            else:
                output = tile.format('_|')
        print(Fore.BLUE+output,end=line_end)    
#func a run in the game         
def game_loop():
    monster , door , player = grt_locations()
    playing = True
    
    
    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_move(player)
        print(Fore.YELLOW+"you're to currently in room {}".format(player))
        print(Fore.RED + 'you can move {}'.format(','.join(valid_moves)))
        print(Fore.GREEN + 'enter "quit" to exit.')
        
        move = input('> ')
        move = move.upper()
        
        if move == 'QUIT':
            break
        if move in valid_moves:
            player = move_player(player, move)
            if player == 'monster':
                print(Fore.BLUE + 'oh, sorry you failed to game')
                playing=False
            if player == "door":
                print(Fore.BLUE + "\n **You scaped congratulation general ** \n")  
                playing = False
        else:
            input("\n  ** walls are hard! don,t run into them! ** \n")    
    else:
        if input('Ply again? [Y/n]').lower() != "n":
            game_loop() 
clear_screen()
print(Fore.RED + 'Welcome to Atom')
input('Press return to start!')
clear_screen()
game_loop()
