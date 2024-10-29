# Create a grid example to be displayed later
coord_example = {
        'a1': ' ', 'a2': ' ', 'a3': ' ',
        'b1': ' ', 'b2': 'X', 'b3': ' ',
        'c1': ' ', 'c2': ' ', 'c3': ' '}

def show_grid(coords):
    """Prints the coord grid according to the coords matrix inserted"""

    # Print the grid header
    print('        | 1 | 2 | 3')
    print('--------------------')

    # Print each row of the grid
    for row in ['a', 'b', 'c']:
        print(f'{row} ->    | {coords[row + "1"]} | {coords[row + "2"]} | {coords[row + "3"]}')
        print('--------------------')

    return ''

def intro_game():
    """Starts the game by returning the players chosen shapes and the initial coordinates grid"""
    # Initialize game board
    coord_dict = {f'{row}{col}': ' ' for row in 'abc' for col in '123'}

    # Determine player shapes
    player_1_shape = input('Welcome to the TIC-TAC-TOE Game.\nDo you want to play as X or O? ').upper()
    if player_1_shape not in ['X', 'O']:
        print("Invalid choice. Defaulting to X.")
        player_1_shape = 'X'
    player_2_shape = 'O' if player_1_shape == 'X' else 'X'

    # Explain how to play
    print(f'\nGreat. You will be {player_1_shape}. To play, enter the coordinates corresponding to the place on the grid you want to fill.\n'
          'For example, entering b2 will place your mark in row b, column 2:')
    show_grid(coord_example)

    # Wait for user to start the game
    while input('\nWhen you are ready to start, enter "Y": ').strip().upper() != 'Y':
        pass

    return player_1_shape, player_2_shape, coord_dict

def play_game(player_1_shape, player_2_shape, coord_dict):
    """Main function. Loops until the game is finished. Receives the player's shapes and initial coord grid.
    Checks for each player's input and finishes the game"""

    def is_board_full():
        """Check if there is still available slots on the main grid and returns True or False"""

        return all(value != ' ' for value in coord_dict.values())

    while True:
        # Player 1's turn
        show_grid(coord_dict)
        while True:
            p1_play = input('\nPlayer 1 turn: insert the coordinates to mark in the grid: ').lower()
            if check_input(p1_play, coord_dict):
                coord_dict[p1_play] = player_1_shape
                break
            else:
                print("Invalid move. Please try again.")

        winner, coord_dict_win = check_winner(coord_dict)
        if winner:
            show_grid(coord_dict_win)
            print('Congratulations Player 1! You won!')
            return

        if is_board_full():
            show_grid(coord_dict)
            print('The game is a draw!')
            return

        # Player 2's turn
        show_grid(coord_dict)
        while True:
            p2_play = input('\nPlayer 2 turn: insert the coordinates to mark in the grid: ').lower()
            if check_input(p2_play, coord_dict):
                coord_dict[p2_play] = player_2_shape
                break
            else:
                print("Invalid move. Please try again.")

        winner, coord_dict_win = check_winner(coord_dict)
        print(winner)
        if winner:
            show_grid(coord_dict_win)
            print('Congratulations Player 2! You won!')
            return

        if is_board_full():
            show_grid(coord_dict)
            print('The game is a draw!')
            return

def check_input(player_play, coord_dict):
    """ Check if player_play is a valid key and its value is a space.
    Returns True or False"""

    if player_play in coord_dict and coord_dict[player_play] == ' ':
        return True
    print('You have entered an invalid coord. Please try again!\n')
    return False


def check_winner(coord_dict):
    """Receives the coord grid and check the rows, diagonals and columns for a winner condition.
    Returns True or False."""

    # Check rows
    for row in 'abc':
        if coord_dict[row + '1'] == coord_dict[row + '2'] == coord_dict[row + '3'] != ' ':
            for n in '123':
                coord_dict[row + n] = '-'
            return True, coord_dict

    # Check columns
    for column in '123':
        if coord_dict['a' + column] == coord_dict['b' + column] == coord_dict['c' + column] != ' ':
            for n in 'abc':
                coord_dict[n + column] = '|'
            return True, coord_dict

    # Check diagonals
    if coord_dict['a1'] == coord_dict['b2'] == coord_dict['c3'] != ' ':
        coord_dict['a1'] = '\\'
        coord_dict['b2'] = '\\'
        coord_dict['c3'] = '\\'
        return True, coord_dict

    if coord_dict['a3'] == coord_dict['b2'] == coord_dict['c1'] != ' ':
        coord_dict['a3'] = '/'
        coord_dict['b2'] = '/'
        coord_dict['c1'] = '/'
        return True, coord_dict


    # No winner
    return False, coord_dict