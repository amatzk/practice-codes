class Player:
    def __init__(self, symbol):
        self.symbol = symbol


class Cell:
    def __init__(self):
        self.symbol = None

    def set_symbol(self, symbol):
        if not self.symbol:
            self.symbol = symbol
            return True
        return False


class Board:
    def __init__(self):
        self.cells = [[Cell() for _ in range(3)] for _ in range(3)]

    def draw(self):
        for row in self.cells:
            print(" ".join(cell.symbol if cell.symbol else "-" for cell in row))

    def set_symbol(self, row, col, symbol):
        if 0 <= row < 3 and 0 <= col < 3:
            return self.cells[row][col].set_symbol(symbol)
        return False

    def check_win(self, symbol):
        for row in self.cells:
            if all(cell.symbol == symbol for cell in row):
                return True
        for col in range(3):
            if all(self.cells[row][col].symbol == symbol for row in range(3)):
                return True
        if all(self.cells[i][i].symbol == symbol for i in range(3)):
            return True
        if all(self.cells[i][2 - i].symbol == symbol for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(cell.symbol for row in self.cells for cell in row)


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("X"), Player("O")]
        self.turn = 0


class GameController:
    def __init__(self, game):
        self.game = game

    def get_player_input(self, player):
        while True:
            try:
                row = int(input(f"Player {player.symbol}, enter row: "))
                col = int(input(f"Player {player.symbol}, enter col: "))
                if 0 <= row < 3 and 0 <= col < 3:
                    return row, col
                else:
                    print(f"Invalid move: {row}, {col}, try again.")
            except ValueError:
                print(f"Invalid input: {row}, {col}, please enter a number.")
            except Exception as e:
                print(f"An error occurred: {e}")

    def make_move(self, player, row, col):
        if self.game.board.set_symbol(row, col, player.symbol):
            if self.game.board.check_win(player.symbol):
                print(f"Player {player.symbol} wins!")
                return True
            elif self.game.board.is_full():
                print("The game is a draw!")
                return True
            self.game.turn += 1
        else:
            print(f"Invalid move: {row}, {col}, try again.")
        return False

    def play(self):
        while True:
            self.game.board.draw()
            player = self.game.players[self.game.turn % 2]
            row, col = self.get_player_input(player)
            if self.make_move(player, row, col):
                break
        self.game.board.draw()


game = Game()
game_controller = GameController(game)
game_controller.play()
