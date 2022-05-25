from random import randint

PRG_SIZE = 10
PRG_START_MIN = 1
PRG_START_MAX = 10
PRG_STEP_MIN = 2
PRG_STEP_MAX = 9
# prg stands for progression


def create_question():
    prg_start = randint(PRG_START_MIN, PRG_START_MAX)
    prg_step = randint(PRG_STEP_MIN, PRG_STEP_MAX)
    prg_finish = prg_start + (prg_step * (PRG_SIZE - 1))
    question = list(range(prg_start, prg_finish, prg_step))
    return question


def remove_list_designation(list_to_str):
    list_to_str = str(list_to_str).replace(',', '')
    list_to_str = list_to_str.replace('[', '')
    list_to_str = list_to_str.replace(']', '')
    list_to_str = list_to_str.replace('\'', '')
    return list_to_str


def main():
    question = create_question()
    rdm_index = randint(0, PRG_SIZE - 2)
    right_answer = question[rdm_index]
    question[rdm_index] = '..'
    question = f'Question: {remove_list_designation(question)}'
    return question, right_answer


if __name__ == '__main__':
    main()
