import board
import player
import time
import enemy
class Objects:

    def __init__(self,xc,yc,l,w):

        self.xc = xc
        self.yc = yc
        self.length = l
        self.width = w
    
    def draw(self):
        for i in range(self.length):
            for j in range(self.width):
                bd.buff[self.xc+i][self.yc+j] = 'O'
    
class Cloud(Objects):

    def __init__(self,xc,yc,l,w):
        Objects.__init__(self,xc,yc,l,w)    

    def draw(self):
        for i in range (self.xc,self.xc+self.length):
            for j in range (self.yc,self.yc+self.width):
                if i==self.xc and j==self.yc:
                    board.screen[i][j]=' '
                elif i==self.xc and j==self.yc+self.width-1:
                    board.screen[i][j]=' '
                elif i==self.xc+self.length-1 and j==self.yc:
                    board.screen[i][j]=' '
                elif i==self.xc+self.length-1 and j==self.yc+self.width-1:
                    board.screen[i][j]=' ' 
                else:
                    board.screen[i][j]='c'


class Hills(Objects):
    def __init__(self, xc, yc, l, w, typ):
        Objects.__init__(self, xc, yc, l, w)
        self.typ = typ

    def draw(self):
        if (self.typ == 1):
            board.screen[self.xc][self.yc] = "+"
            board.screen[self.xc-1][self.yc+1] = "+"
            board.screen[self.xc-2][self.yc+2] = "+"
            board.screen[self.xc-3][self.yc+3] = "+"
           
            
            
            board.screen[self.xc-3][self.yc+4] = "+"
            board.screen[self.xc-3][self.yc+5] = "+"
            board.screen[self.xc-3][self.yc+6] = "+"
            board.screen[self.xc-3][self.yc+7] = "+"
            board.screen[self.xc-2][self.yc+8] = "+"
            board.screen[self.xc-1][self.yc+9] = "+"
            board.screen[self.xc][self.yc+10] = "+"
            
        elif(self.typ == 2):
            board.screen[self.xc][self.yc] = "/"
            board.screen[self.xc-1][self.yc+1] = "/"
            board.screen[self.xc-2][self.yc+2] = "/"

            # board.screen[self.xc-2][self.yc+3] = 'U'
            # board.screen[self.xc-2][self.yc+4] = "U"
            # board.screen[self.xc-2][self.yc+5] = "U"

            # board.screen[self.xc-3][self.yc+3] = '^'
            # board.screen[self.xc-3][self.yc+4] = '^'
            # board.screen[self.xc-3][self.yc+5] = '^'

            board.screen[self.xc-3][self.yc+3] = '_'
            board.screen[self.xc-3][self.yc+4] = '_'
            board.screen[self.xc-3][self.yc+5] = '_'


            board.screen[self.xc-2][self.yc+6] = "\\"
            board.screen[self.xc-1][self.yc+7] = "\\"
            board.screen[self.xc][self.yc+8] = "\\"
        
        else:
            board.screen[self.xc][self.yc] = "/"
            board.screen[self.xc-1][self.yc+1] = "/"
            board.screen[self.xc-2][self.yc+2] = "/"

            board.screen[self.xc-2][self.yc+3] = "\\"
            board.screen[self.xc-1][self.yc+4] = "\\"
            board.screen[self.xc][self.yc+5] = "\\"
        
class Bricks(Objects):
    def __init__(self, xc, yc, l, w):
        Objects.__init__(self, xc, yc, l, w)

    def draw(self):
        for i in range(self.length):
            for j in range(self.width):
                board.screen[self.xc + i][self.yc + j] = 'X'

class Pipe(Objects):
    def __init__(self, xc, yc, l, w):
        Objects.__init__(self, xc, yc, l, w)

    def draw(self):
        for i in range(self.length):
            for j in range(self.width):
                if(j==0 or j==self.width-1):
                    board.screen[self.xc + i][self.yc + j] = '|'
                else:
                    board.screen[self.xc+i][self.yc+j] = '-'
        for i in range (self.width):
            board.screen[self.xc-1][self.yc+i] = '_'

class Holes(Objects):
    def __init__(self, xc, yc, l, w):
        Objects.__init__(self, xc, yc, l, w)

    def draw(self):
        for i in range(self.length):
            for j in range(self.width):
                board.screen[self.xc + i][self.yc + j] = ' '

class Coins(Objects):
    def __init__(self, xc, yc, l, w):
        Objects.__init__(self, xc, yc, l, w)

    def draw(self):
        board.screen[self.xc][self.yc] = '0'

    def check_coin(self):
        print(self.xc,self.yc)
        time.sleep(.04)
        if(board.screen[self.xc][self.yc-1]=='M' or board.screen[self.xc-1][self.yc]=='M' or  board.screen[self.xc-1][self.yc-1]=='M'):
            print(self.xc,self.yc,"if ke andar")
            time.sleep(.4)
            board.screen[self.xc][self.yc] = ' '
            return 1
        return 0       
    
                    
    
                    