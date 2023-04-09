import sys


import pygame

class Tile:
	def __init__(self, x, y, color):
		self.x = x
		self. y = y
		self.color = color
		self.width = 50
		self.height = 50


	def is_clicked(self):
		if self.color == (0, 0, 0):
			return True


class Synth:
	def __init__(self):
			pygame.init()
			self.tile_list = []
			self.screen_width = 800
			self.screen_height = 400
			self.fps = pygame.time.Clock()
			self.current_beat = 0
			self.tempo = 134 # bpm
			self.beat_intervals = 60000 // self.tempo # millisecond difference between quarter notes
			self.draw_beat_current = pygame.event.custom_type() # custom event to run every beat interval
			self.beat_playing = False
			self.channels = []
			self.samples = {0: pygame.mixer.Sound("./kick_sample.mp3"),
							1: pygame.mixer.Sound("./snare_sample.mp3")}


			self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
			pygame.display.set_caption("Synth")


	def run(self):
		"""Starts main loop for game"""
		self.init_tiles()
		self.init_channels()

		pygame.time.set_timer(self.draw_beat_current, self.beat_intervals) # draw new (current)beat every interval

		while True:
			self.fps.tick(60)


			# Watch for keyboard and mouse inputs
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.rect_clicked()
				if event.type == self.draw_beat_current:
					self.increase_beat()


			# Redraw screen color each pass through loop
			self.screen.fill((201, 201, 201))

			
			self.draw_tiles()

			self.draw_current_beat(self.current_beat)
			self.play_beat()

			
			
			# Make most recently drawn screen visible
			pygame.display.flip()




	def draw_tiles(self):
	# all 4s are for time sig, make this intercahgable later
		for tiles in self.tile_list:
			for tile in tiles:
				pygame.draw.rect(self.screen, tile.color, 
					(tile.x, tile.y,tile.width,tile.height))


				


	def rect_clicked(self):
		for rect_list in self.tile_list:
			for i in range(len(rect_list)):
				click_pos = pygame.mouse.get_pos()
				rect = pygame.Rect(rect_list[i].x, rect_list[i].y, 50, 50)
				if rect.collidepoint(click_pos):
					x,y = rect[0], rect[1]
					if rect_list[i].color == (0, 0, 0):
						rect_list[i] = Tile(x, y, (255,255,255))
					else:
						rect_list[i] = Tile(x, y, (0,0,0))



	def init_tiles(self):
		self.tile_list = [[] for i in range(4)]

		screen_pad_width = 80 #top and bottom
		screen_pad_height = 20


		# all 4s are for time sig, make this intercahgable later
		for i in range(4):
			for j in range(4):
				self.tile_list[i].append(Tile(screen_pad_width, screen_pad_height, (255, 255, 255)))
				screen_pad_width += self.screen_width // 4

			screen_pad_height += self.screen_height // 4
			screen_pad_width = 80


	def draw_current_beat(self, i):
		mark = pygame.Rect((self.tile_list[0][i%4].x)+15, (self.tile_list[0][i%4].y)-25, 20, 20)
		pygame.draw.rect(self.screen, (123, 123, 123), mark)
	
	def increase_beat(self):
		current_beat = self.current_beat % 4
		self.current_beat += 1
		self.beat_playing = False
		return current_beat



	def play_beat(self):
		if not self.beat_playing:
			self.beat_playing = True
			self.current_beat %= 4
			
			for i in range(4):
				for j in range(4):
					if self.tile_list[j][i].is_clicked() and self.current_beat == i:
						self.channels[j].play(self.samples[j])

		else:
			#print("is playing") #do nothing, already playing beat
			pass


	def init_channels(self):
		for i in range(4):
			self.channels.append(pygame.mixer.Channel(i))


 

					




# get point clicked and check if it collided with any point in our rectangles
# if yes turn rect "on\off"
# 
		
if __name__ == "__main__":
	# Make a game instance, and run it
	ai = Synth()
	ai.run()


# give 380 for full screen
# give 780 for full width
# 380/4


# 10 + 197 + 197 + 197 + 197 
# 10 + 197...
# ....
# ...


