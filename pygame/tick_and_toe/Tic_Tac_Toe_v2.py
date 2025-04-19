import pygame
from sys import exit


class GameConfigClass :
	def __init__( self ) :
		pygame.init()
		self.pallete_list_inition()
		self.colors_inition()
		self.screen_inition()
		self.load_images()

	def screen_inition( self ) :
		screen_info = pygame.display.Info()
		self.screen_width = max( screen_info.current_w - 100, 300 )
		self.screen_height = max( screen_info.current_h - 100, 300 )
		self.screen = pygame.display.set_mode( (self.screen_width, self.screen_height), pygame.RESIZABLE )
		pygame.display.set_caption( "Tic-Tac-Toe" )

	# def handle_resize( self ) :

	def load_images( self ) :
		self.tile_img = pygame.image.load( 'files/frame_500px.png' ).convert_alpha()
		self.x_img = pygame.image.load( 'files/X_500px.png' ).convert_alpha()
		self.o_img = pygame.image.load( 'files/O_500px-1.png' ).convert_alpha()
		self.horizontal_column_img = pygame.image.load( 'files/verrtical_column.png' ).convert_alpha()
		self.oblique_column_lt_rb_img = pygame.image.load( 'files/oblique_column.png' ).convert_alpha()

	def get_font( self, size ) :
		return pygame.font.Font( 'files/Pixeltype.ttf', size )

	def pallete_list_inition( self ) :  # colors https://lospec.com/palette-list/slso8
		self.pallete = [ '#0d2b45',  # 0
		                 '#203c56',  # 1
		                 '#544e68',  # 2
		                 '#8d697a',  # 3
		                 '#d08159',  # 4
		                 '#ffaa5e',  # 5
		                 '#ffd4a3',  # 6
		                 '#ffecd6'  # 7
		                 ]

	def colors_inition( self ) :
		self.lines_color = self.pallete[ 0 ]
		self.BG_color = self.pallete[ 0 ]
		self.Title_color = self.pallete[ 5 ]
		self.button_out_color = self.pallete[ 5 ]
		self.button_in_color = self.pallete[ 1 ]
		self.button_text_color = self.pallete[ 5 ]
		self.button_hover_color = self.pallete[ 2 ]

	def images_resize( self, size ) :
		self.x_img = pygame.transform.scale( self.x_img, (size, size) ).convert_alpha()
		self.o_img = pygame.transform.scale( self.o_img, (size, size) ).convert_alpha()
		self.tile_img = pygame.transform.scale( self.tile_img, (size, size) ).convert_alpha()


class Tile :
	def __init__( self, config, symbol, x, y, size ) :
		self.config = config
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
		self.config.screen.blit( self.config.tile_img, self.rect )
		if self.marked :
			if self.type == 'x' :
				image = self.config.x_img
			elif self.type == 'o' :
				image = self.config.o_img
			else :
				print( "error" )
			self.config.screen.blit( image, self.rect )

	def images_resize( self, size ) :
		self.config.x_img = pygame.transform.scale( self.config.x_img, (size, size) ).convert_alpha()
		self.config.o_img = pygame.transform.scale( self.config.o_img, (size, size) ).convert_alpha()
		self.config.tile_img = pygame.transform.scale( self.config.tile_img, (size, size) ).convert_alpha()

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


class BoardClass :
	def __init__( self, config ) :
		self.config = config
		self.tile_size = self.tile_size_calculate()
		self.board_of_tiles = self.make_board()
		self.board_size = 3
		self.empty_tile = None

	def tile_size_calculate( self ) :
		return min( self.config.screen_height, self.config.screen_width ) // 3

	def make_board( self ) :
		board = [ ]
		self.tile_size = self.tile_size_calculate()
		for row in range( 3 ) :
			board_row = [ ]
			for col in range( 3 ) :
				correct_x = (self.config.screen_width - 3 * self.tile_size) // 2 + col * self.tile_size
				correct_y = (self.config.screen_height - 3 * self.tile_size) // 2 + row * self.tile_size
				board_row.append( Tile( self.config, None, correct_x, correct_y, self.tile_size ) )
			board.append( board_row )
		return board

	def check_win( self, player ) :
		for i in range( self.board_size ) :
			for j in range( self.board_size ) :
				if self.board_of_tiles[ i ][ j ].type != player :
					break
			else :
				return True
		for i in range( self.board_size ) :
			for j in range( self.board_size ) :
				if self.board_of_tiles[ j ][ i ].type != player :
					break
			else :
				return True
		if (self.board_of_tiles[ 0 ][ 0 ].type == self.board_of_tiles[ 1 ][ 1 ].type == self.board_of_tiles[ 2 ][
			2 ].type == player) or (
				self.board_of_tiles[ 0 ][ 2 ].type == self.board_of_tiles[ 1 ][ 1 ].type == self.board_of_tiles[ 2 ][
			0 ].type == player) :
			return True
		return False

	def check_draw( self ) :
		for i in range( 3 ) :
			for j in range( 3 ) :
				if self.board_of_tiles[ i ][ j ].type == self.empty_tile :
					return False
		return True

	"""
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
"""  # minimax


# text , w , h , pos , elevation )
class Button :
	def __init__( self, config, text, text_size, width, height, pos, elevation ) :
		# Core attributes
		self.config = config
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elevation = elevation
		self.original_y_pos = pos[ 1 ]
		self.text = text
		self.pos = pos

		# top rectangle
		self.top_rect = pygame.Rect( self.pos, (width, height) )
		self.top_color = self.config.button_out_color

		# bottom rectangle
		self.bottom_rect = pygame.Rect( pos, (width, height) )
		self.bottom_color = self.config.button_in_color

		# text
		self.text_surf = (self.config.get_font( text_size )).render( text, False, config.button_text_color )
		self.text_rect = self.text_surf.get_rect( center = self.top_rect.center )

	def resize( self ) :
		self.text_surf = (self.config.get_font( self.text_size )).render( self.text, False,
		                                                                  self.config.button_text_color )
		self.text_rect = self.text_surf.get_rect( center = self.top_rect.center )
		self.bottom_rect = pygame.Rect( self.pos, (self.width, self.height) )
		self.original_y_pos = self.pos[ 1 ]
		self.top_rect = pygame.Rect( self.pos, (self.width, self.height) )

	def draw( self ) :
		# elevation logic
		self.top_rect.y = self.original_y_pos - self.dynamic_elevation
	#	self.text_rect.center = self.top_rect.center

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

		pygame.draw.rect( self.config.screen, self.bottom_color, self.bottom_rect, border_radius = 12 )
		pygame.draw.rect( self.config.screen, self.top_color, self.top_rect, border_radius = 12 )
		self.config.screen.blit( self.text_surf, self.text_rect )

	def check_click( self ) :
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint( mouse_pos ) :
			self.top_color = self.config.button_hover_color
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
			self.top_color = self.config.button_in_color
			self.pressed = False
		return False


def main_game() :
	# Initialize game configuration
	config = GameConfigClass()

	def play() :
		# Initialize game board
		board = BoardClass( config )
		current_player = "o"
		game_active = True
		winner = None

		# Handle window resize
		config.screen_inition()
		board.tile_size = min( config.screen_height, config.screen_width ) // 3
		config.images_resize( board.tile_size )

		while True :
			mouse_pos = pygame.mouse.get_pos()

			# Handle events
			for event in pygame.event.get() :
				if event.type == pygame.QUIT :
					pygame.quit()
					exit()

				if event.type == pygame.VIDEORESIZE :
					# Handle window resize
					config.screen_inition()
					board.tile_size = min( config.screen_height, config.screen_width ) // 3
					config.images_resize( board.tile_size )

					"""
					config.screen_width, config.screen_height = event.w, event.h
					config.screen = pygame.display.set_mode( (config.screen_width, config.screen_height),
					                                         pygame.RESIZABLE )
					# Resize all elements
					board.tile_size = min( config.screen_height, config.screen_width ) // 3
					config.images_resize( board.tile_size )
					board.board_of_tiles = board.make_board()
					"""

				if game_active and event.type == pygame.MOUSEBUTTONUP :
					# Handle tile clicks
					for row in board.board_of_tiles :
						for tile in row :
							if tile.check_click( mouse_pos ) and not tile.marked :
								tile.marked = True
								tile.type = current_player

								# Check game state
								if board.check_win( current_player ) :
									game_active = False
									winner = current_player
								elif board.check_draw() :
									game_active = False

								# Switch player
								current_player = 'o' if current_player == 'x' else 'x'

			# Draw everything
			config.screen.fill( config.BG_color )

			# Draw board tiles
			for row in board.board_of_tiles :
				for tile in row :
					tile.draw()

			# Draw game over message if needed
			if not game_active :
				if winner :
					message = f"PLAYER {winner.upper()} WON!"
				else :
					message = "DRAW!"

				menu_text = config.get_font( config.screen_width // 5 ).render( message, False, config.Title_color )
				menu_rect = menu_text.get_rect( center = (config.screen_width // 2, config.screen_height // 6) )
				config.screen.blit( menu_text, menu_rect )

				# Add back to menu button
				back_button = Button( config, "BACK TO MENU", 50, config.screen_width // 3, config.screen_height // 10,
				                      (config.screen_width // 2 - config.screen_width // 6, config.screen_height // 2),
				                      5 )
				back_button.draw()
				back_button.check_click()


			pygame.display.update()

	def options() :
		while True :
			config.screen.fill( config.BG_color )

			options_text = config.get_font( 50 ).render( "This is the options screen", False, config.pallete[ 0 ] )
			options_rect = options_text.get_rect( center = (config.screen_width // 2, config.screen_height // 2) )
			config.screen.blit( options_text, options_rect )

			back_button = Button( config, "BACK", config.screen_width // 4, config.screen_height // 10, (
				config.screen_width // 2 - config.screen_width // 8, config.screen_height // 2 + 100), 5 )
			back_button.draw()

			for event in pygame.event.get() :
				if event.type == pygame.QUIT :
					pygame.quit()
					exit()

				if back_button.check_click() :
					return  # Exit options

			pygame.display.update()

	def text_size_calculate( text, weidth ) :
		return int( weidth / len( text ) * 1.5 )

	def button_values( config ) :
		button_w = config.screen_width // 4
		button_h = config.screen_height // 12
		button_space = max( config.screen_height // 30, 5 )
		button_x = (config.screen_width - button_w) // 2
		button_y = config.screen_height // 3
		elevation = 5

		return button_w, button_h, button_space, button_x, button_y, elevation

	def menu() :
		# calculate button values
		button_w, button_h, button_space, button_x, button_y, elevation = button_values( config )

		def next_button( p ) :
			return p + button_space + button_h

		title_list = [ 'PLAYER VS AI', "PLAYER VS PLAYER", 'OPTIONS', "QUIT " ]
		# Create buttons
		player_ai = Button( config, title_list[ 0 ], text_size_calculate( title_list[ 0 ], button_w ), button_w,
		                    button_h, (button_x, button_y), elevation )
		button_y = next_button( button_y )
		player_p = Button( config, title_list[ 1 ], text_size_calculate( title_list[ 1 ], button_w ), button_w,
		                    button_h, (button_x, button_y), elevation )
		button_y = next_button( button_y )
		options_button = Button( config, title_list[ 2 ], text_size_calculate( title_list[ 2 ], button_w ), button_w,
		                    button_h, (button_x, button_y), elevation )
		button_y = next_button( button_y )
		quit_button = Button( config, title_list[ 3 ], text_size_calculate( title_list[ 3 ], button_w ), button_w,
		                    button_h, (button_x, button_y), elevation )

		# calculate
		menu_text = config.get_font( config.screen_width // 5 ).render( "TIC-TAC-TOE", False, config.Title_color )
		menu_rect = menu_text.get_rect( center = (config.screen_width // 2, config.screen_height // 6) )

		# List of buttons creation
		buttons = [ player_ai, player_p, options_button, quit_button ]
		while True :
			config.screen.fill( config.BG_color )
			config.screen.blit( menu_text, menu_rect )

			# Draw and handle buttons
			for button in buttons :
				button.check_click()
				button.draw()

			# Handle events
			for event in pygame.event.get() :
				if event.type == pygame.QUIT :
					pygame.quit()
					exit()

				if event.type == pygame.VIDEORESIZE :
					# Handle window
					config.screen_inition()
					# Handle Title
					menu_text = config.get_font( config.screen_width // 5 ).render( "TIC-TAC-TOE", False,
					                                                                config.Title_color )
					menu_rect = menu_text.get_rect( center = (config.screen_width // 2, config.screen_height // 6) )
					# Handle buttons

					button_w, button_h, button_space, button_x, button_y, _ = button_values( config )
					for button in buttons :
						button.width = button_w
						button.height = button_h
						button.text_size = text_size_calculate( button.text, button_w )
						button.pos = (button_x, button_y)
						button_y = next_button( button_y )
						button.resize()
					"""
					config.screen_width, config.screen_height = max( event.w , 300 ) , max( event.h , 300 )
					config.screen = pygame.display.set_mode( (config.screen_width, config.screen_height),                                      pygame.RESIZABLE )
					config.screen.fill( config.BG_color )
					"""

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

		# Start with the menu
		menu()

	menu()


main_game()
"""
def main_game() :
	config = GameConfigClass

	def play() :

		config.screen.fill( BG_color )
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
						if check_win( Board, current_player ) :
							active = False
						elif check_draw( Board, None ) :
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
			menu_text = get_font( screen_width // 5 ).render( f"PLAYER {current_player.upper()} WON ", False,
			                                                  Title_color )
			menu_rect = menu_text.get_rect( center = (screen_width // 2, screen_height // 6) )
			screen.blit( menu_text, menu_rect )

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
"""
