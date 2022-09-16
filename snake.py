from block import Block

class Snake:
    def __init__(self,block_size:int):
        self.__block_size = block_size
        self.__snake = []

        self.__head = None

        self.__HORIZONTAL_MOVE = 0
        self.__VERTICAL_MOVE = 0
        self.__snake_length = 0
        

        self.__initial_state = True




    def initSnake(self):
        x,y = self.__block_size*6,self.__block_size*6
        self.__snake_length = 0
        self.__snake = []
        for i in range(3):
            new_block = Block(self.__block_size,x,y)
            x+=self.__block_size

            self.__snake.append(new_block)
            self.__snake_length+= 1
        self.__head = self.__snake[0]
        self.__HORIZONTAL_MOVE = -self.__block_size
        self.__initial_state = True



    def MoveLeft(self):
        if  not self.__HORIZONTAL_MOVE > 0:
            self.__HORIZONTAL_MOVE = -self.__block_size
            self.__VERTICAL_MOVE = 0
            self.__initial_state = False

    def MoveRight(self):
        if not self.__HORIZONTAL_MOVE < 0:
            self.__HORIZONTAL_MOVE = self.__block_size
            self.__VERTICAL_MOVE = 0
            self.__initial_state = False
    def MoveUp(self):
        if not self.__VERTICAL_MOVE > 0:
            self.__HORIZONTAL_MOVE = 0
            self.__VERTICAL_MOVE= -self.__block_size
            self.__initial_state = False
    def MoveDown(self):
        if not self.__VERTICAL_MOVE < 0:
            self.__HORIZONTAL_MOVE = 0
            self.__VERTICAL_MOVE = self.__block_size
            self.__initial_state = False


    def Move(self):
        if not self.__initial_state:
            if self.__VERTICAL_MOVE != 0 or self.__HORIZONTAL_MOVE != 0:
                self.__snake.pop()
                firstBlock = self.__snake[0].copy()
                firstBlock.left += self.__HORIZONTAL_MOVE
                firstBlock.top+= self.__VERTICAL_MOVE
                self.__snake.insert(0,firstBlock)
                self.__head = firstBlock
    def checkCollision(self,rect) -> bool:
        return self.__head.collidepoint(rect.left,rect.top)

    def checkSelfCollide(self) -> bool:
        for index in range(1,self.__snake_length):
            if self.checkCollision(self.__snake[index]):
                return True
        return False

    def Eat(self,food):
        self.__snake.append(food.copy())
        self.__snake_length+=1

    @property
    def Snake(self) -> list:
        return self.__snake

    @property
    def SnakeHead(self) -> Block:
        return self.__head
    @property 
    def Length(self) -> int:
        return self.__snake_length

    @property
    def HorizontalMove(self) -> int:
        return self.__HORIZONTAL_MOVE
    @property
    def VerticalMove(self) -> int:
        return self.__VERTICAL_MOVE