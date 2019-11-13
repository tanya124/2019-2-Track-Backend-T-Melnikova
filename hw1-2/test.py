import unittest
from TicTacToe import TicTacToe

class TestGame(unittest.TestCase):
    def test_check_correct(self):
        game = TicTacToe(3)
        game.make_move(0, 0)
        self.assertEqual(game.check_correct(0, 1), True)
        self.assertEqual(game.check_correct(2, 2), True)
        self.assertEqual(game.check_correct(1, 0), True)

        self.assertEqual(game.check_correct(0, 0), False)
        self.assertEqual(game.check_correct(-1, 0), False)
        self.assertEqual(game.check_correct(2, 100500), False)

if __name__ == '__main__':
    unittest.main()
