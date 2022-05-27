import brain_games.engine
from brain_games.games import logic_progression

TASK = 'What number is missing in the progression?'


def main():
    brain_games.engine.gaming(logic_progression.gaming, TASK)


if __name__ == '__main__':
    main()
