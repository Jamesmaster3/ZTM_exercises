import sys
from random import randint

input1 = int(sys.argv[1])
input2 = int(sys.argv[2])
result = randint(input1, input2)
print(result)

while True:

    try:
        answer = int(input('What number do you guess? '))
        answer <= input2
        if answer == result:
            print('You are a genius!')
            break
        elif answer < input1 or answer > input2:
            print(f'Guess a number between {input1} and {input2}')

        else:
            print('Try again!')
            continue
    except ValueError:
        print('Please input a number.')
        continue
    except:
        print('error')
