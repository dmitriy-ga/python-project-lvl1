import brain_games.engine

TASK = 'What is the result of the expression?'


def gaming():
    brain_games.engine.gaming('calc', TASK)


if __name__ == '__main__':
    gaming()
