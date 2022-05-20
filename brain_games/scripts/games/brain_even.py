import prompt
from brain_games.scripts.common_games_funcs import checking_answer, greeting
from random import randint


def questioning():
    question = randint(1, 100)
    print(f'Question: {question}')

    answer = prompt.string('Your answer: ').lower().strip()
    right_answer = 'yes' if question % 2 == 0 else 'no'
    return answer, right_answer


def main():
    name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        answer, right_answer = questioning()
        checking_answer(answer, right_answer, name)
    # Exiting 'for' = win
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
