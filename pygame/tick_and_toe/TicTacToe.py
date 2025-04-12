import pygame
from sys import exit
from random import randint, choice

# initialize pygame
pygame.init()

# Deafault screen sizee
screen_info = pygame.display.Info()
screen_width = screen_info.current_w - 100
screen_height = screen_info.current_h - 100

BG = pygame.Surface( (screen_width, screen_height) )

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
BG_color = pallete[ 1 ]

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


def board_placement() :
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


# text , w , h , pos , elevation )
class Button :
	def __init__( self, text, width, height, pos, elevation ) :
		# Core attributes
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[ 1 ]

		# top rectangle
		self.top_rect = pygame.Rect( pos, (width, height) )
		self.top_color = '#475F77'

		# bottom rectangle
		self.bottom_rect = pygame.Rect( pos, (width, height) )
		self.bottom_color = '#354B5E'
		# text
		self.text_surf = get_font( 50 ).render( text, False, pallete[0] )
		self.text_rect = self.text_surf.get_rect( center = self.top_rect.center )

	def draw( self ) :
		# elevation logic
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect( screen, self.bottom_color, self.bottom_rect, border_radius = 12 )
		pygame.draw.rect( screen, self.top_color, self.top_rect, border_radius = 12 )
		screen.blit( self.text_surf, self.text_rect )
		#self.check_click()

	def check_click( self ) :
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint( mouse_pos ) :
			self.top_color = '#D74B4B'
			if pygame.mouse.get_pressed()[ 0 ] :
				self.dynamic_elecation = 0
				self.pressed = True
			else :
				if self.pressed :
					self.pressed = False
					return True
				self.dynamic_elecation = self.elevation
		else :
			self.dynamic_elecation = self.elevation
			self.top_color = '#475F77'
			self.pressed = False
		return False

def play() :
	while True :
		screen.fill( pallete[ 0 ] )
		pygame.display.update()


def options() :
	while True :
		options_mouse_pos = pygame.mouse.get_pos() # po chuj mi to ?
		screen.fill( pallete[ 1 ] )
		options_text = get_font( 50 ).render( "this is the options screen", False, pallete[ 0 ] )
		options_rect = options_text.get_rect( center = (screen_width // 2, screen_height // 2) )
		screen.blit( options_text, options_rect )

		B1 = Button( "Back", 200, 50, (screen_width // 2 - 100, screen_height // 2 + 100), 5 )
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
	global screen, screen_width, screen_height, BG
	while True :
		screen.fill( pallete[0])
		screen.blit( BG, (0, 0) )

		menu_mouse_pos = pygame.mouse.get_pos() # to tez po chuj mi ?

		button_w = screen_width // 4
		button_h = screen_height // 12
		button_space = max( screen_height // 30, 5 )
		button_x = (screen_width - button_w) // 2
		button_y = screen_height // 3
		e = 5

		menu_text = get_font( screen_width // 5 ).render( "MAIN MENU", False, pallete[5] )
		menu_rect = menu_text.get_rect( center = (screen_width // 2, screen_height // 6) )
		screen.blit( menu_text , menu_rect )

		def next_button( p ) :
			return p + button_space + button_h
		# render menu
		player_ai = Button( "PLAYER vs AI", button_w, button_h, (button_x, button_y), e )
		button_y = next_button( button_y )
		player_p = Button( "PLAYER vs Player", button_w, button_h, (button_x, button_y), e )
		button_y = next_button( button_y )
		options_button = Button( "OPTIONS", button_w , button_h , (button_x, button_y), e )
		button_y = next_button( button_y )
		quit_button = Button( "QUIT", button_w, button_h , (button_x, button_y), e )

		# Draw buttons
		for button in [ player_ai, player_p, options_button, quit_button ] :
			button.draw()

		#events
		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				pygame.quit()
				exit()
			if event.type == pygame.VIDEORESIZE :
				# Update screen dimensions and recreate the screen surface
				screen_width, screen_height = event.w, event.h
				screen = pygame.display.set_mode( (screen_width, screen_height), pygame.RESIZABLE )
				BG = pygame.Surface( (screen_width, screen_height) )
				BG.fill( pallete[0] )

			if event.type == pygame.MOUSEBUTTONUP:  # Zmiana na MOUSEBUTTONUP
				if player_ai.top_rect.collidepoint( event.pos ) :
					play()
				if player_p.top_rect.collidepoint( event.pos ) :
					play()
				if options_button.top_rect.collidepoint( event.pos ) :
					options()
				if quit_button.top_rect.collidepoint( event.pos ) :
					pygame.quit()
					exit()
			"""
			if event.type == pygame.MOUSEBUTTONUP :
				if player_ai.check_click():
					play()
				if player_p.check_click() :
					play()
				if options_button.check_click() :
					options()
				if quit_button.check_click() :
					pygame.quit()
					exit()
			"""
		pygame.display.update()
menu()
