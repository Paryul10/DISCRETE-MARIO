import board,signal
import os ,sys,subprocess
import time
import enemy
from person import *
import enemy
import config
#from colorama import Back ,Fore ,Style
#pylint: disable-msg=R0913


class Mario(Person):

    def __init__(self,xc,yc,isalive):

        Person.__init__(self,xc,yc,isalive)
        self.health = 3
        self.coins = 0
        self.kills = 0 #0 represents small mario
        self.score = 0

    #####################--------------------------------MOVEMENTS-PLAYER-----------------################################
    def move_player(self,changex,changey,bidi):
        
        #if(self.xc < 28 and self.xc > 1):
        self.xc+=changex
        self.yc+=changey
        # if(self.yc < bidi.left):
        #     self.yc = bidi.left

    ''' 
        ENEMIES ALSO MOVE WHILE THE PLAYER JUMPS , SO ACCORDINGLY THE CODE
    '''
    def jump(self , bidi , prev,en,playboy,dooms,scene,statics,cns,doi):
        
        speedx = 4
        speedy = 1
        self.xc = self.xc - speedx

        start = time.time()
        
        # bidi.initialize()
        # config.set_scene(bidi,scene,statics)
        # config.set_coins(cns)        
        # bidi.set_score(playboy)
        # self.set_player(self.xc,self.yc)
        # os.system('clear')
        # bidi.render(playboy,en)

        while(self.xc < self.orgx):
            
            if(time.time() - start > .5):
                start = time.time()
                for enemy in en:
                    enemy.move_enemy(enemy.xc,enemy.yc, playboy.yc)
                    self.check_player_alive(dooms,bidi,doi)
                    chek = enemy.check_enemy_alive(self)
                    if(chek == 1):
                        #do = subprocess.Popen(['aplay', 'mb_touch.wav'])                        
                        en.remove(enemy)
            
            # for coin in coins:
            #     k = coin.check_coin()
            #     if(k):
            #         coins.remove(coin)

            speedx = speedx - 1            
            self.xc = self.xc - speedx

            if(prev == 0):
                self.yc = self.yc - speedy
            elif(prev == 1):
                self.yc = self.yc + speedy
            


            
            for i in range(0,2):
                for j in range(0,2):
                    x = playboy.xc + i
                    y = playboy.yc + j
                    if(board.screen[x][y] == '0'):
                        playboy.coins = playboy.coins+1
                        for coin in cns:
                            if(coin.xc == x and coin.yc == y):
                                cns.remove(coin)
            bidi.initialize()
            config.set_scene(bidi,scene,statics)
            config.set_coins(cns)        
            bidi.set_score(playboy)
            self.set_player(self.xc,self.yc)
            for enemy in en:
                enemy.set_enemy(enemy.xc,enemy.yc)
            os.system('clear')
            bidi.render(playboy,en)
            time.sleep(.05)
            
    ###############################------------------POSITIONING---------------------------##############################
    def update_player_pos(self, xpos,ypos):
        for i in range(0,2):
            for j in range(0,2):
                board.screen[xpos+i][ypos+j] = ' '

    def set_player(self,xc,yc):     
        for i in range(0,2):
            for j in range(0,2):
                board.screen[xc+i][yc+j] = 'M'
    ######################---------------------------------IS_PLAYER_ALIVE/IS_GAME_OVER--------------########################
    def check_player_alive(self,dooms,bidi,doi):
        chk = 0
        if(board.screen[self.xc][self.yc] == 'e' and board.screen[self.xc+1][self.yc] == 'e'):
            chk = chk + 1
        if(board.screen[self.xc][self.yc+1] == 'e' and board.screen[self.xc+1][self.yc+1] == 'e'):
            chk = chk + 1

        if(chk>=1):
            #do = subprocess.Popen(['aplay', 'mb_die.wav']) 
            #os.killpg(os.getpgid(doi.pid), signal.SIGTERM)
            #doi = subprocess.Popen(['mplayer', 'mario_08.wav'])
            print(self.health)
            self.reduce_life(dooms,bidi,doi)
        return

    def reduce_life(self,dooms,bidi,doi):
        if(self.health > 0):
            self.health = self.health -1
        if(self.health >0):
            #print(self.orgx,self.orgy)
            #time.sleep(1)
            self.xc = self.orgx 
            self.yc = self.orgy + bidi.left
        elif self.health == 0:
            self.check_game_over(dooms,doi)

    def check_game_over(self,dooms,doi):
            #os.killpg(os.getpgid(doi.pid), signal.SIGTERM)
            os.system('clear')
            print('GAME OVER!!!!!!!!!!!!!!!!!!')
            print('TOTAL_SCORE=',self.score)
            print('TIME ALIVE=',time.time()-dooms)
            sys.exit(0)

    
    
            

        

        
        
        




