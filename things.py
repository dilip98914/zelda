import pygame

class Thing(pygame.sprite.Sprite):
	def __init__(self,x,y,path,name):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(path)
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.destructable=False
		self.name=name


class Room(object):
	def __init__(self):
		self.wall_list=pygame.sprite.Group()
		self.mob_list=pygame.sprite.Group()
		self.item_list=pygame.sprite.Group()
		self.dungeon=False
		self.door_list=pygame.sprite.Group()
		