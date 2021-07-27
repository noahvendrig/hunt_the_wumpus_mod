# import pygame
# pygame.init()
# screen = pygame.display.set_mode((100, 100))
# menuSelections = ['startBtn', 'optBtn', 'quitBtn']
# currentSelection = menuSelections.index('startBtn')

# print(currentSelection)
# done = True
# while done:
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 done = False
#                 pygame.quit()
#             if event.key == pygame.K_DOWN:
#                 if currentSelection + 1 == len(menuSelections): currentSelection = 0
#                 else: currentSelection += 1
#                 print(f'{currentSelection}, {menuSelections[currentSelection]}')
    
from PIL import Image
img = Image.open("./img/123.jpg")
pixImg = img.resize((100,100), Image.BILINEAR)
result = pixImg.resize(img.size, Image.NEAREST)
result.save('img/mod22.png')
result.show()

# import pygame, sys

# class Button:
# 	def __init__(self,text,width,height,pos,elevation):
# 		#Core attributes 
# 		self.pressed = False
# 		self.elevation = elevation
# 		self.dynamic_elecation = elevation
# 		self.original_y_pos = pos[1]

# 		# top rectangle 
# 		self.top_rect = pygame.Rect(pos,(width,height))
# 		self.top_color = '#475F77'

# 		# bottom rectangle 
# 		self.bottom_rect = pygame.Rect(pos,(width,height))
# 		self.bottom_color = '#354B5E'
# 		#text
# 		self.text_surf = gui_font.render(text,True,'#FFFFFF')
# 		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

# 	def draw(self):
# 		# elevation logic 
# 		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
# 		self.text_rect.center = self.top_rect.center 

# 		self.bottom_rect.midtop = self.top_rect.midtop
# 		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

# 		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
# 		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
# 		screen.blit(self.text_surf, self.text_rect)
# 		self.check_click()

# 	def check_click(self):
# 		mouse_pos = pygame.mouse.get_pos()
# 		if self.top_rect.collidepoint(mouse_pos):
# 			self.top_color = '#D74B4B'
# 			if pygame.mouse.get_pressed()[0]:
# 				self.dynamic_elecation = 0
# 				self.pressed = True
# 			else:
# 				self.dynamic_elecation = self.elevation
# 				if self.pressed == True:
# 					print('click')
# 					self.pressed = False
# 		else:
# 			self.dynamic_elecation = self.elevation
# 			self.top_color = '#475F77'

# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption('Gui Menu')
# clock = pygame.time.Clock()
# gui_font = pygame.font.Font(None,30)

# button1 = Button('Click me',200,40,(200,250),5)

# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			pygame.quit()
# 			sys.exit()

# 	screen.fill('#DCDDD8')
# 	button1.draw()

# 	pygame.display.update()
# 	clock.tick(60)

# import pygame, sys

# pygame.init()

# WHITE = (255, 255, 255)

# GREY = (200, 200, 200)

# BLACK = (0, 0, 0)

 

 

# class Button():

#     def __init__(self, txt, location, action, bg=WHITE, fg=BLACK, size=(80, 30), font_name="Segoe Print", font_size=16):

#         self.color = bg  # the static (normal) color

#         self.bg = bg  # actual background color, can change on mouseover

#         self.fg = fg  # text color

#         self.size = size

 

#         self.font = pygame.font.SysFont(font_name, font_size)

#         self.txt = txt

#         self.txt_surf = self.font.render(self.txt, 1, self.fg)

#         self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

 

#         self.surface = pygame.surface.Surface(size)

#         self.rect = self.surface.get_rect(center=location)

 

#         self.call_back_ = action

 

#     def draw(self):

#         self.mouseover()

 

#         self.surface.fill(self.bg)

#         self.surface.blit(self.txt_surf, self.txt_rect)

#         screen.blit(self.surface, self.rect)

 

#     def mouseover(self):

#         self.bg = self.color

#         pos = pygame.mouse.get_pos()

#         if self.rect.collidepoint(pos):

#             self.bg = GREY  # mouseover color

 

#     def call_back(self):

#         self.call_back_()

 

 

# def my_great_function():

#     print("Great! " * 5)

 

 

# def my_fantastic_function():

#     print("Fantastic! " * 5)

 

 

# def mousebuttondown():

#     pos = pygame.mouse.get_pos()

#     for button in buttons:

#         if button.rect.collidepoint(pos):

#             button.call_back()

 

 

# screen = pygame.display.set_mode((120, 100))

# RED = (255, 0, 0)

# BLUE = (0, 0, 255)

 

# button_01 = Button("Great!", (60, 30), my_great_function)

# button_02 = Button("Fantastic!", (60, 70), my_fantastic_function, bg=(50, 200, 20))

# buttons = [button_01, button_02]

 

# while True:

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             pygame.quit()

#             sys.exit()

#         elif event.type == pygame.MOUSEBUTTONDOWN:

#             mousebuttondown()

 

#     for button in buttons:

#         button.draw()

 

#     pygame.display.flip()

#     pygame.time.wait(40)

