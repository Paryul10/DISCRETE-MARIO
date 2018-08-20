import sys,os,time,random,signal
#from getch import *
import board
import person
import player
import enemy
#import signal
#from alarmexception import *
#import random
import config
import objects
#import inp
#pylint: disable-msg=R0913

#EACH INSTANCE YOU NEED TO STORE THE 

# def alarmHandler(signum, frame):
#     raise AlarmException

# def input_char(timeout=1):
#     signal.signal(signal.SIGALRM, alarmHandler)
#     signal.alarm(timeout)
#     try:
#         text = getch()
#         signal.alarm(0)
#         return text
#     except AlarmException:
#         pass
#     signal.signal(signal.SIGALRM, signal.SIG_IGN)
#     return ''

height = 30
width = 60
bidi = board.Board(height,width)

game_time = 120

playboy = player.Mario(height-6,6,1)
playboy.set_player(height-6,6)
setx = height - 6
sety = 6

#cloud = objects.Cloud()
clouds = []
for i in range(1,60):
    x = random.randint(2,height-12)
    y = i * random.randint(14,16)
    l = random.randint(3,6)
    w = random.randint(5,6)
    if(w<=l):
        i-=1
    else:
        cloud = objects.Cloud(x,y,l,w)
        clouds.append(cloud)

bidi.initialize()
#set_clouds()
bidi.set_score(playboy)

en = []
getch = config.GetchUnix()


#count=0
##########################-------------------SPAWNS-ENEMY WHEN CALLED--------------------------######################
def spawn_enemy():
    x = height - 6
    y = bidi.left + random.randint(int(width/2),width -5)
    fl=1
    for enem in en:
        if(y == enem.yc):
            fl=0
        #if(bidi[x][y] == 'M'):  #here you will see where the enemies not to be spawned -------FUTURE
            #fl=0


    if(fl):
        ene = enemy.Enemy(x,y,1)
        en.append(ene)
    else:
        spawn_enemy()



            

    

os.system('clear')
#bidi.render()
prev = -1 
start = time.time()
dooms = start
while(True):
    
#''' this part moves the enemy after every half second , checks player status ,enemy status ,initializes , sets player and enemies
 #   '''
    if(time.time() - start > .5):
        start = time.time()
        if(len(en) < 2):
            spawn_enemy()
        for eni in en:
            eni.move_enemy(eni.xc,eni.yc,playboy.yc)
            playboy.check_player_alive(dooms,bidi)
            chk = eni.check_enemy_alive(playboy)
            if(chk):
                en.remove(eni)

        bidi.initialize()
        bidi.set_score(playboy)
        playboy.set_player(playboy.xc, playboy.yc)
        for eni in en:
            eni.set_enemy(eni.xc, eni.yc)
        os.system('clear')
        bidi.render(playboy,en)

#''' takes user input and does the functionality accordingly '''
    inp = config.input_char()
    if(inp == 'a'):
        #print("a")
        playboy.move_player(0,-1,bidi)
        prev = 0
    elif(inp == 'd'):
        #print("d")
        playboy.move_player(0,1,bidi)
        prev = 1
    elif(inp == 'w'):
        #print("w")
        playboy.jump(bidi,prev,en,playboy,dooms)
        prev = -1

    if(inp == 'q'):
        print("q")
        sys.exit(0)

#''' after input the positions change , we need to reset the board , set the new positions of player ,enemy ,, clear screen ,and print board'''
    bidi.initialize()
    bidi.set_score(playboy)
    playboy.set_player(playboy.xc, playboy.yc)
    for eni in en:
            check = eni.check_enemy_alive(playboy)
            if(check):
                en.remove(eni)
    for eni in en:
        eni.set_enemy(eni.xc, eni.yc)
    os.system('clear')
    bidi.render(playboy,en)


