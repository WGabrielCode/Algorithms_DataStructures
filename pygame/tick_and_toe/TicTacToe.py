import pygame
from sys import exit

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

# initialize screen
screen = pygame.display.set_mode( (screen_width, screen_height), pygame.RESIZABLE )
pygame.display.set_caption( "Tic-Tac-Toe" )


def get_font( size ) :
	return pygame.font.Font( 'files/Pixeltype.ttf', size )


class Tile :
	def __init__( self, symbol, x, y, size, tile_image, X_image, O_image ) :
		self.tile_image = tile_image
		self.x_image = X_image
		self.o_image = O_image
		self.rect = pygame.Rect( x, y, size, size )
		self.type = symbol
		self.marked = False
		self.left_x = x
		self.top_y = y
		self.size = size

	def check_click( self, mouse_pos ) :
		if not self.marked and self.rect.collidepoint( mouse_pos ) and pygame.mouse.get_just_released()[ 0 ] :
			return True
		return False

	def draw( self ) :
		screen.blit( self.tile_image, self.rect )
		if self.marked :
			if self.type == 'x' :
				image = self.x_image
			elif self.type == 'o' :
				image = self.o_image
			else :
				print( "error" )
			screen.blit( image, self.rect )

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


def image_resize( image_a, image_b, image_c, size ) :
	global screen_width, screen_height

	# image_a = pygame.transform.smoothscale( image_a, (size, size) ).convert_alpha()
	image_a = pygame.transform.scale( image_a, (size, size) ).convert_alpha()
	image_b = pygame.transform.scale( image_b, (size, size) ).convert_alpha()
	image_c = pygame.transform.scale( image_c, (size, size) ).convert_alpha()
	return image_a, image_b, image_c


def check_win( board, player ) :
	# Check rows
	for i in range( 3 ) :
		for j in range( 3 ) :
			if board[ i ][ j ].type != player :
				break
		else :
			return True
	# Check columns
	for i in range( 3 ) :
		for j in range( 3 ) :
			if board[ j ][ i ].type != player :
				break
		else :
			return True
	# Check diagonals
	if (board[ 0 ][ 0 ].type == board[ 1 ][ 1 ].type == board[ 2 ][ 2 ].type == player) or (
			board[ 0 ][ 2 ].type == board[ 1 ][ 1 ].type == board[ 2 ][ 0 ].type == player) :
		return True
	return False


def check_draw( Board, empty ) :
	for i in range( 3 ) :
		for j in range( 3 ) :
			if Board[ i ][ j ].type == empty :
				return False
	return True


def minimax( Board, symbol ) :
	circle_ = 'x'
	cross_ = 'o'
	empty_ = None

	if check_win_2d( Board, 1 ) : return 1, None
	if check_win_2d( Board, 2 ) : return -1, None
	if check_draw( Board ) : return 0, None

	best_pair = (None, None)
	if symbol == circle_ :  # dla kolka
		best = -1
		for i in range( 3 ) :
			for j in range( 3 ) :
				if Board[ i ][ j ].type == empty_ :
					Board[ i ][ j ].type = symbol
					score, _ = minimax( Board, cross_ )
					Board[ i ][ j ].type = 0
					if score > best :
						best = score
						if best == 1 :
							return best, (i, j)
						best_pair = (i, j)
		return best, best_pair

	if symbol == cross_ :
		best = 3
		for i in range( 3 ) :
			for j in range( 3 ) :
				if Board[ i ][ j ].type == empty_ :
					Board[ i ][ j ].type = symbol
					score, _ = minimax( Board, 1 )
					Board[ i ][ j ].type = 0
					if score < best :
						best = score
						if best == -1 :
							return best, (i, j)
						best_pair = (i, j)
		return best, best_pair


def make_board( tile_size, tile_image, x_image, o_image ) :
	global screen_width, screen_height
	margin = 20
	board = [ ]
	for row in range( 3 ) :
		board_row = [ ]
		for col in range( 3 ) :
			correct_x = (screen_width - 3 * tile_size) // 2 + col * tile_size
			correct_y = (screen_height - 3 * tile_size) // 2 + row * tile_size
			board_row.append( Tile( None, correct_x, correct_y, tile_size, tile_image, x_image, o_image ) )
		board.append( board_row )
	return board


def play() :
	# 'size', 'tile_size' , 'margin_x', 'margin_y', 'line_width' }
	global screen_width, screen_height, BG_color, screen
	screen.fill( BG_color )
	current_player = "o"
	tile_image = pygame.image.load( 'files/frame_500px.png' ).convert_alpha()
	X_image = pygame.image.load( 'files/X_500px.png' ).convert_alpha()
	O_image = pygame.image.load( 'files/O_500px-1.png' ).convert_alpha()

	tile_size = min( screen_height, screen_width ) // 3
	tile_image, X_image, O_image = image_resize( tile_image, X_image, O_image, tile_size )
	Board = make_board( tile_size, tile_image, X_image, O_image )

	active = True
	while active :
		mouse_pos = pygame.mouse.get_pos()
		for i in range( 3 ) :
			for j in range( 3 ) :
				tile = Board[ i ][ j ]
				if tile.check_click( mouse_pos ) :
					tile.marked = True
					tile.type = current_player
					if check_win( Board , current_player ) :
						active = False
					elif check_draw( Board , None ) :
						active = False
					if current_player == 'x' :
						current_player = 'o'
					else :
						current_player = 'x'

				tile.draw()

		for event in pygame.event.get() :

			if event.type == pygame.QUIT :
				pygame.quit()
				exit()

			if event.type == pygame.VIDEORESIZE :
				# Update screen dimensions and recreate the screen surface
				screen_width, screen_height = event.w, event.h
				screen = pygame.display.set_mode( (screen_width, screen_height), pygame.RESIZABLE )
				BG = pygame.Surface( (screen_width, screen_height) )
				BG.fill( BG_color )
				tile_size = min( screen_width, screen_height ) // 3
				tile_image, X_image, O_image = image_resize( tile_image, X_image, O_image, tile_size )
				for i in range( 3 ) :
					for j in range( 3 ) :
						tile = Board[ i ][ j ]
						tile.tile_image = tile_image
						tile.o_image = O_image
						tile.x_image = X_image
						tile.size = tile_size
						tile.rect = pygame.Rect( tile.left_x, tile.top_y, tile_size, tile_size )

			if 1 == 0 :
				# if event.type == pygame.MOUSEBUTTONUP :
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

	while not active :
		menu_text = get_font( screen_width // 5 ).render( f"PLAYER { current_player.upper() } WON ", False, Title_color )
		menu_rect = menu_text.get_rect( center = (screen_width // 2, screen_height // 6) )
		screen.blit( menu_text , menu_rect )

		pygame.display.update()


def options() :
	while True :
		options_mouse_pos = pygame.mouse.get_pos()  # po chuj mi to ?
		screen.fill( BG_color )
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

		menu_text = get_font( screen_width // 5 ).render( "TIC-TAC-TOE", False, Title_color )
		menu_rect = menu_text.get_rect( center = (screen_width // 2, screen_height // 6) )
		screen.blit( menu_text, menu_rect )

		menu_mouse_pos = pygame.mouse.get_pos()  # to tez po chuj mi ? juz wiem po co

		# Draw buttons
		for button in [ player_ai, player_p, options_button, quit_button ] :
			button.check_click()
			button.draw()
		# events
		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				pygame.quit()
				exit()

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


# play()
menu()
