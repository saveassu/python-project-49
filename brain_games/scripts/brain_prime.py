from random import randint


def get_user_name():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def game(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_count = 0
    required_wins = 3

    while correct_count < required_wins:
        number = randint(1, 100)
        print(f"Question: {number}")

        user_answer = input("Your answer: ").strip().lower()
        correct_answer = "yes" if is_prime(number) else "no"

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