import random

# List of questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. J.K. Rowling", "D. Mark Twain"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. CO2", "B. O2", "C. H2O", "D. NaCl"],
        "answer": "C"
    },
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who is the current President of the United States?",
        "options": ["A. Joe Biden", "B. Barack Obama", "C. Donald Trump", "D. George Bush"],
        "answer": "A"
    }
]

# Function to run the quiz
def run_quiz(quiz_data):
    # Shuffle the questions
    random.shuffle(quiz_data)
    
    # Initialize score
    score = 0
    
    # Ask each question
    for question_data in quiz_data:
        print(question_data["question"])
        for option in question_data["options"]:
            print(option)
        
        # Get the user's answer
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        
        # Provide feedback
        if answer == question_data["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {question_data['answer']}.\n")
    
    # Show final score
    print(f"Quiz over! You scored {score}/{len(quiz_data)}.")

# Run the quiz
run_quiz(quiz_data)
