import brain_games.engine
from brain_games.games import logic_prime

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    brain_games.engine.gaming(logic_prime.gaming, TASK)


if __name__ == '__main__':
    main()
