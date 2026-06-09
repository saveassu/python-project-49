from random import randint
import math


def generate_question():
    num1 = randint(1, 100)
    num2 = randint(1, 100)


    correct_answer = math.gcd(num1, num2)


    question = f"{num1} {num2}"

    return question, correct_answer


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    correct_count = 0

    while correct_count < 3:

        question, correct_answer = generate_question()

        print(f"Question: {num1} {num2}")
        user_answer = input("Your answer: ")
        if int(user_answer) == correct_answer:
            print("Correct!")
            correct_count += 1
        else:
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()