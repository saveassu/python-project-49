from random import randint


def get_user_name():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_count = 0
    required_wins = 3

    while correct_count < required_wins:
        number = randint(0, 100)
        print(f"Question: {number}")

        user_answer = input(
            "Your answer: ").strip().lower()

        is_even = number % 2 == 0
        correct_answer = "yes" if is_even else "no"

        if user_answer == correct_answer:
            print("Correct!")
            correct_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    name = get_user_name()
    game(name)


if __name__ == "__main__":
    main()