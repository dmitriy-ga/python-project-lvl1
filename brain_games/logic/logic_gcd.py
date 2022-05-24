import prompt
from math import gcd
from random import randint

MIN_NUM = 1
MAX_NUM = 100


def main():
    num1 = randint(MIN_NUM, MAX_NUM)
    num2 = randint(MIN_NUM, MAX_NUM)
    print(f'Question: {num1} {num2}')
    answer = prompt.integer('Your answer: ')
    right_answer = gcd(num1, num2)
    return answer, right_answer


if __name__ == '__main__':
    main()
