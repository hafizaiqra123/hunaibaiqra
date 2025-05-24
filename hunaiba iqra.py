class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question("which is the smallest planet?\n(a) jupiter\n(b) murcury\n(c) venus\n", "b"),
    Question("which element has the au symbol?\n(a) gold\n(b) silver\n(c) copper\n", "a"),
    Question("what is the capital of canada?\n(a) toronto\n(b) paris\n(c) ottawa\n", "c"),
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got", score, "out of", (questions), "correct.")

run_quiz(questions)


