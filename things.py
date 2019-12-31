import pygame
from cavegeneration import Map


# trees-256 X 113
# single-trees 528 X 144
# single-tree 50 X 50
# rocks,dungeon_rocks 615 X 144
# breakable rocks 144 X 54
# water left-top 216 X 157 
# water right-top 216 X 157 
# water right-bottom 216 X 157 



class Thing(pygame.sprite.Sprite):
	def __init__(self,x,y,w,h,path,name):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(path)
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.w,self.h=w,h
		self.destructable=False
		self.name=name


class Trees(Thing):
	def __init__(self,x,y):
		Thing.__init__(self,x,y,256,113,'overworld/trees.png','trees')


class Rocks(Thing):
	def __init__(self,x,y):
		Thing.__init__(self,x,y,256,113,'overworld/rocks.png','rocks')

class SingleTrees(Thing):
	def __init__(self,x,y):
		Thing.__init__(self,x,y,256,113,'overworld/single_trees.png','single_trees')



class Room(object):
	def __init__(self):
		self.wall_list=pygame.sprite.Group()
		self.mob_list=pygame.sprite.Group()
		self.item_list=pygame.sprite.Group()
		self.dungeon=False
		self.door_list=pygame.sprite.Group()
		
class Overworld(object):
	def __init__(self):
		self.map=Map(100,100)
		print(self.map.map[0][0])


if __name__=="__main__":
	overworld=Overworld()