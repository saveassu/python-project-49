from random import randint


def get_user_name():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def game(name):
    print("What number is missing in the progression?")

    correct_count = 0
    required_wins = 3

    while correct_count < required_wins:
        start = randint(1, 10)
        step = randint(1, 5)
        length = randint(5, 10)

        progression = []
        for i in range(length):
            number = start + i * step
            progression.append(number)

        hidden_index = randint(0, length - 1)
        correct_answer = progression[hidden_index]

        progression[hidden_index] = ".."

        question_text = ""
        for num in progression:
            question_text += str(num) + " "
        question_text = question_text.strip()

        print(f"Question: {question_text}")
        user_answer = input("Your answer: ").strip()

        if user_answer == str(correct_answer):
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