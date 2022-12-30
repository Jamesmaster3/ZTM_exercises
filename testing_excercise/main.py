from random import randint


def run_guess(answer, guess):
    try:
        if 0 < int(guess) < 11:
            if guess == answer:
                print('You are a genius!')
                return True
            else:
                print('Try again!')
                return False
        else:
            print('Hey bozo, I said 1~10')
            return False
    except TypeError as err:
        print('please enter a number')
        return TypeError
    except ValueError as err:
        print('Please enter a number')
        return ValueError


if __name__ == '__main__':

    answer = randint(1, 10)

    while True:
        try:
            guess = int(input('What number do you guess? '))
            if run_guess(answer, guess):
                break
        except:
            continue
