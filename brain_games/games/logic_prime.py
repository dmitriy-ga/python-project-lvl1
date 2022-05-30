from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
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


def gaming():
    random_num = randint(MIN_NUM, MAX_NUM)
    right_answer = 'yes' if is_prime(random_num) else 'no'
    return random_num, right_answer
