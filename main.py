import pygame
from pygame.locals import *


TreeImg=pygame.image.load('overworld/trees.png')
TreeImg2=pygame.image.load('overworld/single_trees.png')
TreeImg3=pygame.image.load('overworld/single_tree.png')



	



class Link(pygame.sprite.Sprite):

	def __init__(self,x,y,DIRECTION,has_sword,has_bombs):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("link/link_up1.png")
		self.ticker=0
		self.current_frame=0
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.change_x_left=0
		self.change_x_right=0
		self.change_y_up=0
		self.change_y_down=0
		self.change_y=0
		self.walls=None
		self.mobs=None
		self.items=None
		self.bomb_items=None
		self.keys=None
		self.locks=None
		self.DIRECTION=DIRECTION
		self.upKeyPressed=False
		self.downKeyPressed=False
		self.leftKeyPressed=False
		self.rightKeyPressed=False
		self.spacePressed=False
		self.WALKRATE=5
		self.RIGHT,self.LEFT,self.UP,self.DOWN="right left up down".split()
		self.action='walking'
		self.has_sword=has_sword
		self.effect=pygame.mixer.Sound('LoZ_Sounds/LOZ_Sword.wav')
		self.item_find=pygame.mixer.Sound('LoZ_Sounds/LoZ_Get_Item.wav')
		self.item_find.set_volume(.3)
		self.secret=pygame.mixer.Sound('LoZ_Sounds/LoZ_Secret.wav')
		self.secret.set_volume(.6)
		self.enter_door=False
		self.enter_door2=False
		self.enter_door3=False
		self.in_dungeon=False
		self.can_move=True
		self.has_key=False
		self.has_bombs=False
		self.bombs=pygame.sprite.Group()

	def walk(self):
		pass
	def update(self):
		pass

class Mob(pygame.sprite.Sprite):
	def __init__(self,x,y,hitpoint,game):
		pygame.sprite.Sprite.__init__(self)
		self.rect=Rect(0,0,48,48)
		self.image=pygame.image.load('meanie/0.png')
		self.rect.x=x
		self.rect.y=y
		self.walls=None
		self.doors=None

	def update(self):
		pass

class Mob_Arrow(pygame.sprite.Sprite):
	def __init__(self,x,y,direction):
		pygame.sprite.Sprite.__init__(self)

	def update(self):
		pass

class Bomb(pygame.sprite.Sprite):
	def __init__(self,x,y,link):
		pygame.sprite.Sprite.__init__(self)

	def update(self):
		pass



class Wall(Thing):
	def __init__(self,x,y,path):
		Thing().__init__(self,x,y,path)

	def update(self):
		pass


class Door(Thing):
	def __init__(self,x,y):
		path='link/walk_right1.png'
		Thing.__init__(self,x,y,path)
		self.image.fill(Color("Black"))

class Rock(Thing):
	def __init__(self,x,y,path,destructable):
		Thing.__init__(self,x,y,path)
		self.destructable=destructable


class DungeonRock(Thing):
	def __init__(self,x,y):
		path='overworld/dungeon_rocks.png'
		Thing.__init__(self,x,y,path)


class Water(Thing):
	def __init__(self,x,y,path):
		Thing.__init__(self,x,y,path)


class Sword(Thing):
	def __init__(self,x,y):
		path='0.png'
		Thing.__init__(self,x,y,path)


class Key(Thing):
	def __init__(self,x,y):
		path='misc/key.png'
		Thing.__init__(self,x,y,path)


class Text(Thing):
	def __init__(self,x,y):
		path='Alone.png'
		Thing.__init__(self,x,y,path)


class Room(object):
	wall_list=None
	def __init__(self):
		self.wall_list=pygame.sprite.Group()
		self.mob_list=pygame.sprite.Group()
		self.item_list=pygame.sprite.Group()
		self.door_list=pygame.sprite.Group()
		self.door_list2=pygame.sprite.Group()
		self.door_list3=pygame.sprite.Group()
		self.key_list=pygame.sprite.Group()
		self.lock_list=pygame.sprite.Group()
		self.bomb_items_list=pygame.sprite.Group()
		self.dungeon=False


class Dungeon(Room):
	def __init__(self):
		Room.__init__(self)
		self.dungeon=True
		items=[Sword(390,250),Text(240,125)]
		walls = [DungeonRock(0,-50), DungeonRock(400,-50), DungeonRock(-550,90),
	                DungeonRock(-550,220),DungeonRock(-550,300),DungeonRock(-550,400),DungeonRock(738,90),
	                DungeonRock(738,220),DungeonRock(738,300),DungeonRock(738,400),DungeonRock(-375,500),
	                DungeonRock(570,500), Wall(382,175,Oldie)]
        doors = []
        for wall in walls:
            self.wall_list.add(wall)
        for item in items:
            self.item_list.add(item)
class Room1(Room):
	def __init__(self):
		Room.__init__(self)
		walls = [Wall(0,0,TreeImg), Wall(256,0,TreeImg),Wall(500,0,TreeImg), Wall((900-256),0,TreeImg), Wall(-160,113,TreeImg),
                 Wall(-160,226,TreeImg),Wall(-160,440,TreeImg), Wall(-160, 553,TreeImg),
                 Wall((900-150),113,TreeImg),Wall((900-150),226,TreeImg), Water((800-216),443, Water1),Wall(700,0,TreeImg),
                 Wall(75,553,TreeImg),Wall(200,553,TreeImg),Wall(330,553,TreeImg)]
        doors=[Door(300,66)]
        for wall in walls:
        	self.wall_list.add(wall)
        for door in doors:
        	self.door_list.add(door)


class Room2(Room):
	def __init__(self):
		Room.__init__(self)
		walls = [Water(0,443, "overworld/water_right.png"),Wall(213,500,"overworld/trees.png"), Wall(326,500,"overworld/trees.png"),
                 Rock(0,0,"overworld/rocks.png",False),Rock(-500,120,"overworld/rocks.png",False),Rock(-500,200,"overworld/rocks.png",False), Wall(439,500,"overworld/trees.png"),Wall(551,500,"overworld/trees.png"),
                 Wall(750,0,"overworld/trees.png"),Wall(750, 339,"overworld/trees.png"),Wall(750,451,"overworld/trees.png"),Wall(750,113,"overworld/trees.png"),
                  Wall(750,226,"overworld/trees.png")]
        self.keys=[Key(300,300)]
        for wall in walls:
        	self.wall_list.add(wall)
        for key in self.keys:
        	self.key_list.add(key)



class GameMain():
	done=False

	def __init__(self,width=800,height=600):
		pygame.mixer.pre_init(4410,-16,2,2048)
		pygame.init()
		self.color=(252,216,168)
		self.width,self.height=width,height
		pygame.display.set_caption('zelda in making')
		self.screen=pygame.display.set_mode((self.width,self.height))
		self.clock=pygame.time.Clock()
		self.rock=DungeonRock(0,10)
		self.link=Link(200,500,"DOWN",False,False)
		self.all_sprite_list=pygame.sprite.Group()
		self.all_sprite_list.add(self.rock)
		self.all_sprite_list.add(self.link)
		self.rooms=[[Room1(),Dungeon()],
					[Room2(),Dungeon()],]
		self.current=(1,0)
		self.current_room=self.rooms[self.current[1]][self.current[0]]


		self.current_screen='title'

	def main_loop(self):
		pygame.mixer.music.load("LoZ_Sounds/overworld.ogg")
		pygame.mixer.music.play(-1)
		pygame.mixer.music.set_volume(.5)

		while not self.done:
			if self.current_screen=='game':
				self.handle_events()
				self.draw()
				self.all_sprite_list.update()
				self.change_room()
			elif self.current_screen=='title':
				self.handle_events_title()
				self.draw_title()
			self.clock.tick(60)

		pygame.quit()

	def draw_title(self):
		self.screen.fill(Color('Grey'))
		logo=pygame.image.load('logo.png')
		credit=pygame.image.load('credits.png')
		self.screen.blit(logo,(220,200))
		self.screen.blit(credit,(240,443))
		pygame.display.flip()

	def handle_events_title(self):
		events=pygame.event.get()
		for event in events:
			if event.type==pygame.QUIT:
				self.done=True
			if event.type==KEYDOWN:
				if event.key==K_RETURN:
					self.current_screen='game'


	def handle_events(self):
		events=pygame.event.get()
		keys=pygame.key.get_pressed()
		for event in events:
			if event.type==QUIT:
				self.done=True
			elif event.type==KEYDOWN and self.link.can_move:
				if event.key==K_ESCAPE:
					self.done=True
				elif event.key==K_UP:
					self.link.upKeyPressed=True
					self.link.downKeyPressed=False
					self.link.DIRECTION=self.link.UP

				elif event.key==K_DOWN:
					self.link.downKeyPressed=True
					self.link.upKeyPressed=False
					self.link.DIRECTION=self.link.DOWN
					self.link.change_y=5
				elif event.key==K_LEFT:
					self.link.leftKeyPressed=True
					self.link.rightKeyPressed=False
					self.link.DIRECTION=self.link.LEFT
				elif event.key==K_RIGHT:
					self.link.rightKeyPressed=True
					self.link.leftKeyPressed=False
					self.link.DIRECTION=self.link.RIGHT

				elif event.key==K_r:
					obj=GameMain()
					obj.main_loop()
					
				elif event.key==K_SPACE and self.link.has_sword==True:
					self.link.spacePressed=True
					self.link.can_move=False
					self.link.effect.play()
					self.link.action='attacking'

			elif event.type==KEYUP:
				if event.key==K_UP:
					self.link.upKeyPressed=False
					if self.link.rightKeyPressed:
						self.link.DIRECTION=self.link.RIGHT
					elif self.link.leftKeyPressed:
						self.link.DIRECTION=self.link.LEFT
				elif event.key==K_DOWN:
					self.link.downKeyPressed=False
					if self.link.rightKeyPressed:
						self.link.DIRECTION=self.link.RIGHT
					elif self.link.leftKeyPressed:
						self.link.DIRECTION=self.link.LEFT
				elif event.key==K_RIGHT:
					self.link.rightKeyPressed=False
					if self.link.upKeyPressed:
						self.link.DIRECTION=self.link.UP
					elif self.link.downKeyPressed:
						self.link.DIRECTION=self.link.DOWN
				elif event.key==K_LEFT:
					self.link.leftKeyPressed=False
					if self.link.upKeyPressed:
						self.link.DIRECTION=self.link.UP
					elif self.link.downKeyPressed:
						self.link.DIRECTION=self.link.DOWN

				elif event.key==K_SPACE:
					self.link.can_move=True
					self.link.spacePressed=False
					self.link.action='walking'

	def draw(self):
		if self.current_room.dungeon:
			self.screen.fill(Color('Black'))
		else:
			self.screen.fill((self.color))

		self.all_sprite_list.draw(self.screen)
		self.current_room.wall_list.draw(self.screen)
		self.current_room.item_list.draw(self.screen)
		self.current_room.key_list.draw(self.screen)
		self.current_room.door_list.draw(self.screen)
		if self.link.has_sword==False:
			self.current_room.item_list.draw(self.screen)
		else:
			for item in self.current_room.item_list:
				item.kill()
		self.current_room.door_list.draw(self.screen)
		pygame.display.flip()

	def change_room(self):
		if self.link.enter_door:
			self.current_room=self.rooms[0][1]
			self.link.in_dungeon=True
			self.link.items=self.current_room.item_list
			if self.link.in_dungeon:
				self.link.walls=self.current_room.wall_list
				self.link.doors=self.current_room.door_list
				#i Guess exit
				if self.link.rect.y>600:
					self.current_room=self.rooms[self.current[1]][self.current[0]]
					self.link.enter_door=False
					self.link.in_dungeon=False
					self.link.walls=self.current_room.wall_list
					self.link.doors=self.current_room.door_list
					self.link.items=self.current_room.item_list
		elif self.link.rect.x>801:
			self.current=(self.current[0]+1,self.current[1])
			self.current_room=self.rooms[self.current[1]][self.current[0]]
			self.link.walls=self.current_room.wall_list
			self.link.doors=self.current_room.door_list
			self.link.items=self.current_room.item_list
			self.link.doors=self.current_room.door_list
			self.link.rect.x=0
			

if __name__=='__main__':
	game=GameMain()
	game.main_loop()