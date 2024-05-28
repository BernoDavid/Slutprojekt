import json
import random
import time

COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"

def print_with_delay(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_colored(text, color):
    print(f"{color}{text}{COLOR_RESET}")

def run_quiz(questions):
    correct_answers = 0
    wrong_answers = 0
    
    print_with_delay("Welcome to My Geography Quiz!\n", 0.05)
    time.sleep(1)
    
    random.shuffle(questions)
    
    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}: {question['question']}")
        for option in question['options']:
            print(option)

        while True:
            answer = input("Your answer (a, b, c, or d): ").strip().lower()
            if answer in ['a', 'b', 'c', 'd']:
                break
            else:
                print("Invalid input. Please answer using a, b, c, or d.")
        
        if answer == question['answer']:
            print_colored("Correct! 🎉\n", COLOR_GREEN)
            correct_answers += 1
        else:
            print_colored(f"Oops! The correct answer was {question['answer']}. 🙁\n", COLOR_RED)
            wrong_answers += 1
        
        time.sleep(1)
    
    total_questions = len(questions)
    score_percentage = (correct_answers / total_questions) * 100
    
    print_with_delay("\nQuiz Completed!", 0.1)
    print_with_delay(f"Correct Answers: {correct_answers}", 0.1)
    print_with_delay(f"Wrong Answers: {wrong_answers}", 0.1)
    print_with_delay(f"Your score: {score_percentage:.2f}%\n", 0.1)
    
    if correct_answers > wrong_answers:
        print_with_delay("Well done! You know your geography! 🌍", 0.1)
    else:
        print_with_delay("Better luck next time! Keep learning! 📚", 0.1)

def load_questions(filename):
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    questions = load_questions('questions.json')
    run_quiz(questions)
