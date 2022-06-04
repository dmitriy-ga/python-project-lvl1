from random import randint

TASK = 'What number is missing in the progression?'
PROG_SIZE = 10
PROG_START_MIN = 1
PROG_START_MAX = 10
PROG_STEP_MIN = 2
PROG_STEP_MAX = 9
# prog stands for progression


def create_random_progression():
    prog_start = randint(PROG_START_MIN, PROG_START_MAX)
    prog_step = randint(PROG_STEP_MIN, PROG_STEP_MAX)
    prog_finish = prog_start + (prog_step * (PROG_SIZE - 1))
    question = list(range(prog_start, prog_finish, prog_step))
    return question


def run_game():
    question = create_random_progression()
    random_index = randint(0, PROG_SIZE - 2)

    right_answer = question[random_index]
    question[random_index] = '..'

    symbols_to_remove = str.maketrans('', '', "[],'")
    question = str(question).translate(symbols_to_remove)
    return question, right_answer
