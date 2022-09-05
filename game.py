import pygame

from snake import Snake
import time

pygame.init()


from food import Food
class Game:
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 500

        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.snake_area = pygame.Surface((self.screen_width*0.8,self.screen_height*0.8))



        self.snake = Snake(120,120)

        self.food = Food(60,60)

        self.font = pygame.font.SysFont('ubuntumono',size=20,bold=True,italic=False)
        self.font_color = (255,255,255)







    

    def drawSnake(self):
        #draw every element, the first one is the head so the color is different
        for index,element in enumerate(self.snake.snake):
            #pygame.draw.rect(self.snake_area,self.snake.body_color,element,border_radius=1)

            '''
            if index > 1:
                pygame.draw.rect(self.snake_area,self.snake.body_color,element,border_radius=1)
            
            if index == 0:
                pygame.draw.rect(self.snake_area,self.snake.head_color,element,border_radius=1)
            else:
                pygame.draw.rect(self.snake_area,self.snake.body_color,element,border_radius=1)
            '''
        #self.snake_area.blit(self.snake.graphics[0]["graphic"],self.snake.graphics[0]["pos"])
        for graphic in self.snake.graphics:
            self.snake_area.blit(graphic["graphic"],graphic['pos'])
    #food.
    def drawFood(self):
        pygame.draw.rect(self.snake_area,self.food.food_color,self.food.food)

        self.snake_area.blit(self.food.apple,self.food.food)


    #starting the game
    def startGame(self):
        self.__startGame()



    #checking if the location of the head is inside the rectangle

    def checkIfOutOfScreen(self):

        if self.snake.head.left > self.snake_area.get_width() or self.snake.head.left < 0:
            return True
        return self.snake.head.top > self.snake_area.get_height() or self.snake.head.top < 0
    

    #the actual game

    def __startGame(self):
        self.snake.initSnake()
        while True:



            if self.checkIfOutOfScreen():
                self.screen.blit(self.font.render("Oops!, saliste del area",True,(255,255,255)),(100,250))
                pygame.display.update()
                pygame.time.delay(3000)
                self.snake.initSnake()
                self.food.relocateFood()

            #checking if the snake colide with itself
            if self.snake.checkSelfCollide():
                self.screen.blit(self.font.render("Oops!, te chocaste contigo mismo",True,(255,255,255)),(80,250))
                pygame.display.update()
                pygame.time.delay(3000)
                self.snake.initSnake()
                self.food.relocateFood()
            #checking if the snake colide with food.
            if self.snake.checkCollision(self.food.food.copy()):
                self.snake.Eat(self.food.food.copy())
                self.food.relocateFood()
            


            #checking if events to set the direction of the snake
            for event in pygame.event.get():
                if event.type == pygame.QUIT: exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake.moveLeft()
                    elif event.key == pygame.K_RIGHT:
                        self.snake.moveRight()
                    elif event.key == pygame.K_UP:
                        self.snake.moveUp()
                    elif event.key == pygame.K_DOWN:
                        self.snake.moveDown()



            #moving the snake
            self.snake.move()
            self.snake.snakeGraphics()

            #setting the background collor.
            self.snake_area.fill((25,25,25))
            self.screen.fill((0,0,0))

            #drawings elements
            self.drawSnake()   
            self.drawFood()
            

            #drawing the area and texts
            self.screen.blit(self.snake_area,(45,60))

            self.screen.blit(self.font.render("Snake Game",False,self.font_color),(self.screen_width*0.5-60,30))

            self.screen.blit(self.font.render(f"Food: {self.snake.snake_size}",False,self.font_color),(45,30))

            


            pygame.time.Clock().tick(13)
            pygame.display.update()
    
        time.sleep(3)
    
    

game = Game()

game.startGame()
