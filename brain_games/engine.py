import prompt

ROUNDS_COUNT = 3


def checking_answer(answer, right_answer):
    if str(answer) == str(right_answer):
        print('Correct!')
        winning = True
    else:
        winning = False
    return winning


def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def gaming(game, task):
    name = greeting()
    print(task)
    winning = None
    for i in range(ROUNDS_COUNT):
        question, right_answer = game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ').lower()
        winning = checking_answer(answer, right_answer)
        if not winning:
            # Game over, exit
            print(f"'{answer}' is wrong answer. "
                  f"Correct answer was '{right_answer}'.")
            # This print in two lines printing on one line
            print(f"Let's try again, {name}!")
            break
    if winning:
        print(f'Congratulations, {name}!')
