from magic_squares.entities.prompt import Prompt
from magic_squares.entities.square import Square


def main():
    prompt = Prompt()
    valid_input = False

    while not valid_input:
        try:
            prompt.get_input()
            valid_input = True
        except ValueError:
            print('Not an odd number. Please try again.')

    square = Square(prompt.number)
    square.step_to_finish()

    print('The result matrix for N=%d is:\n' % prompt.number)
    print(square.to_string())

    if square.is_magic_square():
        print('\nThe result matrix is a magic square.')
    else:
        print('\nThe result matrix is not a magic square.')

if __name__ == "__main__":
    main()
