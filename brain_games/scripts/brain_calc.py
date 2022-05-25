import brain_games.engine

TASK = 'What is the result of the expression?'


def main():
    brain_games.engine.main('logic_calc.main', TASK)


if __name__ == '__main__':
    main()
