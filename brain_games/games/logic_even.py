from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def run_game():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    right_answer = 'yes' if random_number % 2 == 0 else 'no'
    return random_number, right_answer
