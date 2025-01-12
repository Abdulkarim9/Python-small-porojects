import random


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        for question in self.questions:
            print(question.prompt)

            for i, option in enumerate(question.options):
                print(f"{i+1}-{option}")

            user_input = input(f"Enter The correct option: ")

            if user_input == question.answer:
                print("Correct")
                self.score += 1
                
            else:
                print("Incorrect:)")

        print(f"You got {self.score} correct out of {len(self.questions)}")
                    


class MUltipleChoices:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer



questions = [MUltipleChoices("What is the capital of France?", ["Paris", "London", "New York"], "Paris"),
MUltipleChoices("What is the largest ocean in the world?", ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean"], "Pacific Ocean"),
MUltipleChoices("Who invented the light bulb?", ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla"], "Thomas Edison")
]

random.shuffle(questions)

quiz = Quiz(questions)
quiz.start()
