from parameters import *


class Game:
    def __init__(self):
        self.mode = 'placing'
        self.positions = {}
        self.controller = None

    def clear(self):
        self.positions = {}
    def check_winner(self, player):

        count = 0
        for r in range(rows):
            for c in range(columns):
                if self.positions.get((r, c)) == player:
                    count = count + 1
            if count == columns:
                return True
            count = 0

        count = 0

        for c in range(columns):
            for r in range(rows):
                if self.positions.get((r, c)) == player:
                    count = count + 1
                if count == rows:
                    return True
            count = 0

        count = 0

        for i in range(min(rows, columns)):
            if self.positions.get((i, i)) == player:
                count = count + 1
        if count == min(rows, columns):
            return True

        count = 0

        for i in range(min(rows, columns)):
            if self.positions.get((rows - i - 1, i)) == player:
                count = count + 1
        if count == min(rows, columns):
            return True

        count = 0
        return False

    def get_position_status(self, row: int, col: int) -> str:
        return self.positions.get((row, col))

    def set_controller(self, controller):
        self.controller = controller

    def check_position(self, row: int, col: int) -> bool:
        print(self.get_position_status(row, col))
        if self.get_position_status(row, col) is None:
            return True
        else:
            return False

    def set_position(self, row: int, col: int, player: str) -> bool:
        if self.check_position(row, col):
            self.positions[(row, col)] = player
            return True
        else:
            return False
