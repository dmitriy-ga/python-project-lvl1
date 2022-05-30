from random import randint

PRG_SIZE = 10
PRG_START_MIN = 1
PRG_START_MAX = 10
PRG_STEP_MIN = 2
PRG_STEP_MAX = 9
# prg stands for progression


def create_random_progression():
    prg_start = randint(PRG_START_MIN, PRG_START_MAX)
    prg_step = randint(PRG_STEP_MIN, PRG_STEP_MAX)
    prg_finish = prg_start + (prg_step * (PRG_SIZE - 1))
    question = list(range(prg_start, prg_finish, prg_step))
    return question


def gaming():
    question = create_random_progression()
    rdm_index = randint(0, PRG_SIZE - 2)

    right_answer = question[rdm_index]
    question[rdm_index] = '..'

    symbols_to_remove = str.maketrans('', '', "[],'")
    question = str(question).translate(symbols_to_remove)
    return question, right_answer
