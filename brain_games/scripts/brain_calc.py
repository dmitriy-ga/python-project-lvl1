import brain_games.engine
from brain_games.games import logic_calc

TASK = 'What is the result of the expression?'


def main():
    brain_games.engine.gaming(logic_calc.gaming, TASK)


if __name__ == '__main__':
    main()
