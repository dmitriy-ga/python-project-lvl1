import prompt
from brain_games.scripts.common_games_funcs import checking_answer, greeting
from random import randint


def isprime(num):
    if num <= 1:
        return False
    # Negative, 1 and 0 is not a prime numbers!
    i = num - 1
    while i >= 2:
        if num % i == 0:
            return False
        i -= 1
    return True


def questioning():
    question = randint(1, 100)
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ').lower().strip()
    right_answer = 'yes' if isprime(question) else 'no'
    return answer, right_answer


def main():
    name = greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        answer, right_answer = questioning()
        checking_answer(answer, right_answer, name)
    # Exiting 'for' = win
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
