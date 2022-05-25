import prompt
from random import choice, randint

MIN_TERM = 1
MAX_TERM = 100
MIN_FACTOR = 2
MAX_FACTOR1 = 100
MAX_FACTOR2 = 10


def question_calc_addition():
    num1 = randint(MIN_TERM, MAX_TERM)
    num2 = randint(MIN_TERM, MAX_TERM)
    print(f'Question: {num1} + {num2}')
    answer = prompt.integer('Your answer: ')
    right_answer = num1 + num2
    return answer, right_answer


def question_calc_subtraction():
    num1 = randint(MIN_TERM, MAX_TERM)
    num2 = randint(MIN_TERM, MAX_TERM)
    if num2 > num1:
        num1, num2 = num2, num1
    print(f'Question: {num1} - {num2}')
    answer = prompt.integer('Your answer: ')
    right_answer = num1 - num2
    return answer, right_answer


def question_calc_multiply():
    num1 = randint(MIN_FACTOR, MAX_FACTOR1)
    num2 = randint(MIN_FACTOR, MAX_FACTOR2)
    print(f'Question: {num1} * {num2}')
    answer = prompt.integer('Your answer: ')
    right_answer = num1 * num2
    return answer, right_answer


def main():
    calc_modes = [question_calc_addition,
                  question_calc_subtraction,
                  question_calc_multiply]

    answer, right_answer = choice(calc_modes)()
    return answer, right_answer


if __name__ == '__main__':
    main()
