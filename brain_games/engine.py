import prompt

ROUNDS_COUNT = 3


def greeting():
    print("Welcome to the Brain Games!")
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    return player_name


def run_game(game):
    player_name = greeting()
    print(game.TASK)
    for i in range(ROUNDS_COUNT):
        question, right_answer = game.run_game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ').lower()
        if str(answer) == str(right_answer):
            print('Correct!')
        else:
            # Game over, exit
            print(f"'{answer}' is wrong answer. "
                  f"Correct answer was '{right_answer}'.")
            # This print in two lines printing on one line
            print(f"Let's try again, {player_name}!")
            break
    else:
        # Exited from 'for' without 'break'
        print(f'Congratulations, {player_name}!')
