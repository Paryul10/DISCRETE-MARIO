#from colorama import Fore , Back ,Style
#import colors
import random
screen = [[' ' for x in range(910)] for y in range(40)]
class Board:

    def __init__(self,height,width):

        self.height = height
        self.width = width
        self.left = 0
        self.right = width
        self.initialize()

    def initialize(self):
    
        for i in range (self.height):
            for j in range (self.left+self.width):
                if i==0 or i > self.height-5:
                    screen[i][j]="*"
                elif j==0 or j==self.left+self.width-1:
                    screen[i][j]='*'
                else:
                    screen[i][j]=' '

        
        screen[self.height-27][356] = '_'
        screen[self.height-27][355] = '/'
        screen[self.height-28][356] = '/'
        screen[self.height-29][357] = '|'

    def set_score(self,playboy):

        screen[1][self.left+35] = 'K'
        screen[1][self.left+36] = 'I'
        screen[1][self.left+37] = 'L'
        screen[1][self.left+38] = 'L'
        screen[1][self.left+39] = 'S'

        screen[1][self.left+40] = ':'
        screen[1][self.left+41] = playboy.kills

        screen[1][self.left+51] = 'C'
        screen[1][self.left+52] = 'O'
        screen[1][self.left+53] = 'I'
        screen[1][self.left+54] = 'N'
        screen[1][self.left+55] = 'S'

        screen[1][self.left+56] = ':'
        screen[1][self.left+57] = playboy.score
        screen[1][self.left+48] = ':'
        screen[1][self.left+49] = playboy.health

        screen[1][self.left+43] = 'L'
        screen[1][self.left+44] = 'I'
        screen[1][self.left+45] = 'V'
        screen[1][self.left+46] = 'E'
        screen[1][self.left+47] = 'S'

    def render(self,playboy,en):

        # if(playboy.yc<=self.left+15):
        #     self.left-=1
        if(playboy.yc>=self.left+(3/4)*self.width):
            self.left+=1
        
        for eni in en:
            if(eni.yc < self.left):
                en.remove(eni)
            
        for i in range (self.height):
            for j in range (self.left,self.left+self.width):
                if(screen[i][j]=='*'):
                    print("\033[1;32;40m" + screen[i][j],end=' ')
                elif(screen[i][j]=='M'):
                    print("\033[1;36;40m" +screen[i][j],end =' ')
                elif(screen[i][j]=='c'):
                    print("\033[1;34;40m" +screen[i][j],end =' ')
                elif(screen[i][j]=='e'):
                    print("\033[1;31;40m" +screen[i][j],end =' ')
                elif(screen[i][j]=='+' or screen[i][j]=='/' or screen[i][j]=='\\' or screen[i][j]=='_'):
                    print("\033[1;37;40m" +screen[i][j],end =' ')
                elif(screen[i][j]=='X'):
                    print("\033[1;33;40m" +screen[i][j],end =' ')
                else:
                    print(screen[i][j],end =' ')
            print()
