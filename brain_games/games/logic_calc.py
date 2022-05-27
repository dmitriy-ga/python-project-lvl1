from random import choice, randint

MIN_TERM = 1
MAX_TERM = 100
MIN_FACTOR = 2
MAX_FACTOR1 = 100
MAX_FACTOR2 = 10


def question_calc_addition():
    num1 = randint(MIN_TERM, MAX_TERM)
    num2 = randint(MIN_TERM, MAX_TERM)
    question = f'{num1} + {num2}'
    right_answer = num1 + num2
    return question, right_answer


def question_calc_subtraction():
    num1 = randint(MIN_TERM, MAX_TERM)
    num2 = randint(MIN_TERM, MAX_TERM)
    if num2 > num1:
        num1, num2 = num2, num1
    # Making potential number positive
    question = f'{num1} - {num2}'
    right_answer = num1 - num2
    return question, right_answer


def question_calc_multiply():
    num1 = randint(MIN_FACTOR, MAX_FACTOR1)
    num2 = randint(MIN_FACTOR, MAX_FACTOR2)
    # num2 must be 2-10 to be not so hard
    question = f'{num1} * {num2}'
    right_answer = num1 * num2
    return question, right_answer


def gaming():
    calc_modes = [question_calc_addition,
                  question_calc_subtraction,
                  question_calc_multiply]

    question, right_answer = choice(calc_modes)()
    return question, right_answer
