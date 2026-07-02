#Build a quiz program.
#Requirements:
#Create a list of 5 questions.
#Use a for loop to ask each question.
#Count how many questions the user answers.
#At the end print:
#Quiz Finished!
#Questions Attempted : 5
#💡 Bonus: Add another list with answers and check if the user's answer is correct. (This is optional—try it if you're feeling confident.)

questions = [
    "What is the capital of India?",
    "What language are we learning?",
    "2 + 2 = ?",
    "What does AI stand for?",
    "Which company created ChatGPT?"
]

attempted = 0

for question in questions:
    answer = input(question + " ")
    attempted = attempted + 1

print("\nQuiz Finished!")
print("Questions Attempted:", attempted)