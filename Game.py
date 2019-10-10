import unittest


class TicTacToe:
    def __init__(self, N):
        self.dim = N
        self.field = [['_' for j in range(N)] for i in range(N)]
        self.game_over = False
        self.player_number = 0
        self.count_of_moves = 0

    # Выводит поле в консоль
    def print_field(self):
        for row in self.field:
            for i in row:
                print(i, end='')
            print()

    def begin_game(self):
        while not self.game_over:
            print('Ход игрока {}'.format(self.player_number))
            self.get_data()

    # Проверка корректности введенных данных
    def check_correct(self, row, column):
        if 0 <= row < self.dim and 0 <= column < self.dim:
            if self.field[row][column] == '_':
                return True

        return False

    # Считывание данных
    def get_data(self):
        # Пока не ввели верные координаты
        while True:
            print("Текущее состояние поля:")
            self.print_field()
            print("Введите координаты:")
            row, column = map(int, input().split())

            if self.check_correct(row, column):
                self.make_move(row, column)
                break
            else:
                print("Введены неверные координаты. Попробуйте снова.")

    # Функция, делающая ход
    def make_move(self, row, column):
        if self.player_number == 0:
            self.field[row][column] = 'x'
        else:
            self.field[row][column] = 'o'

        self.count_of_moves += 1
        self.is_win()
        self.player_number = (self.player_number + 1) % 2

    # Функция, проверяющая закончилась игра или нет
    def is_win(self):
        if self.player_number == 0:
            symbol = 'x'
            self.check_field(symbol)
        else:
            symbol = 'o'
            self.check_field(symbol)

        if self.game_over:
            print('Победил игрок {}'.format(self.player_number))
        elif self.count_of_moves == self.dim * self.dim:
            self.game_over = True
            print('Ничья')

    # Проверка состояния поля
    def check_field(self, symbol):
        # Пробегаемся по строкам и столбцам
        for i in range(self.dim):
            count_ch_in_row = 0
            count_ch_in_col = 0
            for j in range(self.dim):
                if self.field[i][j] == symbol:
                    count_ch_in_row += 1
                if self.field[j][i] == symbol:
                    count_ch_in_col += 1

            if count_ch_in_row == self.dim or count_ch_in_col == self.dim:
                self.game_over = True
                break

        # Пробегаемся по диагоналям
        count_ch_in_right = 0
        count_ch_in_left = 0
        for i in range(self.dim):
            if self.field[i][i] == symbol:
                count_ch_in_right += 1
            if self.field[self.dim - 1 - i][self.dim - 1 - i] == symbol:
                count_ch_in_left += 1

        if count_ch_in_right == self.dim or count_ch_in_left == self.dim:
            self.game_over = True


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


NEW_GAME = TicTacToe(3)
NEW_GAME.begin_game()
# unittest.main()
