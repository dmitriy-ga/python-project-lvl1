import prompt
from random import randint

MIN_NUM = 1
MAX_NUM = 100


def is_prime(num):
    if num <= 1:
        return False
    # Negative, 1 and 0 is not a prime numbers!
    i = num - 1
    while i >= 2:
        if num % i == 0:
            return False
        i -= 1
    return True


def main():
    question = randint(MIN_NUM, MAX_NUM)
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ').lower().strip()
    right_answer = 'yes' if is_prime(question) else 'no'
    return answer, right_answer


if __name__ == '__main__':
    main()
