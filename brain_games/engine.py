from brain_games.games import (logic_even,
                               logic_calc,
                               logic_gcd,
                               logic_prime,
                               logic_progression)
import prompt

ROUNDS = 3
games_list = {'even': logic_even.main,
              'calc': logic_calc.main,
              'gcd': logic_gcd.main,
              'prime': logic_prime.main,
              'progression': logic_progression.main}


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


def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def main(game, task):
    name = greeting()
    print(task)
    game_to_start = games_list[game]
    for i in range(ROUNDS):
        answer, right_answer = game_to_start()
        checking_answer(answer, right_answer, name)
    # Exiting 'for' = win
    print(f'Congratulations, {name}!')
