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


def checking_answer(answer, right_answer):
    if str(answer) == str(right_answer):
        print('Correct!')
        winning = True
    else:
        winning = False
    return winning


def asking(started_game):
    if started_game == ['even', 'gcd', 'prime']:
        answer = prompt.integer('Your answer: ')
    else:
        answer = prompt.string('Your answer: ').lower().strip()
    return answer


def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def main(game, task):
    name = greeting()
    print(task)
    game_to_start = games_list[game]
    winning = None
    for i in range(ROUNDS):
        question, right_answer = game_to_start()
        print(question)
        answer = asking(game)
        winning = checking_answer(answer, right_answer)
        if not winning:
            # Game over, exit
            print(f"'{answer}' is wrong answer. "
                  f"Correct answer was '{right_answer}'.")
            # This print in two lines printing on one line
            print(f"Let's try again, {name}!")
            break
    if winning:
        print(f'Congratulations, {name}!')
