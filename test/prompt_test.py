from unittest import TestCase
from unittest.mock import patch

import magic_squares
from magic_squares.entities.prompt import Prompt


class TestPrompt(TestCase):

    def setUp(self):
        self.prompt = Prompt()

    def test_input_number_is_odd(self):
        odd_number = 3
        with patch.object(magic_squares.entities.prompt, "input", create=True,
                          return_value=odd_number):
            self.prompt.get_number()
            self.assertEqual(self.prompt.number, odd_number)

    def test_input_number_is_even(self):
        even_number = 2
        with patch.object(magic_squares.entities.prompt, "input", create=True, return_value=even_number):
            self._assert_value_error_exception_()

    def _assert_value_error_exception_(self):
        with self.assertRaises(ValueError) as context:
            self.prompt.get_number()
            self.assertTrue('N needs to be an odd integer' in context.exception)
