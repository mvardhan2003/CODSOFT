import random

# Quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "choices": ["A) London", "B) Paris", "C) Rome", "D) Berlin"],
        "correct_answer": "B",
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["A) Earth", "B) Jupiter", "C) Mars", "D) Venus"],
        "correct_answer": "B",
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["A) Michelangelo", "B) Leonardo da Vinci", "C) Pablo Picasso", "D) Vincent van Gogh"],
        "correct_answer": "B",
    },
]

def display_welcome_message():
    print("Welcome to the General Knowledge Quiz!")
    print("You will be presented with multiple-choice questions.")
    print("Select the correct option by typing the letter (A, B, C, D) and press Enter.")
    print("Let's begin!\n")

def get_user_choice():
    return input("Enter your answer choice: ").upper()

def present_quiz_question(question_data):
    print(question_data["question"])
    for choice in question_data["choices"]:
        print(choice)
    user_answer = get_user_choice()
    return user_answer

def evaluate_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    return False

def display_feedback(is_correct, correct_answer):
    if is_correct:
        print("Correct!\n")
    else:
        print("Incorrect.")
        print("The correct answer is:", correct_answer, "\n")

def calculate_final_score(total_questions, correct_answers):
    return int((correct_answers / total_questions) * 100)

def display_final_results(score):
    print("Your Final Score:", score, "%")
    if score >= 70:
        print("Great job! You did well.")
    else:
        print("Keep practicing to improve your knowledge.")

def play_again():
    return input("Do you want to play again? (yes/no): ").lower().startswith("y")

def main():
    display_welcome_message()
    total_questions = len(quiz_data)
    correct_answers = 0

    while True:
        random.shuffle(quiz_data)
        for question_data in quiz_data:
            user_answer = present_quiz_question(question_data)
            is_correct = evaluate_answer(user_answer, question_data["correct_answer"])
            display_feedback(is_correct, question_data["correct_answer"])
            if is_correct:
                correct_answers += 1

        final_score = calculate_final_score(total_questions, correct_answers)
        display_final_results(final_score)

        if not play_again():
            break
        else:
            correct_answers = 0
            print("\nLet's play again!\n")

if __name__ == "__main__":
    main()
