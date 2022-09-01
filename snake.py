import pygame



class Snake:
    def __init__(self,start_left,start_top):



        #size of the snake actually.
        self.block_width = 13
        self.block_height = 13


        #starting positions and starting state.
        self.start_left = start_left
        self.start_top = start_top
        self.start_state = False

        self.snake = [
            #pygame.Rect(start_left,start_top,self.block_width,self.block_height),
            #pygame.Rect(start_left-13,start_top,self.block_width,self.block_height),
            #pygame.Rect(start_left-26,start_top,self.block_width,self.block_height)
        ]

        #counter for the snake size.
        self.snake_size = 3

        #head of the snake.
        self.head = None

        #color.
        self.head_color = (255,25,255)
        self.body_color = (255,255,255)


        #this will increment according to the block size. and are use for moving the snake .
        self.__VERTICAL_MOVE = 0
        self.__HORIZONTAL_MOVE  = 0




    #initializing the snake
    def initSnake(self):
        self.snake = []
        increment = -self.block_width
        for i in range(3):
            increment+=13
            self.snake.append(pygame.Rect(self.start_left+increment,self.start_top,self.block_width,self.block_height))

        self.head = self.snake[0]
        self.snake_size = 3
        self.__VERTICAL_MOVE = 0
        self.__HORIZONTAL_MOVE = 0
        self.start_state = True

    #checking if the snake has not move to right than it can move to the left
    def moveLeft(self):
        if not self.__HORIZONTAL_MOVE > 0:
            self.__VERTICAL_MOVE = 0
            self.__HORIZONTAL_MOVE = - self.block_width
            self.start_state = False

    #checking if the snake has not move to the left than it can move to the right
    def moveRight(self):
        if not self.start_state:
            if not self.__HORIZONTAL_MOVE < 0:
                self.__VERTICAL_MOVE = 0
                self.__HORIZONTAL_MOVE = self.block_width
                self.start_state = False

    #checking if the snake has not move down than it can move up.
    def moveUp(self):
        if not self.__VERTICAL_MOVE > 0 :
            self.__HORIZONTAL_MOVE =  0
            self.__VERTICAL_MOVE = - self.block_height
            self.start_state = False
    #checking if the snake has not move up than it can move down.
    def moveDown(self):
        if not self.__VERTICAL_MOVE < 0:
            self.__HORIZONTAL_MOVE = 0
            self.__VERTICAL_MOVE = self.block_height
            self.start_state = False



    #checking if the colide with something in this particular case, food or itself.
    def checkCollision(self,object):
        return self.head.collidepoint(object.left,object.top)


    #eating food. and increasing size.
    def Eat(self,food):
        self.snake.append(food)
        self.snake_size+=1

    #cheeckinf if the snake colide with itself.
    def checkSelfCollide(self):
        for i in range(1,self.snake_size):
            if self.checkCollision(self.snake[i]):
                return True
        return False


    #moving the snake

    """
    the logic here is that the snake moves 13 spaces up or 20 spaces down, depending on the value of
    HORIZONTAL_MOVE and VERTICAL_MOVE
    the space are set according to the block size if the block size changes so its spcae between moves.
    in every iteration the head just increments and moves the rest of the body just change its position in the array where
    they are going to be drawn.
    """
    def move(self):
        if self.__VERTICAL_MOVE != 0 or self.__HORIZONTAL_MOVE != 0:
            aux_list = []
            for index,element in enumerate(self.snake):
                current_pos = self.snake[index].copy()
                if index == 0:
                    self.snake[index].left+=self.__HORIZONTAL_MOVE
                    self.snake[index].top+=self.__VERTICAL_MOVE
                    self.head = self.snake[index]
                else:
                    previous_pos = aux_list.pop(0)
                    self.snake[index].left = previous_pos.left
                    self.snake[index].top = previous_pos.top
                aux_list.append(current_pos)                

    


