from brain_games.games import *  # noqa: F401, F403
from brain_games.common_games_funcs import greeting, checking_answer

ROUNDS = 3


def main(game, task):
    name = greeting()
    print(task)
    game_to_start = eval(game)
    for i in range(ROUNDS):
        answer, right_answer = game_to_start()
        checking_answer(answer, right_answer, name)
    # Exiting 'for' = win
    print(f'Congratulations, {name}!')
