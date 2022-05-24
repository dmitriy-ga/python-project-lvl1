import prompt
from random import randint

MIN_NUM = 1
MAX_NUM = 100


def main():
    question = randint(MIN_NUM, MAX_NUM)
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ').lower().strip()
    right_answer = 'yes' if question % 2 == 0 else 'no'
    return answer, right_answer


if __name__ == '__main__':
    main()
