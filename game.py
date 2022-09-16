
import pygame
from sys import exit
from snake import Snake
from food import Food
from sprite_sheet import SpriteSheet
from time import sleep

pygame.init()
pygame.font.init()




    






class SnakeArea(pygame.Surface):
    def __init__(self,block_size:int,block_num:int):
        self.__block_size = int(block_size)
        self.__block_num = int(block_num * 0.8) 
        self.__width = int((self.__block_size * self.__block_num))
        self.__height = int((self.__block_size * self.__block_num))
        self.__size = (self.__width,self.__height)
        self.__spritesheet = SpriteSheet()

        
        super().__init__(self.__size)   


        self.__food = Food(self.__block_size)
        self.__snake = Snake(self.__block_size)




    
    def initElements(self):
        self.__food.LocateFood(self.__size)
        self.__snake.initSnake()

    def setSheet(self,sheet:SpriteSheet):
        self.__spritesheet = sheet

    def RelocateFood(self):
        self.__food.LocateFood(self.__size)

    
    def checkIfOutOfScreen(self) -> bool:
        if self.__snake.SnakeHead.left >= self.__width or self.__snake.SnakeHead.left < 0:
            return True
        if self.__snake.SnakeHead.top >= self.__height or self.__snake.SnakeHead.top < 0:
            return True
        return False

    
    def __drawBackground(self):
        brown_grass = self.__spritesheet.getEnvironSprite("brown_grass_sprite",self.__block_size)
        green_grass = self.__spritesheet.getEnvironSprite("green_grass_sprite",self.__block_size)
        x = 0
        y = 0
        for  i in range(self.__block_num):
            for j in range(self.__block_num):
                
                if i == 0:
                    self.blit(brown_grass,(x,y))
                elif j == 0:
                    self.blit(brown_grass,(x,y))
                elif j == self.__block_num-1:
                    self.blit(brown_grass,(x,y))
                elif i == self.__block_num-1:
                    self.blit(brown_grass,(x,y))
                else:
                    self.blit(green_grass,(x,y))
                x+=self.__block_size
            x = 0
            y+=self.__block_size 

    
    def __drawFood(self):
       
        apple = self.__spritesheet.getSprite("food_apple",self.__block_size)
        
        self.blit(apple,(self.__food.left,self.__food.top))

    def __drawSnake(self):
        
        for index in range(self.__snake.Length):
            if index == 0:
                
                #seeting head sprite correctly

                if self.__snake.HorizontalMove > 0:
                    head = self.__spritesheet.getSprite("snake_head_right",self.__block_size)
                elif self.__snake.HorizontalMove < 0:
                    head = self.__spritesheet.getSprite("snake_head_left",self.__block_size)
                elif self.__snake.VerticalMove > 0:
                    head = self.__spritesheet.getSprite("snake_head_down",self.__block_size)
                elif self.__snake.VerticalMove <  0:
                    head = self.__spritesheet.getSprite("snake_head_up",self.__block_size)

                self.blit(head,(self.__snake.SnakeHead.left,self.__snake.SnakeHead.top))
            elif index == self.__snake.Length-1:
                
                #setting tail sprite correctly
                
                if self.__snake.Snake[index].left == self.__snake.Snake[index-1].left:
                    if self.__snake.Snake[index].top > self.__snake.Snake[index-1].top:
                        tail = self.__spritesheet.getSprite("snake_tail_down",self.__block_size)
                    else:
                        tail = self.__spritesheet.getSprite("snake_tail_up",self.__block_size)
                elif self.__snake.Snake[index].top == self.__snake.Snake[index-1].top:
                    if self.__snake.Snake[index].left > self.__snake.Snake[index-1].left:
                        tail = self.__spritesheet.getSprite("snake_tail_right",self.__block_size)
                    else:
                        tail = self.__spritesheet.getSprite("snake_tail_left",self.__block_size)

                self.blit(tail,(self.__snake.Snake[index].left,self.__snake.Snake[index].top))
            else:
                #setting snake body
                if self.__snake.Snake[index].left == self.__snake.Snake[index-1].left and self.__snake.Snake[index].left == self.__snake.Snake[index+1].left:
                    body = self.__spritesheet.getSprite("snake_body_vertical",self.__block_size)
                    self.blit(body,(self.__snake.Snake[index].left,self.__snake.Snake[index].top))
                elif self.__snake.Snake[index].top == self.__snake.Snake[index-1].top and self.__snake.Snake[index].top == self.__snake.Snake[index+1].top:
                    body = self.__spritesheet.getSprite("snake_body_horizontal",self.__block_size)
                    self.blit(body,(self.__snake.Snake[index].left,self.__snake.Snake[index].top))
                else:
                    #setting snake body curves
                    if self.__snake.Snake[index].left == self.__snake.Snake[index-1].left and self.__snake.Snake[index].top > self.__snake.Snake[index-1].top:
                        if self.__snake.Snake[index].left > self.__snake.Snake[index+1].left:
                            curve = self.__spritesheet.getSprite("snake_bottom_right_corner",self.__block_size)
                        else:
                            curve = self.__spritesheet.getSprite("snake_bottom_left_corner",self.__block_size)
                    elif self.__snake.Snake[index].left == self.__snake.Snake[index-1].left and self.__snake.Snake[index].top < self.__snake.Snake[index-1].top:
                        if self.__snake.Snake[index].left > self.__snake.Snake[index+1].left:
                            curve = self.__spritesheet.getSprite("snake_top_right_corner",self.__block_size)
                        else:
                            curve = self.__spritesheet.getSprite("snake_top_left_corner",self.__block_size)
                        

                    elif self.__snake.Snake[index].top == self.__snake.Snake[index-1].top  and self.__snake.Snake[index].left > self.__snake.Snake[index-1].left:
                        if self.__snake.Snake[index].top > self.__snake.Snake[index+1].top:
                            curve = self.__spritesheet.getSprite("snake_bottom_right_corner",self.__block_size)
                        else:
                            curve = self.__spritesheet.getSprite("snake_top_right_corner",self.__block_size)
                    elif self.__snake.Snake[index].top == self.__snake.Snake[index-1].top  and self.__snake.Snake[index].left < self.__snake.Snake[index-1].left:
                        if self.__snake.Snake[index].top > self.__snake.Snake[index+1].top:
                            curve = self.__spritesheet.getSprite("snake_bottom_left_corner",self.__block_size)
                        else:
                            curve = self.__spritesheet.getSprite("snake_top_left_corner",self.__block_size)
                         
                    self.blit(curve,(self.__snake.Snake[index].left,self.__snake.Snake[index].top))

  
    
    


   


    def drawElements(self):
        self.__drawBackground()
        self.__drawFood()
        self.__drawSnake()


    @property
    def Snake(self):
        return self.__snake
    @property
    def Food(self):
        return self.__food
    


class MainWindow:
    def __init__(self):
        self.__block_size = 30
        self.__block_num = 20

        self.__width = self.__block_size * self.__block_num
        self.__height = self.__block_size * self.__block_num

        self.__size = (self.__width,self.__height)

        self.main_window = pygame.display.set_mode(self.__size)

        self.snake_area = SnakeArea(self.__block_size,self.__block_num)

        self.__spriteSheet = SpriteSheet()

        self.__font = pygame.font.Font(None,32)
        self.__title = pygame.font.Font(None,32)
        self.__counter_text = pygame.font.Font(None,20)
        self.__counter_surface = pygame.Surface((200,30))

        self.__random_text = pygame.font.Font(None,24)


        self.__fps = 60
        self.__element_speed = 120
        self.__userEvent = pygame.USEREVENT


    def __drawTitle(self):


        self.main_window.blit(
        self.__title.render("Snake Game",False,(255,255,255),(148,117,94)),
        (0,0)
        )

    def __drawCounter(self):
        apple = self.__spriteSheet.getSprite("food_apple",25)
        self.__counter_surface.fill((148,117,94))
        self.__counter_surface.blit(apple,(0,0))
        self.__counter_surface.blit(
            self.__counter_text.render(f"{self.snake_area.Snake.Length}",False,(255,255,255),(148,117,94)),
            (30,8)
        )
        self.main_window.blit(self.__counter_surface,(200,0))

    def __drawText(self,text):
        self.main_window.blit(
            self.__random_text.render(text,False,(255,255,255),(148,117,94)),
            (30,30)
        )

    def __drawBackground(self):
        water = self.__spriteSheet.getEnvironSprite("water_sprite",self.__block_size)
        x = 0
        y = 0
        for i in range(self.__block_size):
            for i in range(self.__block_size):
                self.main_window.blit(water,(x,y))
                x+=self.__block_size
            x = 0
            y+=self.__block_size

    def initElements(self):
        pygame.time.set_timer(self.__userEvent,self.__element_speed)
        self.snake_area.setSheet(self.__spriteSheet)
        self.__drawBackground()
        self.__drawTitle()
        self.__drawCounter()

    def gameLoop(self):
        
        self.initElements()
        self.snake_area.initElements()

        
        while True:
            
            self.__drawCounter()   
                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:exit()


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake_area.Snake.MoveLeft()
                    elif event.key == pygame.K_RIGHT:
                        self.snake_area.Snake.MoveRight()
                    elif event.key == pygame.K_UP:
                        self.snake_area.Snake.MoveUp()
                    elif event.key == pygame.K_DOWN:
                        self.snake_area.Snake.MoveDown()

                if event.type == self.__userEvent:
                        
                    self.snake_area.Snake.Move()

                    self.snake_area.drawElements() 

                    self.main_window.blit(self.snake_area,(60,50))
                    
                    if self.snake_area.checkIfOutOfScreen():
                        self.snake_area.Snake.initSnake() 
                    
                    if self.snake_area.Snake.checkSelfCollide():
                        self.snake_area.Snake.initSnake()

                    if self.snake_area.Snake.checkCollision(self.snake_area.Food):
                        self.snake_area.Snake.Eat(self.snake_area.Food)
                        self.snake_area.RelocateFood()
            
            
            
           

            pygame.display.update()
            pygame.time.Clock().tick(self.__fps)


if __name__ == "__main__":
    game = MainWindow()
    game.gameLoop()