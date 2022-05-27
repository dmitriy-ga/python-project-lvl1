from random import randint

MIN_NUM = 1
MAX_NUM = 100


def main():
    random_num = randint(MIN_NUM, MAX_NUM)
    right_answer = 'yes' if random_num % 2 == 0 else 'no'
    return random_num, right_answer


if __name__ == '__main__':
    main()
