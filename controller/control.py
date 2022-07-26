import view.main_screen
import model.game



class Controller:
    def __init__(self):
        self.game = model.game.Game()
        self.board = view.main_screen.Board()
        self.board.set_controller(self)
        self.player = 'X'

    def clear(self):
        self.board.clear()
        self.game.clear()
        self.player = 'X'

    def change_player(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def button_click(self, row: int, col: int):
        if self.game.set_position(row, col, self.player):
            self.board.set_button_status(self.player, row, col)
        else:
            self.board.set_message('Position is occupied. Player {self.player} plays.')
            return None
        if self.game.check_winner(self.player):
            self.board.set_message(f"Player {self.player} won. Play again. Play X plays.")
            self.clear()
            return None

        self.change_player()
        self.board.set_message(f"Player {self.player} plays")


