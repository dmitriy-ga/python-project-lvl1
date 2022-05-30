from math import gcd
from random import randint

TASK = 'Find the greatest common divisor of given numbers.'
MIN_NUM = 1
MAX_NUM = 100


def gaming():
    num1 = randint(MIN_NUM, MAX_NUM)
    num2 = randint(MIN_NUM, MAX_NUM)
    question = f'{num1} {num2}'
    right_answer = gcd(num1, num2)
    return question, right_answer
