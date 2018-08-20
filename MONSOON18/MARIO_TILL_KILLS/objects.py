import board
import player
import enemy
class Objects:

    def __init__(self,xc,yc,l,w):

        self.xc = xc
        self.yc = yc
        self.length = l
        self.width = w
    
class Cloud(Objects):

    def __init__(self,xc,yc,l,w):
        Objects.__init__(self,xc,yc,l,w)

    def set_cloud():
        for i in range (xc,xc+l):
            for j in range (yc,yc+w):
                if i==xc and j==yc:
                    board.screen[i][j]=' '
                elif i==xc and j==yc+w-1:
                    board.screen[i][j]=' '
                elif i==xc+l-1 and j==yc:
                    board.screen[i][j]=' '
                elif i==xc+l-1 and j==yc+w-1:
                    board.screen[i][j]=' ' 
                else:
                    board.screen[i][j]='c'

        



    
    
     