from unittest import TestCase
from tictactoe import tictactoe


class PlayerInputMockTest(TestCase):
    tictactoe = tictactoe

    def __init__(self, input_v):
        self.input_v = input_v
        self.input_index += 1

    def get_input(self):
        value = self.input_v[self.input_index]
        self.input_index += 1
        return value


class PBMockTest(TestCase):
    tictactoe = tictactoe

    def __init__(self):
        self.print = None

    def print(self, board):
        self.print = board


class CheckIfTieStubTest(TestCase):
    tictactoe = tictactoe

    def __init__(self, tie):
        self.tie = tie

    def is_tie(self, board):
        return self.tie

    def isnt_tie(self, board):
        self.tie = False
        return self.tie
