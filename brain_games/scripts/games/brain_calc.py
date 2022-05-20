from brain_games.scripts.common_games_funcs import (
    checking_answer,
    greeting
)
import prompt
from random import choice, randint


def question_calc_addition():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    print(f'Question: {num1} + {num2}')
    answer = prompt.integer('Your answer: ')
    right_answer = num1 + num2
    return answer, right_answer


def question_calc_subtraction():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    if num2 > num1:
        num1, num2 = num2, num1
        #
    print(f'Question: {num1} - {num2}')
    answer = prompt.integer('Your answer: ')
    right_answer = num1 - num2
    return answer, right_answer


def question_calc_multiply():
    num1 = randint(1, 100)
    num2 = randint(2, 10)
    print(f'Question: {num1} * {num2}')
    answer = prompt.integer('Your answer: ')
    right_answer = num1 * num2
    return answer, right_answer


def main():
    name = greeting()
    print('What is the result of the expression?')
    calc_modes = [question_calc_addition,
                  question_calc_subtraction,
                  question_calc_multiply]
    for i in range(3):
        answer, right_answer = choice(calc_modes)()
        checking_answer(answer, right_answer, name)
    # Exiting 'for' = win
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
