from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    if number <= 1:
        return False
    # Negative, 1 and 0 is not a prime numbers!
    i = number - 1
    while i >= 2:
        if number % i == 0:
            return False
        i -= 1
    return True


def run_game():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    right_answer = 'yes' if is_prime(random_number) else 'no'
    return random_number, right_answer
