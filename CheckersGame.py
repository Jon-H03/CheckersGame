
from colorain import *


class Board:
    def __init__(self):
        self._board = [[None, "White", None, "White", None, "White", None, "White"],
                       ["White", None, "White", None, "White", None, "White", None],
                       [None, "White", None, "White", None, "White", None, "White"],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       ["Black", None, "Black", None, "Black", None, "Black", None],
                       [None, "Black", None, "Black", None, "Black", None, "Black"],
                       ["Black", None, "Black", None, "Black", None, "Black", None]]

    def get_board(self):
        """Returns the current board."""
        return self._board

    def update_board(self, coord: tuple, new_square_value):
        """Updates board given an ending coordinate and a piece color."""
        # Iterates through rows and then columns of board in order to find which square to update.
        for row_num in range(len(self._board)):
            if row_num == coord[0]:
                for col_num in range(len(self._board[row_num])):
                    if col_num == coord[1]:
                        self._board[row_num][col_num] = new_square_value


class Piece:
    def validate_move(self, color: str, starting_square_location: tuple, destination_square_location: tuple):
        """Validate_move makes sure the player is moving said piece in a diagonal that is one square away."""
        starting_row = starting_square_location[0]
        starting_col = starting_square_location[1]
        starting_col_copy = starting_square_location[1]
        destination_row = destination_square_location[0]
        destination_col = destination_square_location[1]

        if color == "White":
            while starting_row <= destination_row:
                if starting_row > destination_row:
                    return False
                if starting_row == destination_row and starting_col == destination_col or starting_row == destination_row and starting_col_copy == destination_col:
                    return True
                starting_row += 1
                starting_col += 1
                starting_col_copy -= 1
            else:
                return False

        if color == "Black":
            while starting_row >= destination_row:
                if starting_row < destination_row:
                    return False
                if starting_row == destination_row and starting_col == destination_col or starting_row == destination_row and starting_col_copy == destination_col:
                    return True
                starting_row -= 1
                starting_col += 1
                starting_col_copy -= 1
            else:
                return False


class King(Piece):
    def validate_move(self, color: str, starting_square_location: tuple, destination_square_location: tuple):
        """Validate_move makes sure the player is moving said king according to the rules validated by this function. """
        starting_row = starting_square_location[0]
        starting_col = starting_square_location[1]
        starting_row_copy = starting_square_location[0]
        starting_col_copy = starting_square_location[1]
        destination_row = destination_square_location[0]
        destination_col = destination_square_location[1]

        if color == "White":
            while starting_row < destination_row or starting_row > destination_row:
                if starting_row == destination_row and starting_col == destination_col or starting_row == destination_row and starting_col_copy == destination_col or \
                        starting_row_copy == destination_row and starting_col == destination_col or starting_row_copy == destination_row and starting_col_copy == destination_col:
                    return True
                starting_row += 1
                starting_col += 1
                starting_row_copy -= 1
                starting_col_copy -= 1
            else:
                return False

        if color == "Black":
            while starting_row > destination_row or starting_row < destination_row:
                if starting_row == destination_row and starting_col == destination_col or starting_row == destination_row and starting_col_copy == destination_col or \
                        starting_row_copy == destination_row and starting_col == destination_col or starting_row_copy == destination_row and starting_col_copy == destination_col:
                    return True
                starting_row += 1
                starting_col += 1
                starting_row_copy -= 1
                starting_col_copy -= 1
            else:
                return False


class TripleKing(King):
    def validate_move(self, color: str, starting_square_location: tuple, destination_square_location: tuple):
        """Validate_move makes sure the player is moving a triple king according to the rules validated by this function."""
        starting_row = starting_square_location[0]
        starting_col = starting_square_location[1]
        starting_row_copy = starting_square_location[0]
        starting_col_copy = starting_square_location[1]
        destination_row = destination_square_location[0]
        destination_col = destination_square_location[1]

        if color == "White":
            while starting_row < destination_row or starting_row > destination_row:
                if starting_row == destination_row and starting_col == destination_col or starting_row == destination_row and starting_col_copy == destination_col or \
                        starting_row_copy == destination_row and starting_col == destination_col or starting_row_copy == destination_row and starting_col_copy == destination_col:
                    return True
                starting_row += 1
                starting_col += 1
                starting_row_copy -= 1
                starting_col_copy -= 1
            else:
                return False

        if color == "Black":
            while starting_row > destination_row or starting_row < destination_row:
                if starting_row == destination_row and starting_col == destination_col or starting_row == destination_row and starting_col_copy == destination_col or \
                        starting_row_copy == destination_row and starting_col == destination_col or starting_row_copy == destination_row and starting_col_copy == destination_col:
                    return True
                starting_row += 1
                starting_col += 1
                starting_row_copy -= 1
                starting_col_copy -= 1
            else:
                return False


class Player:
    def __init__(self, name: str, color: str):
        self._name = name
        self._color = color
        self._king_count = 0
        self._triple_king_count = 0
        self._captured_pieces = 0

    def get_name(self):
        """Returns the name of the player."""
        return self._name

    def get_color(self):
        """Returns the color of the player."""
        return self._color

    def get_king_count(self):
        """Returns the amount of kings a player has."""
        return self._king_count

    def add_king(self):
        """Adds 1 to player's king count."""
        self._king_count += 1

    def remove_king(self):
        """Subtracts 1 from a player's king count."""
        self._king_count -= 1

    def get_triple_king(self):
        """Returns the amount of triple kings a player has."""
        return self._triple_king_count

    def add_triple_king(self):
        """Adds 1 to player's triple king count."""
        self._triple_king_count += 1

    def get_captured_pieces_count(self):
        """Returns amount of captured pieces a player has."""
        return self._captured_pieces

    def add_captured_piece(self):
        """Adds 1 to a player's captured pieces."""
        self._captured_pieces += 1


class OutofTurn(Exception):
    """OutofTurn exception gets raised when a player attempts to move a piece out of turn."""
    pass


class InvalidSquare(Exception):
    """InvalidSquare exception gets raised when a player does not own the checker in the present space or the location does not exist."""
    pass


class InvalidPlayer(Exception):
    """InvalidPlayer exception gets raised when a nonexistent player tries to make a move."""
    pass


class Checkers:
    def __init__(self):
        self._players = []
        self._current_turn = None # Depicted by name
        self._board = Board()
        self._winner = None

    def get_board(self):
        """Returns the board in its current state."""
        return self._board.get_board()

    def switch_current_turn(self, player_name):
        """Switches the turn to the opposing player."""
        if self._current_turn == player_name:
            for player in self._players:
                if player.get_name() != player_name:
                    self._current_turn = player.get_name()

    def piece_to_king(self, square_location):
        """Piece_to_king makes a normal piece transform into a king on either respective side."""
        square_value = self._board.get_board()[square_location[0]][square_location[1]]

        # If piece is White and on opposite end of board
        if square_value == "White" and square_location[0] == 7:
            self._board.update_board((square_location[0], square_location[1]), "White_king")
            for player in self._players:
                if player.get_color() == "White":
                    player.add_king()

        # If piece is Black and on opposite end of board
        if square_value == "Black" and square_location[0] == 0:
            self._board.update_board((square_location[0], square_location[1]), "Black_king")
            for player in self._players:
                if player.get_color() == "Black":
                    player.add_king()

    def king_to_triple_king(self, square_location):
        """king_to_triple_king can be called when a king returns back to its original side and transforms the king into
        a triple king."""
        square_value = self.get_board()[square_location[0]][square_location[1]]

        # If king is White
        if square_value == "White_king" and square_location[0] == 0:
            self._board.update_board((square_location[0], square_location[1]), "White_Triple_King")
            for player in self._players:
                if player.get_color() == "White":
                    player.add_triple_king()
                    player.remove_king()

        # If king is Black
        if square_value == "Black_king" and square_location[0] == 7:
            self._board.update_board((square_location[0], square_location[1]), "Black_Triple_King")
            for player in self._players:
                if player.get_color() == "Black":
                    player.add_triple_king()
                    player.remove_king()

    def create_player(self, player_name: str, piece_color: str):
        """Create_player function allows two players to be created which much choose either 'Black' or 'White' for their pieces."""
        # Available piece colors and a new instances of a Player.
        piece_colors = ["Black", "White"]
        player = Player(player_name, piece_color)

        # If there are already two players
        if len(self._players) >= 2:
            return "Sorry there are already two players."

        # If piece color is already taken or user input an invalid one.
        if piece_color not in piece_colors:
            return "Sorry that color is already taken."

        # If piece color is black, then we assign the first turn to black.
        if piece_color == "Black":
            self._players.append(player)
            piece_colors.remove("Black")
            self._current_turn = player_name

        # If piece color is white, we remove it from the list and append player.
        elif piece_color == "White":
            self._players.append(player)
            piece_colors.remove("White")
        return player

    def play_game(self, player_name: str, starting_square_location: tuple, destination_square_location: tuple):
        """Play_game function essentially checks necessary conditions, actively shifts and updates the board, and allows
        each player to make their turn and move their pieces, while validating that the moves made are fair and justified
        by the rules. """
        captured_pieces = 0
        player_name_list = []
        colors_list = []
        starting_square_value = self._board.get_board()[starting_square_location[0]][starting_square_location[1]]
        destination_square_value = self._board.get_board()[destination_square_location[0]][
            destination_square_location[1]]

        # Validate that there are two players created.
        if len(self._players) <= 1:
            return "Please create 2 players before starting."

        # If it is not current users turn, raise OutofTurn Exception
        if self._current_turn != player_name:
            print(self._current_turn)
            raise OutofTurn

        # Change Current Player's turn (Since we've already validated who's turn it was)
        self.switch_current_turn(player_name)

        # Append player names and colors to two list for easy access
        for player in self._players:
            player_name_list.append(player.get_name())
            colors_list.append(player.get_color())

        # If input player name is not in player name list.
        if player_name not in player_name_list:
            raise InvalidPlayer

        # If starting square location is out-of-bounds or nonexistent
        if starting_square_location[0] < 0 or starting_square_location[0] > 7:
            print("A starting square does not exist at that location.")
            raise InvalidSquare

        # If destination square location is out-of-bounds or nonexistent
        if destination_square_location[1] < 0 or destination_square_location[1] > 7:
            print("A destination square does not exist at that location.")
            raise InvalidSquare

        # If a player tries to move to a square that's already occupied
        if destination_square_value is not None:
            return f"There is already a {destination_square_value} piece present at that finishing location."

        # If a starting square contains nothing
        if starting_square_value is None:
            return "There is nothing to move in that starting space."

        # If player tries to start in a square his color is not present.
        starting_square_color = starting_square_value[:5]
        if starting_square_color != colors_list[player_name_list.index(player_name)]:
            return "You do not own that square."

        # Validate that player move is valid and check if it is a normal piece
        if starting_square_value == "Black" or starting_square_value == "White":
            piece = Piece()
            current_color = colors_list[player_name_list.index(player_name)]

            # Checks if move was valid
            if piece.validate_move(color=current_color, starting_square_location=starting_square_location,
                                   destination_square_location=destination_square_location) is True:

                # Checks if starting square contains black
                if starting_square_value == "Black":
                    row_difference = destination_square_location[0] - starting_square_location[0]
                    col_difference = destination_square_location[1] - starting_square_location[1]
                    current_row = starting_square_location[0]
                    current_col = starting_square_location[1]

                    # Moves 1 diagonal at a time to check if it has jumped over any opposing pieces.
                    while current_row != destination_square_location[0] and current_col != destination_square_location[1]:
                        if current_row > destination_square_location[0]:
                            current_row -= 1
                        if col_difference > 0 and current_col < destination_square_location[1]:
                            current_col += 1
                        if col_difference < 0 and current_col > destination_square_location[1]:
                            current_col -= 1

                        # If a white piece (Including White King or White Triple King) is hopped over.
                        if self._board.get_board()[current_row][current_col] == "White" or \
                                self._board.get_board()[current_row][current_col] == "White_king" or \
                                self._board.get_board()[current_row][current_col] == "White_Triple_King":
                            self._board.update_board((current_row, current_col), None)
                            for player in self._players:
                                if player.get_color() == "Black":
                                    captured_pieces += 1
                                    player.add_captured_piece()

                # Checks if starting square contains white
                if starting_square_value == "White":
                    row_difference = destination_square_location[0] - starting_square_location[0]
                    col_difference = destination_square_location[1] - starting_square_location[1]
                    current_row = starting_square_location[0]
                    current_col = starting_square_location[1]

                    # Moves 1 diagonal at a time to check if it has jumped over any opposing pieces.
                    while current_row != destination_square_location[0] and current_col != destination_square_location[1]:
                        if current_row < destination_square_location[0]:
                            current_row += 1
                        if col_difference < 0 and current_col > destination_square_location[1]:
                            current_col -= 1
                        if col_difference > 0 and current_col < destination_square_location[1]:
                            current_col += 1

                        # Checks if it has jumped over any Black pieces
                        if self._board.get_board()[current_row][current_col] == "Black" or \
                                self._board.get_board()[current_row][current_col] == "Black_king" or \
                                self._board.get_board()[current_row][current_col] == "Black_Triple_King":
                            self._board.update_board((current_row, current_col), None)
                            for player in self._players:
                                if player.get_color() == "White":
                                    captured_pieces += 1
                                    player.add_captured_piece()

            else:
                return "That was an invalid move. Please try again."

        # Check if the starting square contains a King piece.
        if starting_square_value == "White_king" or starting_square_value == "Black_king":
            king = King()
            current_color = colors_list[player_name_list.index(player_name)]

            # Checks if the player made a valid move for the king.
            if king.validate_move(color=current_color, starting_square_location=starting_square_location,
                                  destination_square_location=destination_square_location) is True:

                # Checks if starting square contains a Black King.
                if starting_square_value == "Black_king":
                    row_difference = destination_square_location[0] - starting_square_location[0]
                    col_difference = destination_square_location[1] - starting_square_location[1]
                    current_row = starting_square_location[0]
                    current_col = starting_square_location[1]

                    # Moves 1 diagonal forward or backward at a time in order to see if any opposing pieces were hopped over.
                    while current_row != destination_square_location[0] and current_col != destination_square_location[1]:
                        if current_row > destination_square_location[0]:
                            current_row -= 1
                        if current_row < destination_square_location[0]:
                            current_row += 1
                        if col_difference > 0 and current_col < destination_square_location[1]:
                            current_col += 1
                        if col_difference < 0 and current_col > destination_square_location[1]:
                            current_col -= 1

                        # Check if a White piece was hopped over.
                        if self._board.get_board()[current_row][current_col] == "White" or \
                                self._board.get_board()[current_row][current_col] == "White_king" or \
                                self._board.get_board()[current_row][current_col] == "White_Triple_King":
                            self._board.update_board((current_row, current_col), None)
                            for player in self._players:
                                if player.get_color() == "Black":
                                    captured_pieces += 1
                                    player.add_captured_piece()

                # Checks if starting square contains a White King.
                if starting_square_value == "White_king":
                    row_difference = destination_square_location[0] - starting_square_location[0]
                    col_difference = destination_square_location[1] - starting_square_location[1]
                    current_row = starting_square_location[0]
                    current_col = starting_square_location[1]

                    # Moves 1 diagonal forward or backward at a time in order to see if any opposing pieces were hopped over.
                    while current_row != destination_square_location[0] and current_col != destination_square_location[1]:
                        if current_row < destination_square_location[0]:
                            current_row += 1
                        if current_row > destination_square_location[0]:
                            current_row -= 1
                        if col_difference < 0 and current_col > destination_square_location[1]:
                            current_col -= 1
                        if col_difference > 0 and current_col < destination_square_location[1]:
                            current_col += 1

                        # Checks if any black pieces were hopped over.
                        if self._board.get_board()[current_row][current_col] == "Black" or \
                                self._board.get_board()[current_row][current_col] == "Black_king" or \
                                self._board.get_board()[current_row][current_col] == "Black_Triple_King":
                            self._board.update_board((current_row, current_col), None)
                            for player in self._players:
                                if player.get_color() == "White":
                                    captured_pieces += 1
                                    player.add_captured_piece()

        # Check if the starting square contains a Triple King piece.
        if starting_square_value == "Triple_White_King" or starting_square_value == "Triple_Black_King":
            king = King()
            current_color = colors_list[player_name_list.index(player_name)]

            # Checks if the player made a valid move for the king.
            if king.validate_move(color=current_color, starting_square_location=starting_square_location,
                                  destination_square_location=destination_square_location) is True:

                # Checks if starting square contains a Black King.
                if starting_square_value == "Triple_Black_King":
                    row_difference = destination_square_location[0] - starting_square_location[0]
                    col_difference = destination_square_location[1] - starting_square_location[1]
                    current_row = starting_square_location[0]
                    current_col = starting_square_location[1]

                    # Moves 1 diagonal forward or backward at a time in order to see if any opposing pieces were hopped over.
                    while current_row != destination_square_location[0] and current_col != destination_square_location[1]:
                        if current_row > destination_square_location[0]:
                            current_row -= 1
                        if current_row < destination_square_location[0]:
                            current_row += 1
                        if col_difference > 0 and current_col < destination_square_location[1]:
                            current_col += 1
                        if col_difference < 0 and current_col > destination_square_location[1]:
                            current_col -= 1

                        # Check if a White piece was hopped over.
                        if self._board.get_board()[current_row][current_col] == "White" or \
                                self._board.get_board()[current_row][current_col] == "White_king" or \
                                self._board.get_board()[current_row][current_col] == "White_Triple_King":
                            self._board.update_board((current_row, current_col), None)
                            for player in self._players:
                                if player.get_color() == "Black":
                                    captured_pieces += 1
                                    player.add_captured_piece()

                # Checks if starting square contains a White King.
                if starting_square_value == "Triple_White_King":
                    row_difference = destination_square_location[0] - starting_square_location[0]
                    col_difference = destination_square_location[1] - starting_square_location[1]
                    current_row = starting_square_location[0]
                    current_col = starting_square_location[1]

                    # Moves 1 diagonal forward or backward at a time in order to see if any opposing pieces were hopped over.
                    while current_row != destination_square_location[0] and current_col != destination_square_location[1]:
                        if current_row < destination_square_location[0]:
                            current_row += 1
                        if current_row > destination_square_location[0]:
                            current_row -= 1
                        if col_difference < 0 and current_col > destination_square_location[1]:
                            current_col -= 1
                        if col_difference > 0 and current_col < destination_square_location[1]:
                            current_col += 1

                        # Checks if any black pieces were hopped over.
                        if self._board.get_board()[current_row][current_col] == "Black" or \
                                self._board.get_board()[current_row][current_col] == "Black_king" or \
                                self._board.get_board()[current_row][current_col] == "Black_Triple_King":
                            self._board.update_board((current_row, current_col), None)
                            for player in self._players:
                                if player.get_color() == "White":
                                    captured_pieces += 1
                                    player.add_captured_piece()

        # Iterates through rows and columns and replaces starting square with None and replaces destination square with player's color.
        # Also checks if it needs to upgrade pieces to kings or triple kings.
        for row_num in range(len(self._board.get_board())):
            if row_num == starting_square_location[0]:
                for col_num in range(len(self._board.get_board())):
                    if col_num == starting_square_location[1]:
                        color_index = player_name_list.index(player_name)
                        self._board.update_board(starting_square_location, None)
                        self._board.update_board(destination_square_location, starting_square_value)
                        if destination_square_location[0] == 0:
                            self.piece_to_king(destination_square_location)
                        if destination_square_location[0] == 7:
                            self.piece_to_king(destination_square_location)
                        if starting_square_value == "White_king" and destination_square_location[0] == 0:
                            self.king_to_triple_king(destination_square_location)
                        if starting_square_value == "Black_king" and destination_square_location[0] == 7:
                            self.king_to_triple_king(destination_square_location)

        # Return their captured pieces this turn if all else passes
        return captured_pieces

    def get_checker_details(self, square_location: tuple):
        """Gets details of what's present in square."""
        # Iterates through the rows and columns to find the right square to return.
        for row_num in range(len(self._board.get_board())):
            if row_num == square_location[0]:
                for col_num in range(len(self._board.get_board()[row_num])):
                    if col_num == square_location[1]:
                        return self._board.get_board()[row_num][col_num]

    def print_board(self):
        """Prints the board in its current state."""
        # Iterate through each row and print it
        for row in self._board.get_board():
            print(f"{row}\n")

    def game_winner(self):
        """Returns the game winner, if there is one. Otherwise, will return the current leader."""
        # Check if there is a game winner.
        for player in self._players:
            if player.get_captured_pieces_count() == 12:
                self._winner = player.get_name()
                return self._winner

        if self._winner is None:
            return "Game has not ended"
        else:
            return self._winner

    def draw_board(self):
        """Draws the board as an ASCII graphic.
        Requires 'colorain' to be installed.
        Assumes the board is stored as self._board[row][column]
        """
        white_piece_types = ["White", "White_king", "White_Triple_King"]
        black_piece_types = ["Black", "Black_king", "Black_Triple_King"]

        white_square = "<b=gr>"
        black_square = "<b=k>"
        white_piece = "<f=r>"
        black_piece = "<f=b>"
        start_counter = 0

        print("\n 01234567")
        for i in range(0, 8):
            string = ""
            counter = start_counter
            string += str(i)
            for j in range(0, 8):
                # Set background color
                if counter % 2 == 0:
                    string += white_square
                else:
                    string += black_square

                # Set piece color
                if self._board.get_board()[i][j] in white_piece_types:
                    string += white_piece
                if self._board.get_board()[i][j] in black_piece_types:
                    string += black_piece

                # Print piece type (O is normal, K is King, T is Triple King)
                if self._board.get_board()[i][j] == "White" or self._board.get_board()[i][j] == "Black":
                    string += "O"
                elif self._board.get_board()[i][j] == "White_king" or self._board.get_board()[i][j] == "Black_king":
                    string += "K"
                elif self._board.get_board()[i][j] == "White_Triple_King" or self._board.get_board()[i][j] == "Black_Triple_King":
                    string += "T"
                else:
                    string += " "
                counter += 1

            start_counter += 1
            print(StyledText(string + "</></>"))
        print(" 01234567")

board = Board()
checkers = Checkers()
checkers.draw_board()
