
import pygame
import json
class SpriteSheet:
    def __init__(self):
        self.sprite_sheet = pygame.image.load('assets/spritesheet.png')
        self.sprite_sheet_json = json.loads(open('assets/sprites.json','r').read())
        self.grass_sheet = pygame.image.load('assets/environ_tilesheet.png')
        self.grass_sheet_json = json.loads(open('assets/environ_tilesheet.json').read())
        self.spriteDict = {}
        self.__initDict()
    
    def __initDict(self):
        for sprite in self.sprite_sheet_json:
            if not sprite['name'] in self.spriteDict:
                self.spriteDict[sprite['name']] = sprite
        for sprite in self.grass_sheet_json:
            if not sprite['name'] in self.spriteDict:
                self.spriteDict[sprite['name']] = sprite


    def getSpriteMetaData(self,name:str) -> pygame.Surface:
        sprite = self.spriteDict[name]
        x,y = sprite['x'],sprite['y']
        w,h = sprite['width'],sprite['height']

        return (x,y,w,h)

    def getSprite(self,name:str,size:int) -> pygame.Surface:
        
        x,y,w,h = self.getSpriteMetaData(name)

        sprite_surface = pygame.Surface((w,h))
        sprite_surface.set_colorkey((0,0,0))
        sprite_surface.blit(self.sprite_sheet,(0,0),(x,y,w,h))

        sprite_surface = pygame.transform.scale(sprite_surface,(size,size))

        return sprite_surface

    def getEnvironSprite(self,name:str,size:int)-> pygame.Surface:
        x,y,w,h = self.getSpriteMetaData(name)

        sprite_surface = pygame.Surface((w,h))
        sprite_surface.set_colorkey((0,0,0))
        sprite_surface.blit(self.grass_sheet,(0,0),(x,y,w,h))

        sprite_surface = pygame.transform.scale(sprite_surface,(size,size))

        return sprite_surface

    @property
    def Sheet(self):
        return self.sprite_sheet