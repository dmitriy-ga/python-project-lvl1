import brain_games.engine
from brain_games.games import logic_gcd

TASK = 'Find the greatest common divisor of given numbers.'


def main():
    brain_games.engine.gaming(logic_gcd.gaming, TASK)


if __name__ == '__main__':
    main()
