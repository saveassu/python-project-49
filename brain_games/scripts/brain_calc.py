import random

def question():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    op = random.choice(["+", "-", "*"])

    if op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    else:
        answer = a * b

    return f"{a} {op} {b}", answer
def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")


def game_calc():
    print("What is the result of the expression?")

    correct_answers = 0

    while correct_answers < 3:
        question_text, correct_answer = question()

        print("Question:", question_text)
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print("Let's try again!")
            return

    print("Congratulations!")

main()
game_calc()