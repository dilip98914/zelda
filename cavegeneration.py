import random
import pygame

class Node(object):
	def __init__(self,x,y,value,grid,map0):
		self.x,self.y=x,y
		self.value,self.grid=value,grid
		self.nbors1=[]
		self.nbors2=[]
		self.map0=map0
		
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
				if j<0 or i<0 or i>=self.map0.cols or j>=self.map0.rows:
					continue
				if j==self.y and i==self.x:
					continue
				try:
					self.nbors1.append(self.grid[j][i])
				except IndexError:
					continue

		for  j in range(y-2,y+3,2):
			for  i in range(x-2,x+3,2):
				if j<0 or i<0 or i>=self.map0.cols or j>=self.map0.rows:
					continue
				if j==self.y and i==self.x:
					continue
				try:
					self.nbors2.append(self.grid[j][i])
				except IndexError:
					continue



class Map(object):
	def __init__(self,cols,rows,empties=[0],solids=[1],prob=0.4):
		self.cols,self.rows=cols,rows
		self.empties,self.solids=empties,solids
		self.prob=prob
		self.grid=[[0 for x  in range(self.cols)] for y in range(self.rows)]
		self.gridValues=[[0 for x  in range(self.cols)] for y in range(self.rows)]
		self.fill_map()
		self.add_all_nbours()
		self.generate_map1()
		self.to_values()
	def add_all_nbours(self):
		for y in range(self.rows):
			for x in range(self.cols):
				self.grid[y][x].add_nbors()

	def get_raw_grid(self):
		return self.gridValues


	def to_values(self):
		for y in range(self.rows):
			for x in range(self.cols):
				self.gridValues[y][x]=self.grid[y][x].value		

	def print_map(self):
		for y in range(self.rows):
			for x in range(self.cols):
				print(self.grid[y][x])
			print('\n')

	def fill_map(self):
		for y in range(self.rows):
			for x in range(self.cols):
				if random.random()<self.prob:
					solid=random.choice(self.solids)
					# place wall
					self.grid[y][x]=Node(x,y,solid,self.grid,self)
				else:
					empty=random.choice(self.empties)
					self.grid[y][x]=Node(x,y,empty,self.grid,self)
	
	def generate_map1(self,iter=4):
		counter=0
		while counter<=iter:
			for y in range(self.rows):
				for x in range(self.cols):
					curr=self.grid[y][x]
					score1=0
					score2=0
					for nn in curr.nbors1:
						if nn.value in self.solids:
							score1+=1
					for nn in curr.nbors2:
						if nn.value in self.solids:
							score2+=1
					if(score1>=5 or score2<=2):
						curr.value=random.choice(self.solids)
					else:
						curr.value=random.choice(self.empties)

			counter+=1
