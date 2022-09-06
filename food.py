import pygame
from random import randrange
class Food:
    def __init__(self,start_pos_x,start_pos_y):

        self.food_color = (25,255,25)

        self.block_width = 30
        self.block_height = 30
        self.food = pygame.Rect(start_pos_x,start_pos_y,self.block_width,self.block_height)


        
        self.apple = pygame.image.load("assets/apple.png").convert_alpha()
        self.apple = pygame.transform.scale(self.apple,(self.block_width,self.block_height))


    #generatings a random position for  the food.

    def relocateFood(self):
        new_x = randrange(30,330,self.block_width)
        new_y = randrange(30,330,self.block_height)
        self.food.left = new_x
        self.food.top = new_y

   
