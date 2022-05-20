def checking_answer(answer, right_answer, name):
    if answer == right_answer:
        print('Correct!')
    else:
        # Game over, exit
        print(f"'{answer}' is wrong answer. "
              f"Correct answer was '{right_answer}'.")
        # This print in two lines printing on one line
        print(f"Let's try again, {name}!")
        exit()
