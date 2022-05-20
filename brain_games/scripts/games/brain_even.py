import prompt
from random import randint


def questioning():
    question = randint(1, 100)
    print(f'Question: {question}')

    answer = prompt.string('Your answer: ').lower().strip()
    right_answer = 'yes' if question % 2 == 0 else 'no'
    return answer, right_answer


def checking_answer(answer, right_answer, name):
    if answer == right_answer:
        print('Correct!')
    else:
        # Game over, exit
        print(f"'{answer}' is wrong answer. "
              f"Correct answer was '{right_answer}'.")
        # This print in two lines printing on one line
        print(f"Let's try again, {name}!")
        exit()


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        answer, right_answer = questioning()
        checking_answer(answer, right_answer, name)
    # Exiting 'for' = win
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
