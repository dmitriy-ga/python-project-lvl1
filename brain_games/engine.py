import prompt

ROUNDS_COUNT = 3


def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def gaming(game):
    name = greeting()
    print(game.TASK)
    for i in range(ROUNDS_COUNT):
        question, right_answer = game.gaming()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ').lower()
        if str(answer) == str(right_answer):
            print('Correct!')
        else:
            # Game over, exit
            print(f"'{answer}' is wrong answer. "
                  f"Correct answer was '{right_answer}'.")
            # This print in two lines printing on one line
            print(f"Let's try again, {name}!")
            break
    else:
        # Exited from 'for' without 'break'
        print(f'Congratulations, {name}!')
