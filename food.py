
from block import Block
from random import randrange
class Food(Block):
    def __init__(self,block_size:int):
        super().__init__(block_size)

    def LocateFood(self,screen_size:tuple):
        self.left = randrange(0,screen_size[0],self.BlockSize)
        self.top = randrange(0,screen_size[1],self.BlockSize)

   
