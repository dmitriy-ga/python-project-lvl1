import brain_games.engine

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def gaming():
    brain_games.engine.gaming('even', TASK)


if __name__ == '__main__':
    gaming()
