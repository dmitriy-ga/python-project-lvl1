from random import choice, randint

MIN_NUMBER = 1
MAX_NUMBER = 100


def gaming():
    operation = choice(['+', '-', '*'])
    if operation == '-':
        number1 = randint(MIN_NUMBER, MAX_NUMBER)
        number2 = randint(MIN_NUMBER, MAX_NUMBER)
        question = f'{number1} - {number2}'
        right_answer = number1 - number2
    elif operation == '*':
        number1 = randint(MIN_NUMBER, MAX_NUMBER)
        number2 = randint(MIN_NUMBER, MAX_NUMBER)
        question = f'{number1} * {number2}'
        right_answer = number1 * number2
    else:
        number1 = randint(MIN_NUMBER, MAX_NUMBER)
        number2 = randint(MIN_NUMBER, MAX_NUMBER)
        question = f'{number1} + {number2}'
        right_answer = number1 + number2
    return question, right_answer
