from math import gcd
from random import randint

TASK = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def run_game():
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{number1} {number2}'
    right_answer = gcd(number1, number2)
    return question, right_answer
