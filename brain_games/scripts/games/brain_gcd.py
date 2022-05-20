import prompt
from brain_games.scripts.common_games_funcs import checking_answer, greeting
from math import gcd
from random import randint


def questioning():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    print(f'Question: {num1} {num2}')
    answer = prompt.integer('Your answer: ')
    right_answer = gcd(num1, num2)
    return answer, right_answer


def main():
    name = greeting()
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        answer, right_answer = questioning()
        checking_answer(answer, right_answer, name)
    # Exiting 'for' = win
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
