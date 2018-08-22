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
        self._health = 3
        self.coins = 0
        self.kills = 0 #0 represents small mario
        self.score = 0

    #####################--------------------------------MOVEMENTS-PLAYER-----------------################################
    
        
        #if(self.xc < 28 and self.xc > 1):
        
        # if(self.yc < bidi.left):
        #     self.yc = bidi.left
    def move_left(self, bidi):
        if (self.yc >= (bidi.left+7)):
            if board.screen[self.xc][self.yc-1] == " " or board.screen[self.xc][self.yc-1] == "/" or board.screen[self.xc][self.yc-1] == "\\" or board.screen[self.xc][self.yc-1] == "c" or board.screen[self.xc][self.yc-1] == "0" or board.screen[self.xc][self.yc-1] == "+":
                self.yc = self.yc -1
    
    def move_right(self,bidi):
        if (self.yc <= (bidi.left+(3/4)*bidi.width)):
            if board.screen[self.xc][self.yc+2] == " " or board.screen[self.xc][self.yc+2] == "/" or board.screen[self.xc][self.yc+2] == "\\" or board.screen[self.xc][self.yc+2] == "c" or board.screen[self.xc][self.yc+2] == "0" or board.screen[self.xc][self.yc+2] == "+":
                self.yc = self.yc + 1


    ''' 
        ENEMIES ALSO MOVE WHILE THE PLAYER JUMPS , SO ACCORDINGLY THE CODE
    '''
    # def jump(self , bidi , prev,en,playboy,dooms,scene,statics,cns,doi):
        
    #     speedx = 4
    #     speedy = 1
    #     self.xc = self.xc - speedx

    #     start = time.time()
        
    #     # bidi.initialize()
    #     # config.set_scene(bidi,scene,statics)
    #     # config.set_coins(cns)        
    #     # bidi.set_score(playboy)
    #     # self.set_player(self.xc,self.yc)
    #     # os.system('clear')
    #     # bidi.render(playboy,en)

    #     while(self.xc < self.orgx):
            
    #         if(time.time() - start > .5):
    #             start = time.time()
    #             for enemy in en:
    #                 enemy._move_enemy(enemy.xc,enemy.yc, playboy.yc)
    #                 self._check_player_alive(dooms,bidi,doi)
    #                 chek = enemy._check_enemy_alive(self)
    #                 if(chek == 1):
    #                     #do = subprocess.Popen(['aplay', 'mb_touch.wav'])                        
    #                     en.remove(enemy)
            
    #         # for coin in coins:
    #         #     k = coin.check_coin()
    #         #     if(k):
    #         #         coins.remove(coin)

    #         speedx = speedx - 1            
    #         self.xc = self.xc - speedx

    #         if(prev == 0):
    #             self.yc = self.yc - speedy
    #         elif(prev == 1):
    #             self.yc = self.yc + speedy
    def jump(self, playboy,bidi, prev,en, statics, scene, cns,fle,doi,dooms):
        speedx = 2
        speedy = 0
        if(fle == 2):
            speedx = -2
            speedy = -1
        if(fle == 3):
            speedx = -2
            speedy = 1
            
        
        flag = 0
        xt = self.orgx
        xt += 1
        xi = self.xc
        while (self.xc < xt):
            inp = config.input_char_jump()
            if inp == "d":
                if self.yc < bidi.left+(3/4)*bidi.width:
                    speedy = 1
                else:
                    speedy = 0
            if inp == "a":
                if self.yc > bidi.left+7:
                    speedy = -1
                else:
                    speedy = 0
            if inp == "q":
                sys.exit(0)
            
            if self.xc < xi - 10 or flag == 2:
                speedx = -2

            if speedx < 0:
                if speedy == 0:
                    if board.screen[self.xc+2][self.yc] == "X" or board.screen[self.xc+2][self.yc] == "-" or board.screen[self.xc+2][self.yc] == "|":
                        speedx = 0
                        speedy = 0
                        flag = 1
                    elif board.screen[self.xc+3][self.yc] == "X" or board.screen[self.xc+3][self.yc] == "-" or board.screen[self.xc+3][self.yc] == "|" or board.screen[self.xc+3][self.yc] == "*":
                        speedx = -1
                        speedy = 0
                        flag = 1
                    elif board.screen[self.xc+2][self.yc+1] == "X" or board.screen[self.xc+2][self.yc+1] == "-" or board.screen[self.xc+2][self.yc+1] == "|":
                        speedx = 0
                        speedy = 0
                        flag = 1
                    elif board.screen[self.xc+3][self.yc+1] == "X" or board.screen[self.xc+3][self.yc+1] == "-" or board.screen[self.xc+3][self.yc+1] == "|" or board.screen[self.xc+3][self.yc+1] == "*":
                        speedx = -1
                        speedy = 0
                        flag = 1
                elif speedy > 0:
                    if board.screen[self.xc+2][self.yc+1] == "X" or board.screen[self.xc+2][self.yc+1] == "-" or board.screen[self.xc+2][self.yc+1] == "|":
                        speedx = 0
                        speedy = 0
                        flag = 1
                    elif board.screen[self.xc+3][self.yc+1] == "X" or board.screen[self.xc+3][self.yc+1] == "-" or board.screen[self.xc+3][self.yc+1] == "|" or board.screen[self.xc+3][self.yc+1] == "*":
                        speedx = -1
                        speedy = 1
                        flag = 1
                    elif board.screen[self.xc+2][self.yc+2] == "X" or board.screen[self.xc+2][self.yc+2] == "-" or board.screen[self.xc+2][self.yc+1] == "|":
                        speedx = -2
                        speedy = 0
                        flag = 0
                    elif board.screen[self.xc+3][self.yc+2] == "X" or board.screen[self.xc+3][self.yc+2] == "-" or board.screen[self.xc+3][self.yc+2] == "|" or board.screen[self.xc+3][self.yc+2] == "*":
                        speedx = -2
                        speedy = 0
                        flag = 0
                else:
                    if board.screen[self.xc+2][self.yc] == "X" or board.screen[self.xc+2][self.yc] == "-" or board.screen[self.xc+2][self.yc] == "|":
                        speedx = 0
                        speedy = 0
                        flag = 1
                    elif board.screen[self.xc+3][self.yc] == "X" or board.screen[self.xc+3][self.yc] == "-" or board.screen[self.xc+3][self.yc] == "|" or board.screen[self.xc+3][self.yc] == "*":
                        speedx = -1
                        speedy = -1
                        flag = 1
                    elif board.screen[self.xc+2][self.yc-1] == "X" or board.screen[self.xc+2][self.yc-1] == "-" or board.screen[self.xc+2][self.yc-1] == "|":
                        speedx = -2
                        speedy = 0
                        flag = 0
                    elif board.screen[self.xc+3][self.yc-1] == "X" or board.screen[self.xc+3][self.yc-1] == "-" or board.screen[self.xc+3][self.yc-1] == "|" or board.screen[self.xc+3][self.yc-1] == "*":
                        speedx = -2
                        speedy = 0
                        flag = 0

            elif speedx > 0:
                if speedy == 0:
                    if board.screen[self.xc-1][self.yc] == "X" or board.screen[self.xc-1][self.yc] == "-" or board.screen[self.xc-1][self.yc] == "|":
                        speedx = 0
                        speedy = 0
                        flag = 2
                    elif board.screen[self.xc-2][self.yc] == "X" or board.screen[self.xc-2][self.yc] == "-" or board.screen[self.xc-2][self.yc] == "|":
                        speedx = 1
                        speedy = 0
                        flag = 2
                    elif board.screen[self.xc-1][self.yc+1] == "X" or board.screen[self.xc-1][self.yc+1] == "-" or board.screen[self.xc-1][self.yc+1] == "|":
                        speedx = 0
                        speedy = 0
                        flag = 2
                    elif board.screen[self.xc-2][self.yc+1] == "X" or board.screen[self.xc-2][self.yc+1] == "-" or board.screen[self.xc-2][self.yc+1] == "|":
                        speedx = 1
                        speedy = 0
                        flag = 2
                elif speedy > 0:
                    if board.screen[self.xc-1][self.yc+1] == "X" or board.screen[self.xc-1][self.yc+1] == "-" or board.screen[self.xc-1][self.yc+1] == "|":
                        speedx = 0
                        speedy = 0
                        flag = 2
                    elif board.screen[self.xc-2][self.yc+1] == "X" or board.screen[self.xc-2][self.yc+1] == "-" or board.screen[self.xc-2][self.yc+1] == "|":
                        speedx = 1
                        speedy = 1
                        flag = 2
                    elif board.screen[self.xc-1][self.yc+2] == "X" or board.screen[self.xc-1][self.yc+2] == "-" or board.screen[self.xc-1][self.yc+2] == "|":
                        speedx = 2
                        speedy = 0
                        flag = 0
                    elif board.screen[self.xc-2][self.yc+2] == "X" or board.screen[self.xc-2][self.yc+2] == "-" or board.screen[self.xc-2][self.yc+2] == "|":
                        speedx = 2
                        speedy = 0
                        flag = 0
                else:
                    if board.screen[self.xc-1][self.yc] == "X" or board.screen[self.xc-1][self.yc] == "-" or board.screen[self.xc-1][self.yc] == "|":
                        speedx = 0
                        speedy = 0
                        flag = 2
                    elif board.screen[self.xc-2][self.yc] == "X" or board.screen[self.xc-2][self.yc] == "-" or board.screen[self.xc-2][self.yc] == "|":
                        speedx = 1
                        speedy = -1
                        flag = 2
                    elif board.screen[self.xc-1][self.yc-1] == "X" or board.screen[self.xc-1][self.yc-1] == "-" or board.screen[self.xc-1][self.yc-1] == "|":
                        speedx = 2
                        speedy = 0
                        flag = 0
                    elif board.screen[self.xc-2][self.yc-1] == "X" or board.screen[self.xc-2][self.yc-1] == "-" or board.screen[self.xc-2][self.yc-1] == "|":
                        speedx = 2
                        speedy = 0
                        flag = 0

            self.xc = self.xc - speedx
            self.yc = self.yc + speedy

            xt = self.orgx
        
            if(self.xc >= bidi.height - 6 ):
                if(board.screen[self.xc+2][self.yc]== ' ' and board.screen[self.xc+2][self.yc+1]==' '):
                    self.reduce_life(dooms,bidi,doi)
                #self.reduce_life(dooms,bidi,doi)
            


            
            for i in range(0,2):
                for j in range(0,2):
                    x = playboy.xc + i
                    y = playboy.yc + j
                    if(board.screen[x][y] == '0'):
                        do = subprocess.Popen(['aplay', 'mb_coin.wav'])
                        playboy.coins = playboy.coins + 1
                        for coin in cns:
                            if(coin.xc == x and coin.yc == y):
                                cns.remove(coin)
            
            bidi.initialize()
            config.set_scene(bidi,scene,statics)
            config.set_coins(cns)        
            bidi.set_score(playboy,dooms)
            self.set_player(self.xc,self.yc)
            for enemy in en:
                enemy.set_enemy(enemy.xc,enemy.yc)
            os.system('clear')
            bidi.render(playboy,en)
            time.sleep(.05)
        
            if flag == 1:
                break
            
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
    def _check_player_alive(self,dooms,bidi,doi):
        chk = 0
        if(board.screen[self.xc][self.yc] == 'e' and board.screen[self.xc+1][self.yc] == 'e'):
            chk = chk + 1
        if(board.screen[self.xc][self.yc+1] == 'e' and board.screen[self.xc+1][self.yc+1] == 'e'):
            chk = chk + 1

        if(chk>=1):
            #os.killpg(os.getpgid(doi.pid), signal.SIGTERM)
            #doi = subprocess.Popen(['mplayer', 'mario_08.wav'])
            print(self._health)
            self.reduce_life(dooms,bidi,doi)
        return

    def reduce_life(self,dooms,bidi,doi):
        do = subprocess.Popen(['aplay', 'mb_die.wav']) 
        os.system('clear')
        if(self._health > 0):
            self._health = self._health -1
        if(self._health >0):
            #print(self.orgx,self.orgy)
            #time.sleep(1)
            self.xc = self.orgx 
            for i in range (bidi.width):
                if(board.screen[self.xc][bidi.left+i]==' ' and board.screen[self.xc][bidi.left+i+1]==' '):
                    self.yc = i + bidi.left
        elif self._health == 0:
            self.check_game_over(dooms,doi)

    def check_game_over(self,dooms,doi):
            #os.killpg(os.getpgid(doi.pid), signal.SIGTERM)
            os.system('clear')
            print('GAME OVER!!!!!!!!!!!!!!!!!!')
            print('TOTAL_SCORE=',self.score+self.coins*10+self.kills*100+((360-(round(time.time()-dooms)))*10))
            print('TIME ALIVE=',round(time.time()-dooms))
            sys.exit(0)

    
    
            

        

        
        
        




