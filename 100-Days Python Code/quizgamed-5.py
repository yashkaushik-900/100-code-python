# 🧠 Simple Quiz Game in Python

# A list of questions with options and the correct answer
quiz_questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which programming language is known as the 'language of AI'?",
        "options": ["A. Python", "B. C++", "C. Java", "D. Ruby"],
        "answer": "A"
    },
    {
        "question": "What does HTML stand for?",
        "options": [
            "A. Hyper Trainer Marking Language",
            "B. Hyper Text Markup Language",
            "C. Hyper Text Marketing Language",
            "D. Hyper Tool Multi Language"
        ],
        "answer": "B"
    }
]

# Keep track of score
score = 0

print("🎮 Welcome to the Quiz Game! 🎮\n")
print("Instructions: Choose the correct option (A/B/C/D)\n")

# Loop through each question
for index, q in enumerate(quiz_questions, start=1):
    print(f"Q{index}: {q['question']}")
    for option in q["options"]:
        print(option)
    
    # Take user input
    answer = input("Your answer (A/B/C/D): ").strip().upper()

    # Check correctness
    if answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {q['answer']}\n")

# Show final score
print("🎯 Quiz Finished!")
print(f"Your Final Score: {score}/{len(quiz_questions)}")
