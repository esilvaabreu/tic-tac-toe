# Importing necessary functions
from tic_tac_toe import intro_game, play_game

# Creating the initial variables
player_1_shape, player_2_shape, coord_dict = intro_game()

# Executing main function
play_game(player_1_shape, player_2_shape, coord_dict)
