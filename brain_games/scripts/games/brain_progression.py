import prompt
from brain_games.scripts.common_games_funcs import checking_answer, greeting
from random import randint


def create_question():
    prg_size = 10
    prg_start = randint(1, 10)
    prg_step = randint(2, 9)
    prg_finish = prg_start + (prg_step * (prg_size - 1))
    # prg stands for progression
    question = list(range(prg_start, prg_finish, prg_step))
    return question, prg_size


def questioning(question, prg_size):
    rdm_index = randint(0, prg_size - 2)
    right_answer = question[rdm_index]
    question[rdm_index] = '..'
    print('Question: ' + str(question).replace(',', '').replace('[', '').replace(']', ''))
    answer = prompt.integer('Your answer: ')
    return answer, right_answer


def main():
    name = greeting()
    print('What number is missing in the progression?')
    for i in range(3):
        question, prg_size = create_question()
        answer, right_answer = questioning(question, prg_size)
        checking_answer(answer, right_answer, name)
    # Exiting 'for' = win
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
