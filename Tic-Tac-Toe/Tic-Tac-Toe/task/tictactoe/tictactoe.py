import string
class TicTacToe:

    def __init__(self):
        self.accepted = ['X', 'O', '_', ' ']
        self.start = []
        while any(elem not in self.accepted for elem in self.start) or len(self.start) < 9 or len(self.start) > 9:
            self.start = list(input('Enter cells: '))
            if len(self.start) < 9:
                print("Length needs to be at least 9 symbols.")
            elif len(self.start) > 9:
                print("Please only input 9 symbols.")
            elif any(elem not in self.accepted for elem in self.start):
                print("Please only use symbols X, O, _, or a space")
        self.start = [' ' if elem == '_' else elem for elem in self.start]
        self.playing_grid = [self.start[:3], self.start[3:6], self.start[6:9]]
        print(self.playing_grid)
        self.wins = [self.start[:3], self.start[3:6], self.start[6:9],
                     self.start[:7:3], self.start[1:8:3], self.start[2:9:3],
                     self.start[:9:4], self.start[2:7:2]]

    def game_board(self):
        self.game_board = [["---------"],
                      ['| ', " ".join(self.playing_grid[0]), ' |'],
                      ['| ', " ".join(self.playing_grid[1]), ' |'],
                      ['| ', " ".join(self.playing_grid[2]), ' |'],
                      ["---------"]
                      ]
        for row in self.game_board:
            print("".join(row))

    def game_state(self):
        if 'XXX' in self.wins and 'OOO' in self.wins:
            print('Impossible')
        elif abs(self.start.count('X') - self.start.count('O')) > 1:
            print('Impossible')
        elif 'XXX' in self.wins:
            print('X wins')
        elif 'OOO' in self.wins:
            print('O wins')
        # elif self.start.count('_') > 0:
        #     print('Game not finished')
        elif self.start.count(' ') == 0:
            print('Draw')

    def moves(self):
        self.game_board()
        self.game_state()
        while True:
            self.move = input('Enter the coordinates: ').split()
            if any(coord not in string.digits  for coord in self.move):
                print("You should enter numbers!")
                continue
            int_coord = [int(coord) for coord in self.move]
            if any(coord < 1 or coord > 3 for coord in int_coord):
                print("Coordinates should be from 1 to 3!")
                continue
            grid_coord = [-1 * (int_coord[1] - 3), int_coord[0] - 1]
            if self.playing_grid[grid_coord[0]][grid_coord[1]] != ' ':
                print("This cell is occupied! Choose another one!")
                continue
            else:
                self.playing_grid[grid_coord[0]][grid_coord[1]] = "X"
            TicTacToe.game_board(new_game)
            if " " not in self.playing_grid:
                break


new_game = TicTacToe()
new_game.moves()



