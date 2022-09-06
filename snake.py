import pygame



class Snake:
    def __init__(self,start_left,start_top):



        #size of the snake actually.
        self.block_width = 30
        self.block_height = 30


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


        self.graphics = []


        #this will increment according to the block size. and are use for moving the snake .
        self.__VERTICAL_MOVE = 0
        self.__HORIZONTAL_MOVE  = 0


        #initializing snake graphics

        self.snake_head = pygame.image.load('assets/head.png')
        self.snake_body = pygame.image.load('assets/body.png')
        self.snake_body_curve = pygame.image.load('assets/curve.png')
        self.snake_tail = pygame.image.load('assets/tail.png')




    #initializing the snake
    def initSnake(self):
        self.snake = []
        increment = -self.block_width

        self.snake = [
            pygame.Rect(self.start_left,self.start_top,self.block_width,self.block_width),
            pygame.Rect(self.start_left,self.start_top+self.block_width,self.block_width,self.block_width),
            pygame.Rect(self.start_left,self.start_top+self.block_width*2,self.block_width,self.block_width)
        ]

        self.head = self.snake[0]
        self.snake_size = 3
        self.__VERTICAL_MOVE = 0
        self.__HORIZONTAL_MOVE = 0
        self.start_state = True
        self.snakeGraphics()

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
        if not self.start_state:
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
    

    def snakeGraphics(self):
        self.graphics = []


        #head
        head = self.snake_head.copy()
        head = pygame.transform.scale(head,(self.block_width,self.block_height))


        #BODY
        body = self.snake_body.copy()
        body = pygame.transform.scale(body,(self.block_width+2,self.block_height))



        #tail
        tail = self.snake_tail.copy()
        tail = pygame.transform.scale(tail,(self.block_width+1,self.block_height+4))
        


        #curve body
        curve = self.snake_body_curve
        curve = pygame.transform.scale(curve,(self.block_width,self.block_height+4))

        
        for index,element in enumerate(self.snake):

            #setting head position
            if index == 0:
                if self.__HORIZONTAL_MOVE > 0:
                    head = pygame.transform.rotate(head,-90)
                elif self.__HORIZONTAL_MOVE < 0:
                    head = pygame.transform.rotate(head,90)
                elif self.__VERTICAL_MOVE > 0:
                    head = pygame.transform.rotate(head,180)
                
                self.graphics.append({"graphic":head,"pos":self.snake[index]})

            #setting body and curves positions
            elif index + 1 < len(self.snake) and index > 0:

                
                if self.snake[index-1].left == self.snake[index].left and self.snake[index].left == self.snake[index+1].left:
                    body_angle = pygame.transform.rotate(body,90)
                    self.graphics.append({"graphic":body_angle,"pos":self.snake[index]})
                    
                elif self.snake[index-1].top == self.snake[index].top and self.snake[index].top == self.snake[index+1].top:
                    self.graphics.append({"graphic":body,"pos":self.snake[index]})
                
                else:
                    if self.snake[index].top == self.snake[index-1].top:
                        if self.snake[index].left >= self.snake[index-1].left:
                            if self.snake[index].top >= self.snake[index+1].top:
                                current_curve = curve.copy()
                            else:
                                current_curve = pygame.transform.rotate(curve,90)
                            self.graphics.append({"graphic":current_curve,"pos":self.snake[index]})  
                        elif self.snake[index].left <= self.snake[index-1].left:
                            if self.snake[index].top >= self.snake[index+1].top:
                                current_curve = pygame.transform.rotate(curve,-90)
                            else:
                                current_curve = pygame.transform.rotate(curve,-180)
                            self.graphics.append({"graphic":current_curve,"pos":self.snake[index]})
                    elif self.snake[index].left == self.snake[index-1].left:
                        if self.snake[index].top >= self.snake[index-1].top:
                            if self.snake[index].left >= self.snake[index+1].left:
                                current_curve = curve
                            else:
                                current_curve = pygame.transform.rotate(curve,-90)
                            self.graphics.append({"graphic":current_curve,"pos":self.snake[index]})
                        else:
                            if self.snake[index].left >= self.snake[index+1].left:
                                current_curve = pygame.transform.rotate(curve,90)
                            else:
                                current_curve = pygame.transform.rotate(curve,180)
                            self.graphics.append({"graphic":current_curve,"pos":self.snake[index]})

            #setting tail position
            elif index == len(self.snake)-1:
                if self.snake[index].left == self.snake[index-1].left:
                    if self.snake[index].top >= self.snake[index-1].top:
                        self.graphics.append({"graphic":tail,"pos":self.snake[index]})
                    else:
                        tail_angle = pygame.transform.rotate(tail,180)
                        self.graphics.append({"graphic":tail_angle,"pos":self.snake[index]})
                elif self.snake[index].top == self.snake[index-1].top:
                    if self.snake[index].left >= self.snake[index-1].left:
                        tail_angle = pygame.transform.rotate(tail,90)
                        self.graphics.append({"graphic":tail_angle,"pos":self.snake[index]})
                    else:
                        tail_angle = pygame.transform.rotate(tail,-90)
                        self.graphics.append({"graphic":tail_angle,"pos":self.snake[index]})


