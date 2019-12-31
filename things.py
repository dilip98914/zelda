import pygame,sys
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



pygame.init()

screen=pygame.display.set_mode((800,600))


class Overworld(object):
	def __init__(self):
		map0=Map(10,10,[0],[1])
		self.map=map0.get_raw_grid()
		# print(self.map)
		self.entity=Trees(0,0)

	def main_loop(self):
		running=True

		while running:
			screen.fill((255,255,255))
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					running=False

			self.draw()
			pygame.display.flip()


		pygame.quit()
		sys.exit()

	def draw(self):
		for y in range(len(self.map)):
			for x in range(len(self.map[0])):
				# if(self.map.grid[y][x].value==1):
					# entity=
				screen.blit(self.entity.image, (x*self.entity.w,y*self.entity.h))

if __name__=="__main__":
	overworld=Overworld()
	overworld.main_loop()