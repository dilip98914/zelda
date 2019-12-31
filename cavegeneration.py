import random
import pygame

pygame.init() 

rows=100
cols=100
size=10
screen = pygame.display.set_mode((cols*size,rows*size)) 

wallColor=(139,69,19)
emptyColor=(255,255,255)
bgColor=(0,0,0)


class Node(object):
	def __init__(self,x,y,value,grid):
		self.x,self.y=x,y
		self.value,self.grid=value,grid
		self.nbors1=[]
		self.nbors2=[]
		
	def __str__(self):
		return "Node at {}".format((self.x,self.y))
	def getNbors(self,val):
		if val==1:
			for i in range(len(self.nbors1)):
				print(self.nbors1[i])
		elif val==2:
			for i in range(len(self.nbors2)):
				print(self.nbors2[i])


	def add_nbors(self):
		x=self.x
		y=self.y
		for  j in range(y-1,y+2):
			for  i in range(x-1,x+2):
				if j<0 or i<0 or i>=cols or j>=rows:
					continue
				if j==self.y and i==self.x:
					continue
				try:
					self.nbors1.append(self.grid[j][i])
				except IndexError:
					continue

		for  j in range(y-2,y+3,2):
			for  i in range(x-2,x+3,2):
				if j<0 or i<0 or i>=cols or j>=rows:
					continue
				if j==self.y and i==self.x:
					continue
				try:
					self.nbors2.append(self.grid[j][i])
				except IndexError:
					continue



class Map(object):
	def __init__(self,cols,rows):
		self.cols,self.rows=cols,rows
		self.map=[[0 for x  in range(self.cols)] for y in range(self.rows)]
		self.fill_map()
		self.add_all_nbours()
		
	def add_all_nbours(self):
		for y in range(self.rows):
			for x in range(self.cols):
				self.map[y][x].add_nbors()


	def fill_map(self):
		for y in range(self.rows):
			for x in range(self.cols):
				if random.random()<0.4:
					# place wall
					self.map[y][x]=Node(x,y,1,self.map)
				else:
					self.map[y][x]=Node(x,y,0,self.map)

	def draw(self):
		for y in range(self.rows):
			for x in range(self.cols):
				color=None
				if(self.map[y][x].value==1):
					color=wallColor
				else:
					color=emptyColor
				rect = pygame.Rect(x*size,y*size,size-1,size-1)
				pygame.draw.rect(screen,color,rect)



map=Map(cols,rows)

hx=cols/2
hy=rows/2
print(map.map[hy][hx])
print(map.map[hy][hx].getNbors(2))
def main_loop():
	running=True
	while running:
		screen.fill((0,0,0))
		map.draw()	
	   	for event in pygame.event.get():
	   		if event.type == pygame.QUIT:
	   			running = False 
	   	pygame.display.flip()
	pygame.quit()

if __name__=='__main__':
	main_loop() 