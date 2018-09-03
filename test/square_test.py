from unittest import TestCase
import numpy

from magic_squares.entities.square import Square


class TestSquare(TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSquare, self).__init__(*args, **kwargs)
        self.INITIAL_MATRIX = numpy.matrix('0 1 0; 0 0 0; 0 0 0')
        self.MATRIX_AFTER_GONE_OFF_ON_TOP_OF_THE_GRID_FIRST = numpy.matrix('0 1 0; 0 0 0; 0 0 2')
        self.MATRIX_AFTER_GONE_OFF_ON_THE_LEFT_OF_THE_GRID_FIRST = numpy.matrix('0 1 0; 3 0 0; 0 0 2')
        self.MATRIX_AFTER_BUMP_ON_EXISTING_NUMBER = numpy.matrix('0 1 0; 3 0 0; 4 0 2')
        self.MATRIX_AFTER_MOVE_DIAGONALLY_FIRST = numpy.matrix('0 1 0; 3 5 0; 4 0 2')
        self.MATRIX_AFTER_MOVE_DIAGONALLY_SECOND = numpy.matrix('0 1 6; 3 5 0; 4 0 2')
        self.MATRIX_AFTER_GONE_OFF_THE_EDGE_OF_THE_GRID = numpy.matrix('0 1 6; 3 5 7; 4 0 2')
        self.MATRIX_AFTER_GONE_OFF_ON_THE_LEFT_OF_THE_GRID_SECOND = numpy.matrix('8 1 6; 3 5 7; 4 0 2')
        self.MATRIX_AFTER_GONE_OFF_ON_TOP_OF_THE_GRID_SECOND = numpy.matrix('8 1 6; 3 5 7; 4 9 2')
        self.MAGIC_SQUARE_MATRIX = numpy.matrix('8 1 6; 3 5 7; 4 9 2')
        self.INITIAL_MATRIX_AS_STRING = '0\t1\t0\n0\t0\t0\n0\t0\t0'

    def setUp(self):
        self.square = Square(3)

    def test_init_square_with_number_equal_to_3(self):
        self._assert_square_(self.INITIAL_MATRIX)

    def test_init_square_with_number_equal_to_5(self):
        square = Square(5)
        initial_square = numpy.matrix('0 0 1 0 0; 0 0 0 0 0; 0 0 0 0 0; 0 0 0 0 0; 0 0 0 0 0')
        numpy.testing.assert_array_equal(square.matrix, initial_square, verbose=True)

    def test_step_and_gone_off_on_top_of_the_grid_first(self):
        self.square.step_once()
        self._assert_square_(self.MATRIX_AFTER_GONE_OFF_ON_TOP_OF_THE_GRID_FIRST)

    def test_step_and_gone_off_on_the_left_of_the_grid_first(self):
        self._move_square_(times=2)
        self._assert_square_(self.MATRIX_AFTER_GONE_OFF_ON_THE_LEFT_OF_THE_GRID_FIRST)

    def test_step_and_bump_on_existing_number(self):
        self._move_square_(times=3)
        self._assert_square_(self.MATRIX_AFTER_BUMP_ON_EXISTING_NUMBER)

    def test_step_diagonally_first(self):
        self._move_square_(times=4)
        self._assert_square_(self.MATRIX_AFTER_MOVE_DIAGONALLY_FIRST)

    def test_step_diagonally_second(self):
        self._move_square_(times=5)
        self._assert_square_(self.MATRIX_AFTER_MOVE_DIAGONALLY_SECOND)

    def test_step_and_gone_off_the_edge_of_the_grid(self):
        self._move_square_(times=6)
        self._assert_square_(self.MATRIX_AFTER_GONE_OFF_THE_EDGE_OF_THE_GRID)

    def test_step_and_gone_off_on_the_left_of_the_grid_second(self):
        self._move_square_(times=7)
        self._assert_square_(self.MATRIX_AFTER_GONE_OFF_ON_THE_LEFT_OF_THE_GRID_SECOND)

    def test_step_and_gone_off_on_top_of_the_grid_second(self):
        self._move_square_(times=8)
        self._assert_square_(self.MATRIX_AFTER_GONE_OFF_ON_TOP_OF_THE_GRID_SECOND)

    def test_create_magic_square(self):
        self.square.step_to_finish()
        self._assert_square_(self.MAGIC_SQUARE_MATRIX)

    def test_check_that_square_is_not_magic(self):
        self.assertFalse(self.square.is_magic_square())

    def test_check_that_square_is_magic(self):
        self.square.step_to_finish()
        self.assertTrue(self.square.is_magic_square())

    def test_square_to_string(self):
        self.assertEqual(self.square.to_string(), self.INITIAL_MATRIX_AS_STRING)

    def _move_square_(self, times):
        [self.square.step_once() for _ in range(0, times)]

    def _assert_square_(self, the_other_matrix):
        numpy.testing.assert_array_equal(self.square.matrix, the_other_matrix, verbose=True)
