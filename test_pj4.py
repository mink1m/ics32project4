import unittest
import p4mechanics


class BoardTest(unittest.TestCase):
    def setUp(self) -> None:
        self._board = p4mechanics.Board(5, 5)
    def test_columns(self) -> None:
        self.assertEqual(self._board.columns(), 5)
    def test_rows(self) -> None:
        self.assertEqual(self._board.rows(), 5)
    def test_list(self) -> None:
        self.assertEqual(self._board.list(), [[' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ']])
    def test_create_faller(self) -> None:
        self._faller = self._board.create_faller("F 3 X Y Z")
        self.assertEqual(self._board.get_top(), "X")
    def test_mid(self) -> None:
        self._faller = self._board.create_faller("F 3 X Y Z")
        self.assertEqual(self._board.get_mid(), "Y")
    def test_bot(self) -> None:
        self._faller = self._board.create_faller("F 3 X Y Z")
        self.assertEqual(self._board.get_bot(), "Z")
    def get_iter(self) -> None:
        self._faller = self._board.create_faller("F 3 X Y Z")
        self.assertEqual(self._board.get_iter(), 0)
    def get_current_col(self) -> None:
        self._faller = self._board.create_faller("F 3 X Y Z")
        self.assertEqual(self._board.get_current_col(), 3)
    


if __name__ == "__main__":
    unittest.main()