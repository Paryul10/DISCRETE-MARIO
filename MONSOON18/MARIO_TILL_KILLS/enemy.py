from person import *
import board
import time
import player
import random,os
import subprocess

'''
THE ENEMY INHERITS FROM THR PERSON CLASS , coordinates and alive status
'''
class Enemy(Person):

    def ___init__(self,xc,yc,isalive):
        Person.__init__(self,xc,yc,isalive)
        self.espeedy = 0

    ###################################---------------------MOVEMENTS----------------------------##########################
    ''' 
    IN THESE FUNCTIONS I TRY TO CONTROL THE MOVEMENT(RANDOM) OF THE ENEMY . AND ALSO CHECK IF POSITIONING IS ALLOWED
    '''
    def check_empty(self,xc,yc,direction):
        
        c1 = 0
        c2 = 0
        if(board.screen[xc][yc]==' ' or board.screen[xc][yc]=='M' or board.screen[xc][yc]=='+' or board.screen[xc][yc]=='/' or board.screen[xc][yc]== '\\' ):
            c1 = c1+1
        if(board.screen[xc+1][yc]==' ' or board.screen[xc+1][yc]=='M'  or board.screen[xc+1][yc]=='+'  or board.screen[xc+1][yc]=='/' or board.screen[xc+1][yc]=='\\'):
            c1 = c1+1

        if(board.screen[xc][yc+1]==' ' or board.screen[xc][yc+1]=='M' or board.screen[xc][yc+1]=='+' or board.screen[xc][yc+1]=='/' or board.screen[xc][yc+1]=='\\'):
            c2 = c2+1
        if(board.screen[xc+1][yc+1]==' ' or board.screen[xc+1][yc+1]=='M' or board.screen[xc+1][yc+1]=='+' or board.screen[xc+1][yc+1]=='/'or board.screen[xc+1][yc+1]=='\\'):
            c2 = c2+1
        
        if(direction == -1 and c1 == 2):
            return 1
        
        if(direction == 1 and c2 == 2):
            return 1

    def check_movement_left(self,xc,yc):        
        #print('chk_move_left\n')
        #time.sleep(1)
        checking_left = self.check_empty(xc,yc,-1)
        return checking_left

    def check_movement_right(self,xc,yc):
        #print('chk_move_right\n')
        #time.sleep(1)
        checking_right = self.check_empty(xc,yc,1)
        return checking_right
 
    def move_enemy(self,xc,yc,playery):
        
        if(self.yc > playery):
            #print('entered')
            #time.sleep(1)
            if(self.yc- playery > 20):
                self.espeedy = 3
            else:
                self.espeedy = 1
            nx = self.xc
            nyl = self.yc - self.espeedy
            self.enemy_update(self.xc,self.yc)
            #self.set_enemy(nx,nyl)
            nyr = self.yc + 1
            check_left_move = self.check_movement_left(nx,nyl)
            check_right_move = self.check_movement_right(nx,nyr)
            if(check_left_move):
                #print('check1')
                self.set_enemy(nx,nyl)
            elif(check_right_move):
                self.set_enemy(nx,nyr)
                
        elif(self.yc < playery):
            nx = self.xc
            if(abs(self.yc- playery) > 20):
                self.espeedy = 3
            else:
                self.espeedy = 1
            nyl = self.yc - 1
            nyr = self.yc + self.espeedy
            self.enemy_update(self.xc,self.yc)
            check_left_move = self.check_movement_left(nx,nyl)
            check_right_move = self.check_movement_right(nx,nyr)
            if(check_right_move):
                #print('check1')
                self.set_enemy(nx,nyr)
            elif(check_left_move):
                self.set_enemy(nx,nyl)

    ######################################---------------------------------POSITIONING-----------------------------##############
    '''
    THESE FUNCTIONS SET THE ENEMY ON THE BOARD AND REMOVE IT'S PAST EXISTENCE
    '''
    def enemy_update(self,oxc,oyc):
        
        for i in range(0,2):
            for j in range(0,2):
                board.screen[oxc+i][oyc+j] = ' '

    def set_enemy(self,xc,yc):

        self.xc = xc
        self.yc = yc 
        for i in range(0,2):
            for j in range(0,2):
                board.screen[xc+i][yc+j] = 'e'

    ###############################-------------------------------COLLISION----------------------------------###################

    def check_enemy_alive(self,playboy):
        check = 0
        if(board.screen[self.xc][self.yc] == 'M' or board.screen[self.xc][self.yc+1]=='M'):
            check = check + 1
            self.isalive = 0
            playboy.kills = playboy.kills + 1
        if(check > 0):
            do = subprocess.Popen(['aplay', 'mb_touch.wav'])
            return 1
        return 0
    
    ###########################------------------------------SPAWN_ENEMY-------------------------------######################   
