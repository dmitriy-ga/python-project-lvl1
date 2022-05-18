import prompt
from random import randint


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        question = randint(1, 100)
        print(f'Question: {question}')

        answer = prompt.string('Your answer: ').lower().strip()
        right_answer = 'yes' if question % 2 == 0 else 'no'

        if answer == right_answer:
            print('Correct!')
            continue
        else:
            print(f"'{answer}' is wrong answer. "
                  f"Correct answer was '{right_answer}'.")
            # This print in two lines printing on one line
            print(f"Let's try again, {name}!")
            exit()

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
