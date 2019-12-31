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
	
	def draw(self,image,surface,pos):
		surface.blit(image,pos)


class Trees(Thing):
	def __init__(self,x,y):
		Thing.__init__(self,x,y,256,113,'overworld/trees.png','trees')
		self.image2=self.image.subsurface(pygame.Rect(0, 0, 113, 113))
		self.w=256
		self.h=113


class Rocks(Thing):
	def __init__(self,x,y):
		Thing.__init__(self,x,y,256,113,'overworld/rocks.png','rocks')
		self.image2=self.image.subsurface(pygame.Rect(0, 0, 113, 113))
		self.w=256
		self.h=113

class SingleTree(Thing):
	def __init__(self,x,y):
		Thing.__init__(self,x,y,50,50,'overworld/single_tree.png','single_trees')
		self.w=self.h=50
		self.image2=self.image




BG_COLOR=(255,255,255)

class Game(object):
	def __init__(self,w=800,h=600):
		pygame.init()
		self.w,self.h=w,h
		self.clock=pygame.time.Clock()
		self.screen=pygame.display.set_mode((w,h))
		self.running=False
		self.mapManager = MapManager()
		pygame.display.set_caption("The Legend of Zelda in making")

	def update(self):
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				self.running=False
	
	def draw(self):
		self.screen.fill(BG_COLOR)
		self.mapManager.draw(self.screen)
		pygame.display.flip()

	def keepUp(self):
		self.running=True
		
		while self.running:
			self.update()
			self.draw()


		pygame.quit()
		sys.exit()


def getEmptyMap(rows,cols):
	return [ [0 for x in range(cols)] for y in range(rows) ]


class MapManager(object):
	def __init__(self):
		# self.overworld_grid=getEmptyMap(10,10)
		# self.dungeon_grid=getEmptyMap(5,5)
		self.overworld_grid=self.add_to_overworld()
		self.overworld=getEmptyMap(10,10)
		self.arr_to_map(self.overworld_grid)
		self.current=None
		# self.entity=Trees(0,0)
		# self.entity2=Rocks(0,0)
		# self.surface=pygame.surface.Surface([113,113])
		# self.surface.fill([252, 216, 168])

	def add_to_overworld(self):
		walls=[[1,1,1,1,1,1,1,1,1,1],
				[1,0,0,0,0,0,0,2,0,1],
				[1,0,2,2,0,0,0,2,0,1],
				[1,0,0,0,1,1,0,0,0,1],
				[1,0,0,0,1,1,0,2,0,1],
				[1,0,0,0,0,0,0,0,0,1],
				[1,0,2,0,0,0,0,2,2,1],
				[1,0,0,0,0,0,0,2,2,1],
				[1,0,0,0,0,0,0,2,2,1],
				[1,1,1,1,1,1,1,1,1,1],
				]
		return walls

	def arr_to_map(self,arr):
		for y in range(len(arr)):
			for x in range(len(arr[0])):
				if arr[y][x]==0:
					self.overworld[y][x]=Trees(x*113,y*113)
				elif arr[y][x]==1:
					self.overworld[y][x]=Rocks(x*113,y*113)
				elif arr[y][x]==2:
					self.overworld[y][x] = SingleTree(x * 50, y * 50)

	def draw(self,screen):
		for y in range(len(self.overworld)):
			for x in range(len(self.overworld[0])):
				curr_tile=self.overworld[y][x]
				curr_tile.draw(curr_tile.image2,screen,(x*curr_tile.h,y*curr_tile.h))

if __name__=="__main__":
	game=Game()
	game.keepUp()