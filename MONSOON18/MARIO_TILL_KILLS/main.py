import sys,os,time,random,signal
import board
import person
import player
import enemy
import config
import objects
import subprocess

height = 40
width = 60
bidi = board.Board(height,width)
playboy = player.Mario(height-6,6,1)
playboy.set_player(height-6,6)
setx = height - 6
sety = 6

game_time = 120

scene = []
statics = []
statics_y = []
en = []
cns = []

def make_coins():
    coin = objects.Coins(height-5,21,1,1)
    cns.append(coin)
    coin = objects.Coins(height-6,32,1,1)
    cns.append(coin)

    coin = objects.Coins(height-19,32,1,1)
    cns.append(coin)
    coin = objects.Coins(height-19,33,1,1)
    cns.append(coin)
    coin = objects.Coins(height-20,54,1,1)
    cns.append(coin)
    coin = objects.Coins(height-20,52,1,1)
    cns.append(coin)
    coin = objects.Coins(height-7,79,1,1)
    cns.append(coin)
    coin = objects.Coins(height-11,141,1,1)
    cns.append(coin)
    coin = objects.Coins(height-11,142,1,1)
    cns.append(coin)
    coin = objects.Coins(height-11,143,1,1)
    cns.append(coin)

    coin = objects.Coins(height-23,173,1,1)
    cns.append(coin)
    coin = objects.Coins(height-23,174,1,1)
    cns.append(coin)
    
    coin = objects.Coins(height-18,211,1,1)
    cns.append(coin)
    coin = objects.Coins(height-18,212,1,1)
    cns.append(coin)
    coin = objects.Coins(height-18,213,1,1)
    cns.append(coin)

    coin = objects.Coins(height-16,294,1,1)
    cns.append(coin)
    coin = objects.Coins(height-16,307,1,1)
    cns.append(coin)
    coin = objects.Coins(height-16,320,1,1)
    cns.append(coin)
    
    coin = objects.Coins(height-7,330,1,1)
    cns.append(coin)
    coin = objects.Coins(height-11,334,1,1)
    cns.append(coin)
    coin = objects.Coins(height-15,338,1,1)
    cns.append(coin)
    coin = objects.Coins(height-19,342,1,1)
    cns.append(coin)
    coin = objects.Coins(height-23,346,1,1)
    cns.append(coin)



def make_scene():
    for i in range(1,30):
        x = random.randint(2,height-18)
        y = i * random.randint(28,30)
        l = random.randint(3,6)
        w = random.randint(5,6)
        cloud = objects.Cloud(x,y,l,w)
        scene.append(cloud)

    for i in range(1, 20):
        typ = random.randint(1,3)
        x = height - 5      
        if typ == 1:
            hill = objects.Hills(x, i*40, 4, 8, 1)
        elif typ == 2:
            hill = objects.Hills(x, i*40, 6, 12, 2)
        else:
            hill = objects.Hills(x, i*40, 6, 12, 3)            
        scene.append(hill)

def make_objects():
    br = objects.Bricks(height-12, 18, 2, 8)
    statics.append(br)
    br = objects.Bricks(height-18, 30, 2, 6)
    statics.append(br)
    br = objects.Bricks(height-12, 40, 2, 8)
    statics.append(br)

    p = objects.Pipe(height-11, 70, 7, 6)
    statics.append(p)
    p = objects.Pipe(height-14, 82, 10, 10)
    statics.append(p)
    p = objects.Pipe(height-22, 98, 18, 8)
    statics.append(p)

    h = objects.Holes(height-4, 140, 3, 5)
    statics.append(h)
    
    br = objects.Bricks(height-12, 160, 2, 6)
    statics.append(br)
    br = objects.Bricks(height-17, 172, 2, 4)
    statics.append(br)
    br = objects.Bricks(height-6, 200, 2, 10)
    statics.append(br)
    br = objects.Bricks(height-8, 202, 2, 8)
    statics.append(br)
    br = objects.Bricks(height-10, 204, 2, 6)
    statics.append(br)
    br = objects.Bricks(height-12, 206, 2, 4)
    statics.append(br)
    br = objects.Bricks(height-14, 208, 2, 2)
    statics.append(br)
    h = objects.Holes(height-4, 210, 3, 5)
    statics.append(h)
    br = objects.Bricks(height-14, 215, 2, 2)
    statics.append(br)
    br = objects.Bricks(height-12, 215, 2, 4)
    statics.append(br)
    br = objects.Bricks(height-10, 215, 2, 6)
    statics.append(br)
    br = objects.Bricks(height-8, 215, 2, 8)
    statics.append(br)
    br = objects.Bricks(height-6, 215, 2, 10)
    statics.append(br)

    br = objects.Bricks(height-14, 240, 2, 6)
    statics.append(br)
    br = objects.Bricks(height-14, 258, 2, 6)
    statics.append(br)
    br = objects.Bricks(height-14, 276, 2, 8)
    statics.append(br)

    p = objects.Pipe(height-11, 290, 7, 8)
    statics.append(p)
    p = objects.Pipe(height-11, 303, 7, 8)
    statics.append(p)
    p = objects.Pipe(height-11, 316, 7, 8)
    statics.append(p)

    br = objects.Bricks(height-6, 330, 2, 20)
    statics.append(br)
    br = objects.Bricks(height-8, 332, 2, 18)
    statics.append(br)
    br = objects.Bricks(height-10, 334, 2, 16)
    statics.append(br)
    br = objects.Bricks(height-12, 336, 2, 14)
    statics.append(br)
    br = objects.Bricks(height-14, 338, 2, 12)
    statics.append(br)
    br = objects.Bricks(height-16, 340, 2, 10)
    statics.append(br)
    br = objects.Bricks(height-18, 342, 2, 8)
    statics.append(br)
    br = objects.Bricks(height-20, 344, 2, 6)
    statics.append(br)
    br = objects.Bricks(height-22, 346, 2, 4)
    statics.append(br)
    br = objects.Bricks(height-24, 348, 2, 2)
    statics.append(br)

    f = objects.Pipe(height-28,357, 24, 1)
    statics.append(f)

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
    
    if(board.screen[x][y]!=' ' or board.screen[x][y+1]!=' ' or board.screen[x+1][y]!=' ' or board.screen[x+1][y+1]!=' ' ):
        fl = 0
    
    if(board.screen[x][y]==' ' and board.screen[x][y]==' ' and board.screen[x+2][y]==' ' and board.screen[x+2][y]==' '):
        fl = 0

    if(fl):
        ene = enemy.Enemy(x,y,1)
        en.append(ene)
    else:
        spawn_enemy()

start = time.time()
dooms = start   
make_scene()
spawn_enemy()
make_objects()
make_coins()
bidi.initialize()
config.set_scene(bidi,scene,statics)
config.set_coins(cns)
bidi.set_score(playboy,dooms)
#os.system('clear')

prev = -1 


getch = config.GetchUnix()
#doi = subprocess.Popen(['mplayer', 'mario_08.wav'])
doi = 1
#os.system('clear')
#os.system("start /home/zegatron/MONSOON18/MARIO_TILL_KILLS/resources/main_theme.ogg")
#time.sleep(2)
while(True):
    
#''' this part moves the enemy after every half second , checks player status ,enemy status ,initializes , sets player and enemies
#   '''
    if(time.time() - start > .5):
        start = time.time()
        if(len(en) < 2):
            spawn_enemy()
        for eni in en:
            eni._move_enemy(eni.xc,eni.yc,playboy.yc)
            playboy._check_player_alive(dooms,bidi,doi)
            chk = eni._check_enemy_alive(playboy)
            if(board.screen[eni.xc+2][eni.yc]==' ' and board.screen[eni.xc+2][eni.yc]==' '):
                en.remove(eni)
            if(chk):
                en.remove(eni)

        bidi.initialize()
        config.set_scene(bidi,scene,statics)
        config.set_coins(cns)
        bidi.set_score(playboy,dooms)
        playboy.set_player(playboy.xc, playboy.yc)
        for eni in en:
            eni.set_enemy(eni.xc, eni.yc)
        os.system('clear')
        bidi.render(playboy,en)

#''' takes user input and does the functionality accordingly '''
    inp = config.input_char()
    if(inp == 'a'):
        #print("a")
        if board.screen[playboy.xc+2][playboy.yc-1] == " " and board.screen[playboy.xc+2][playboy.yc] == " ":
            playboy.jump(playboy,bidi,prev, en, statics, scene, cns,2,doi,dooms)
        else:
            playboy.move_left(bidi)
        prev = 0
    elif(inp == 'd'):
        #print("d")
        if board.screen[playboy.xc+2][playboy.yc+1] == " " and board.screen[playboy.xc+2][playboy.yc+2] == " ":
            playboy.jump(playboy,bidi,prev, en, statics, scene, cns,3,doi,dooms)
        else:
            playboy.move_right(bidi)
        prev = 1
    elif(inp == 'w'):
        #print("w")
        do = subprocess.Popen(['aplay', 'mb_jump.wav'])
        os.system('clear')
        playboy.jump(playboy,bidi,prev, en, statics, scene, cns,1,doi,dooms)
        prev = -1

    if(inp == 'q'):
        #print("q")
        #os.killpg(os.getpgid(doi.pid), signal.SIGTERM)
        sys.exit(0)

    for i in range(0,2):
        for j in range(0,2):
            x = playboy.xc + i
            y = playboy.yc + j
            if(board.screen[x][y] == '0'):
                do = subprocess.Popen(['aplay', 'mb_coin.wav'])
                os.system('clear')
                playboy.coins = playboy.coins+1
                for coin in cns:
                    if(coin.xc == x and coin.yc == y):
                        cns.remove(coin)
    
#''' after input the positions change , we need to reset the board , set the new positions of player ,enemy ,, clear screen ,and print board'''
    bidi.initialize()
    config.set_scene(bidi,scene,statics)   
    
    bidi.set_score(playboy,dooms)
    config.set_coins(cns)
    
    playboy.set_player(playboy.xc, playboy.yc)
    for eni in en:
        check = eni._check_enemy_alive(playboy)
        if(check):
            en.remove(eni)
            
    for eni in en:
        eni.set_enemy(eni.xc, eni.yc)
    os.system('clear')
    bidi.render(playboy,en)

    if(360 - (round(time.time()-dooms)) < 0):
        os.system('clear')
        print('OUT OF TIME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        time.sleep(1)
        playboy.check_game_over(dooms,doi)

    if(playboy.yc >= 357):
        os.system('clear')
        print('HOOOOOOOOOOOOOOORAY!!!!!!!')
        print('YOUUUUUUUUUUUUUUUUUUUUUUUUUUU WON!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        time.sleep(1)
        playboy.check_game_over(dooms,doi)
        

