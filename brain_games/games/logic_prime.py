from random import randint

MIN_NUM = 1
MAX_NUM = 100


def is_prime(num):
    if num <= 1:
        return False
    # Negative, 1 and 0 is not a prime numbers!
    i = num - 1
    while i >= 2:
        if num % i == 0:
            return False
        i -= 1
    return True


def main():
    random_num = randint(MIN_NUM, MAX_NUM)
    question = f'Question: {random_num}'
    right_answer = 'yes' if is_prime(random_num) else 'no'
    return question, right_answer


if __name__ == '__main__':
    main()
