class Prompt:
    def __init__(self):
        self.number = None

    def get_input(self):
        number = int(input("Enter a valid odd integer: "))
        self._set_number_(number)

    def _set_number_(self, number):
        if self._is_valid_input(number):
            self.number = number
        else:
            raise ValueError('N needs to be an odd integer')

    def _is_valid_input(self, number):
        return self._is_integer_(number) and self._is_odd_(number)

    def _is_odd_(self, number):
        return number % 2 != 0

    def _is_integer_(self, number):
        return int(number) == number
