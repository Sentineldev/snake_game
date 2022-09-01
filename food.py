import pygame
from random import randrange
class Food:
    def __init__(self,start_pos_x,start_pos_y):

        self.food_color = (25,255,25)

        self.block_width = 13
        self.block_height = 13

        self.food = pygame.Rect(start_pos_x,start_pos_y,self.block_width,self.block_height)

    


    #generatings a random position for  the food.

    def relocateFood(self):
        new_x = randrange(13,300,self.block_width)
        new_y = randrange(13,300,self.block_height)
        self.food.left = new_x
        self.food.top = new_y