import random

questions = [
    {"q": "Which of the following is a mutable data type in Python?\n(a) Tuple\n(b) String\n(c) List\n(d) Frozenset\n", "ans": "c"},
    {"q": "Which keyword is used to define a function in Python?\n(a) def\n(b) func\n(c) function\n(d) define\n", "ans": "a"},
    {"q": "Which module in Python is used for random number generation?\n(a) random\n(b) math\n(c) numbers\n(d) os\n", "ans": "a"},
    {"q": "Which of these is not a valid Python loop?\n(a) for\n(b) while\n(c) do-while\n(d) nested for\n", "ans": "c"},
    {"q": "What does OOP stand for?\n(a) Object Oriented Programming\n(b) Open Online Programming\n(c) Optional Output Process\n(d) None of these\n", "ans": "a"},
    {"q": "Which operator is used for exponentiation in Python?\n(a) ^\n(b) **\n(c) //\n(d) %\n", "ans": "b"},
    {"q": "Which of these is a Python library for data analysis?\n(a) pandas\n(b) matplotlib\n(c) numpy\n(d) All of the above\n", "ans": "d"},
    {"q": "Which data structure works on FIFO principle?\n(a) Stack\n(b) Queue\n(c) List\n(d) Dictionary\n", "ans": "b"},
    {"q": "Which function is used to find the length of a list in Python?\n(a) size()\n(b) count()\n(c) len()\n(d) length()\n", "ans": "c"},
    {"q": "Which file mode is used to add data without overwriting?\n(a) r\n(b) w\n(c) a\n(d) x\n", "ans": "c"}
]

def save_score(name, score):
    f = open("scores.txt", "a")
    f.write(f"{name},{score}\n")
    f.close()

def show_scores():
    try:
        f = open("scores.txt", "r")
        print("\n--- Scoreboard ---")
        for line in f:
            name, score = line.strip().split(",")
            print(f"{name}: {score} points")
        f.close()
    except FileNotFoundError:
        print("No scores recorded yet!")

def calculate_grade(score, total):
    percentage = (score / total) * 100
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "D"
    return percentage, grade

def start_quiz():
    name = input("Enter your name: ")
    print(f"\nWelcome {name}! Let's start the quiz.\n")
    print("Scoring System: +4 for correct, -1 for wrong.\n")
    score = 0
    random.shuffle(questions)
    for i, q in enumerate(questions, 1):
        print(f"Q{i}. {q['q']}")
        ans = input("Your answer (a/b/c/d): ").lower()
        if ans == q["ans"]:
            print("✅ Correct! +4 points\n")
            score += 4
        else:
            print(f"❌ Wrong! -1 point (Correct answer: '{q['ans']}')\n")
            score -= 1
    total = len(questions) * 4
    percentage, grade = calculate_grade(score, total)
    print(f"Quiz Over! {name}, your final score is {score}/{total}")
    print(f"Percentage: {percentage:.2f}% | Grade: {grade}")
    save_score(name, score)

def main():
    while True:
        print("\n===== COMPUTER SCIENCE QUIZ =====")
        print("1. Start Quiz")
        print("2. View Scoreboard")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            start_quiz()
        elif choice == "2":
            show_scores()
        elif choice == "3":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()