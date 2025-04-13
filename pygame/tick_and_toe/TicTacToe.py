import pygame
from sys import exit
from random import randint

# initialize pygame
pygame.init()

# Deafault screen sizee
screen_info = pygame.display.Info()
screen_width = screen_info.current_w - 100
screen_height = screen_info.current_h - 100

# colors https://lospec.com/palette-list/slso8
pallete = [ '#0d2b45',  # 0
            '#203c56',  # 1
            '#544e68',  # 2
            '#8d697a',  # 3
            '#d08159',  # 4
            '#ffaa5e',  # 5
            '#ffd4a3',  # 6
            '#ffecd6'  # 7
            ]

lines_color = pallete[ 0 ]
X_color = pallete[ 4 ]
O_color = pallete[ 6 ]
BG_color = pallete[ 0 ]
Title_color = pallete[ 5 ]
button_out_color = pallete[ 5 ]
button_in_color = pallete[ 1 ]
button_text_color = pallete[ 5 ]
button_hover_color = pallete[ 2 ]

# Background
BG = pygame.Surface( (screen_width, screen_height) )
BG.fill( BG_color )
# Game
board = [ ([ None ] * 3) for _ in range( 3 ) ]
current_player = 'o'
game_state = 'menu'
winner = None

# initialize screen
screen = pygame.display.set_mode( (screen_width, screen_height), pygame.RESIZABLE )
pygame.display.set_caption( "Tic-Tac-Toe" )


def get_font( size ) :
	return pygame.font.Font( 'files/Pixeltype.ttf', size )


def board_values() :
	# Calculate board placement to be centered in current window
	global screen_width, screen_height
	min_width, min_height = 300, 300
	screen_width = max( screen_width, min_width )
	screen_height = max( screen_height, min_height )
	board_ratio = 0.8
	board_size = min( screen_width, screen_height ) * board_ratio
	tile_size = board_size // 3
	margin_x = (screen_width - board_size)
	margin_y = (screen_height - board_size)
	return { 'size' : board_size, 'tile_size' : tile_size, 'margin_x' : margin_x, 'margin_y' : margin_y,
	         'line_width' : max( 2, int( board_size * 0.02 ) ) }


class Tile :
	def __init__( self, origin_symbol, origin_rect ) :
		# Core attributes
		self.type = origin_symbol
		self.marked = False
		self.rect = origin_rect
		self.scale = 0.8  # Scale of symbol
		self.load_images()
		self.resize_image()

	def load_image( self ) :
		if self.type == "x" :
			self.symbol_image = pygame.image.load( "files/X_500px.png" ).convert_alpha()
		else :
			self.symbol_image = pygame.image.load( "files/O_500px.png" ).convert_alpha()

	# if trans_factor != 1 :
	#	image.set_alpha( 255 * trans_factor )

	def resize( self ) :
		target_size = int( (self.rect.width) * self.scale )
		self.image = pygame.transform.smoothscale( self.symbol_image, (target_size, target_size) )

	def draw( self ) :
		image_rect = self.image.get_rect( center = self.rect.center )
		screen.blit( self.image, image_rect )

	""" 
	def check_hover( self , transparency_factor ) :
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint( mouse_pos ) :
			if pygame.mouse.get_pressed()[ 0 ] :
				draw
				self.marked = True
			else :
				if self.marked :
					self.marked = False
					return True
		else :
			self.marked = False
		return False
	"""


# text , w , h , pos , elevation )
class Button :
	def __init__( self, text, width, height, pos, elevation ) :
		# Core attributes
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elevation = elevation
		self.original_y_pos = pos[ 1 ]

		# top rectangle
		self.top_rect = pygame.Rect( pos, (width, height) )
		self.top_color = button_out_color

		# bottom rectangle
		self.bottom_rect = pygame.Rect( pos, (width, height) )
		self.bottom_color = button_in_color
		# text
		self.text_surf = get_font( 50 ).render( text, False, button_text_color )
		self.text_rect = self.text_surf.get_rect( center = self.top_rect.center )

	def draw( self ) :
		# elevation logic
		self.top_rect.y = self.original_y_pos - self.dynamic_elevation
		self.text_rect.center = self.top_rect.center

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

		pygame.draw.rect( screen, self.bottom_color, self.bottom_rect, border_radius = 12 )
		pygame.draw.rect( screen, self.top_color, self.top_rect, border_radius = 12 )
		screen.blit( self.text_surf, self.text_rect )

	# self.check_click()

	def check_click( self ) :
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint( mouse_pos ) :
			self.top_color = button_hover_color
			if pygame.mouse.get_pressed()[ 0 ] :
				self.dynamic_elevation = 0
				self.pressed = True
			else :
				if self.pressed :
					self.pressed = False
					return True
				self.dynamic_elevation = self.elevation
		else :
			self.dynamic_elevation = self.elevation
			self.top_color = button_in_color
			self.pressed = False
		return False


def make_board( available_w, available_h ) :
	margin = 20
	tile_size = min( available_h, available_w ) // 3 - margin * 2
	for row in range( 3 ) :
		board_col = [ ]
		for col in range( 3 ) :
			board_row = [ ]
			correct_x = margin + col * tile_size
			correct_y = margin + row * tile_size
			image = pygame.image.load( 'files/frame_500px.png' ).convert_alpha()
			image = pygame.transform.smoothscale( image, (tile_size, tile_size) )
			image_rect = image.get_rect( topleft = (correct_x, correct_y) )
			board_row.append( { 'image' : image, 'rect' : image_rect, 'symbol' : None } )
	board_col.append( board_row )
	return board_col


def play() :
	# 'size', 'tile_size' , 'margin_x', 'margin_y', 'line_width' }
	global screen_width , screen_height
	board_info = board_values()
	while True :
		board_big = make_board( screen_width, screen_height )
		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				pygame.quit()
				return
			if event.type == pygame.VIDEORESIZE :
				screen_width, screen_height = event.w, event.h
				board = make_board( screen_width, screen_height )
		screen.fill( BG_color )
		# Draw tiles
		for row in board_big :
			for tile in row :
				screen.blit( tile[ 'image' ], tile[ 'rect' ] )
		pygame.display.update()


def options() :
	while True :
		options_mouse_pos = pygame.mouse.get_pos()  # po chuj mi to ?
		screen.fill( pallete[ 1 ] )
		options_text = get_font( 50 ).render( "this is the options screen", False, pallete[ 0 ] )
		options_rect = options_text.get_rect( center = (screen_width // 2, screen_height // 2) )
		screen.blit( options_text, options_rect )

		B1 = Button( "BACK", 200, 50, (screen_width // 2 - 100, screen_height // 2 + 100), 5 )
		B1.draw()
		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				pygame.quit()
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN :
				if B1.check_click() :
					menu()
		pygame.display.update()


def menu() :
	global screen, screen_width, screen_height, BG, BG_color

	while True :
		screen.fill( BG_color )  # ograniczyc fill tylko gdy zmieniamy res
		# screen.blit( BG, (0, 0) )

		button_w = screen_width // 4
		button_h = screen_height // 12
		button_space = max( screen_height // 30, 5 )
		button_x = (screen_width - button_w) // 2
		button_y = screen_height // 3
		elevation = 5

		def next_button( p ) :
			return p + button_space + button_h

		# render menu
		player_ai = Button( "PLAYER vs AI", button_w, button_h, (button_x, button_y), elevation )
		button_y = next_button( button_y )
		player_p = Button( "PLAYER vs Player", button_w, button_h, (button_x, button_y), elevation )
		button_y = next_button( button_y )
		options_button = Button( "OPTIONS", button_w, button_h, (button_x, button_y), elevation )
		button_y = next_button( button_y )
		quit_button = Button( "QUIT", button_w, button_h, (button_x, button_y), elevation )

		menu_text = get_font( screen_width // 5 ).render( "TIK-TAK-TOE", False, Title_color )
		menu_rect = menu_text.get_rect( center = (screen_width // 2, screen_height // 6) )
		screen.blit( menu_text, menu_rect )

		menu_mouse_pos = pygame.mouse.get_pos()  # to tez po chuj mi ? juz wiem po co

		# Draw buttons
		for button in [ player_ai, player_p, options_button, quit_button ] :
			button.check_click()
			button.draw()
		# events
		for event in pygame.event.get() :
			if event.type == pygame.VIDEORESIZE :
				# Update screen dimensions and recreate the screen surface
				screen_width, screen_height = event.w, event.h
				screen = pygame.display.set_mode( (screen_width, screen_height), pygame.RESIZABLE )
				BG = pygame.Surface( (screen_width, screen_height) )
				BG.fill( BG_color )
			# if 1 == 0 :
			if event.type == pygame.MOUSEBUTTONUP :
				if player_ai.top_rect.collidepoint( event.pos ) :
					play()
				if player_p.top_rect.collidepoint( event.pos ) :
					play()
				if options_button.top_rect.collidepoint( event.pos ) :
					options()
				if quit_button.top_rect.collidepoint( event.pos ) :
					pygame.quit()
					exit()

		pygame.display.update()


menu()
