class TicTacToeGame:
    def __init__(self):
        self.tiles = [' ' for _ in range(9)]
        self.winner = None

    def display_board(self):
        for i in range(3):
            print('| ' + ' | '.join(self.tiles[i*3:(i+1)*3]) + ' |')

    def place_move(self, position, player):
        if self.tiles[position] == ' ':
            self.tiles[position] = player
            if self.check_winner(player):
                self.winner = player
            return True
        return False

    def check_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for condition in win_conditions:
            if all(self.tiles[i] == player for i in condition):
                return True
        return False

    def has_empty_tiles(self):
        return ' ' in self.tiles

    def available_positions(self):
        return [i for i, tile in enumerate(self.tiles) if tile == ' ']
