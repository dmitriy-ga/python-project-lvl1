import brain_games.engine

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def gaming():
    brain_games.engine.gaming('prime', TASK)


if __name__ == '__main__':
    gaming()
