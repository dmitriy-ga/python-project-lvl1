import brain_games.engine
from brain_games.games import logic_even

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    brain_games.engine.gaming(logic_even.gaming, TASK)


if __name__ == '__main__':
    main()
