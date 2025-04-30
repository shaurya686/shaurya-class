class QnAGame:
    def __init__(self):
        self.questions = [
            ("What is the capital of France?", "Paris"),
            ("What is 2 + 2?", "4"),
            ("What color are bananas?", "Yellow")
        ]
        self.score = 0

    def ask_questions(self):
        for question, answer in self.questions:
            user_answer = input(question + " ")
            if user_answer.strip().lower() == answer.lower():
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {answer}.\n")

    def show_score(self):
        print(f"Game over! You got {self.score} out of {len(self.questions)} right.")

# Create a game object and run it
game = QnAGame()
game.ask_questions()
game.show_score()
