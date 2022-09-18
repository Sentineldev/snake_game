import pygame
pygame.init()
class Block(pygame.Rect):
    def __init__(self,block_size:int,startPosX=None,startPosY=None):
        self.__block_size = block_size
        self.__block_color = (255,255,255)

        if startPosX == None and startPosY == None :
            super().__init__(0,0,self.__block_size,self.__block_size)
        else:
            super().__init__(startPosX,startPosY,self.__block_size,self.__block_size)



    
    
    @property
    def BlockColor(self) -> tuple:
        return self.__block_color
    @property
    def BlockSize(self) -> int:
        return self.__block_size

    def setBlockColor(self,color:tuple):
        self.__block_color = tuple(color)