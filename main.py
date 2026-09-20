from core.storage import load_questions
from core.quiz import Quiz
from random import sample
from pathlib import Path


def main():
    base = Path(__file__).parent
    path = base / "data" / "questions.json"
    data = load_questions(path, enc="utf-8")

    topic = input(f"Выбери тему: {' | '.join(list(data.keys()))}: ")
    questions = sample(data[topic], k=7)

    quiz = Quiz(questions)

    while not quiz.is_finished():
        q = quiz.current_question()
        print(q["question"])
        for i, opt in enumerate(q["options"], start=1):
            print(f"{i}. {opt}")

        user_input = int(input("Твой ответ: "))
        quiz.submit_answer(user_input - 1)

    correct, total = quiz.score()
    print(f"Результат: {correct}/{total}")


if __name__ == "__main__":
    main()