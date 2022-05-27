from random import choice, randint

MIN_TERM = 1
MAX_TERM = 100
MIN_FACTOR = 2
MAX_FACTOR1 = 100
MAX_FACTOR2 = 10


def gaming():
    operation = choice(['+', '-', '*'])
    if operation == '-':
        num1 = randint(MIN_TERM, MAX_TERM)
        num2 = randint(MIN_TERM, MAX_TERM)
        if num2 > num1:
            num1, num2 = num2, num1
        # Making potential right_answer positive
        question = f'{num1} - {num2}'
        right_answer = num1 - num2
    elif operation == '*':
        num1 = randint(MIN_FACTOR, MAX_FACTOR1)
        num2 = randint(MIN_FACTOR, MAX_FACTOR2)
        # num2 must be 2-10 to be not so hard
        question = f'{num1} * {num2}'
        right_answer = num1 * num2
    else:
        num1 = randint(MIN_TERM, MAX_TERM)
        num2 = randint(MIN_TERM, MAX_TERM)
        question = f'{num1} + {num2}'
        right_answer = num1 + num2
    return question, right_answer
