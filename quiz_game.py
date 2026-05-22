import random
import time
import json
import os

# ─── Quiz Questions Database ─────────────────────────────────────────────────

QUESTIONS = {
    "Python": [
        {
            "question": "What is the output of print(type([]))?",
            "options": ["<class 'list'>", "<class 'array'>", "<class 'tuple'>", "<class 'dict'>"],
            "answer": 0,
            "explanation": "[] creates an empty list, so type([]) returns <class 'list'>."
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["function", "def", "fun", "define"],
            "answer": 1,
            "explanation": "'def' is used to define functions in Python."
        },
        {
            "question": "What does len('hello') return?",
            "options": ["4", "5", "6", "error"],
            "answer": 1,
            "explanation": "'hello' has 5 characters, so len() returns 5."
        },
        {
            "question": "Which of these is a valid Python comment?",
            "options": ["// comment", "/* comment */", "# comment", "-- comment"],
            "answer": 2,
            "explanation": "Python uses # for single-line comments."
        },
        {
            "question": "What is the result of 3 ** 2 in Python?",
            "options": ["6", "9", "8", "32"],
            "answer": 1,
            "explanation": "** is the exponent operator. 3**2 = 3²= 9."
        },
    ],
    "General Knowledge": [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Berlin", "Paris", "Madrid"],
            "answer": 2,
            "explanation": "Paris is the capital and largest city of France."
        },
        {
            "question": "How many planets are in our solar system?",
            "options": ["7", "8", "9", "10"],
            "answer": 1,
            "explanation": "There are 8 planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune."
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
            "answer": 3,
            "explanation": "The Pacific Ocean is the largest, covering more than 30% of Earth's surface."
        },
        {
            "question": "Who invented the telephone?",
            "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Albert Einstein"],
            "answer": 1,
            "explanation": "Alexander Graham Bell is credited with inventing the telephone in 1876."
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["WA", "H2O", "HO2", "W2O"],
            "answer": 1,
            "explanation": "Water is H2O — 2 hydrogen atoms and 1 oxygen atom."
        },
    ],
    "Technology": [
        {
            "question": "What does 'CPU' stand for?",
            "options": ["Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Core Processing Unit"],
            "answer": 0,
            "explanation": "CPU stands for Central Processing Unit — the brain of a computer."
        },
        {
            "question": "What does 'HTML' stand for?",
            "options": ["Hyper Text Markup Language", "High Tech Modern Language", "Hyper Transfer Markup Logic", "Home Tool Markup Language"],
            "answer": 0,
            "explanation": "HTML stands for HyperText Markup Language, used to build web pages."
        },
        {
            "question": "Which company created the Python programming language?",
            "options": ["Microsoft", "Google", "No company — Guido van Rossum created it", "Apple"],
            "answer": 2,
            "explanation": "Python was created by Guido van Rossum and first released in 1991."
        },
        {
            "question": "What does 'RAM' stand for?",
            "options": ["Read Access Memory", "Random Access Memory", "Run Active Memory", "Rapid Action Module"],
            "answer": 1,
            "explanation": "RAM stands for Random Access Memory — temporary fast storage for running programs."
        },
        {
            "question": "What is GitHub primarily used for?",
            "options": ["Video editing", "Version control and code hosting", "3D modeling", "Music production"],
            "answer": 1,
            "explanation": "GitHub is a platform for version control and collaboration using Git."
        },
    ],
    "Math": [
        {
            "question": "What is the square root of 144?",
            "options": ["11", "12", "13", "14"],
            "answer": 1,
            "explanation": "√144 = 12, because 12 × 12 = 144."
        },
        {
            "question": "What is 15% of 200?",
            "options": ["25", "30", "35", "40"],
            "answer": 1,
            "explanation": "15% of 200 = (15/100) × 200 = 30."
        },
        {
            "question": "What is the value of π (pi) to 2 decimal places?",
            "options": ["3.12", "3.14", "3.16", "3.18"],
            "answer": 1,
            "explanation": "Pi (π) ≈ 3.14159..., rounded to 2 decimal places = 3.14."
        },
        {
            "question": "How many degrees are in a right angle?",
            "options": ["45", "60", "90", "180"],
            "answer": 2,
            "explanation": "A right angle is exactly 90 degrees."
        },
        {
            "question": "What is 2 to the power of 8?",
            "options": ["128", "256", "512", "64"],
            "answer": 1,
            "explanation": "2^8 = 2×2×2×2×2×2×2×2 = 256."
        },
    ],
}


# ─── Score Tracker ────────────────────────────────────────────────────────────

SCORES_FILE = "scores.json"

def load_scores():
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r") as f:
            return json.load(f)
    return []

def save_score(entry):
    scores = load_scores()
    scores.append(entry)
    scores.sort(key=lambda x: x["score"], reverse=True)
    with open(SCORES_FILE, "w") as f:
        json.dump(scores[:10], f, indent=2)  # Keep top 10

def display_leaderboard():
    scores = load_scores()
    if not scores:
        print("\n  📋 No scores yet — be the first to play!\n")
        return

    print(f"\n{'='*55}")
    print(f"  🏆 LEADERBOARD — Top Scores")
    print(f"{'='*55}")
    medals = ["🥇", "🥈", "🥉"] + ["🎖️"] * 7

    for i, entry in enumerate(scores[:10]):
        print(f"  {medals[i]} {i+1}. {entry['name']:<15} "
              f"{entry['score']:>5} pts  |  "
              f"{entry['category']}  |  "
              f"{entry['correct']}/{entry['total']} correct")
    print(f"{'='*55}\n")


# ─── Quiz Engine ──────────────────────────────────────────────────────────────

def choose_category():
    categories = list(QUESTIONS.keys()) + ["🎲 Random Mix"]
    print("\n  📚 Choose a Category:")
    for i, cat in enumerate(categories, 1):
        count = len(QUESTIONS.get(cat, [q for qs in QUESTIONS.values() for q in qs]))
        print(f"    {i} → {cat}")

    while True:
        choice = input("\n  Your choice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            selected = categories[int(choice) - 1]
            if selected == "🎲 Random Mix":
                all_q = [q for qs in QUESTIONS.values() for q in qs]
                return "Random Mix", all_q
            return selected, QUESTIONS[selected]
        print("  ⚠️  Invalid choice, try again.")


def choose_num_questions(max_q):
    print(f"\n  How many questions? (1–{max_q})")
    while True:
        choice = input("  Your choice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= max_q:
            return int(choice)
        print(f"  ⚠️  Please enter a number between 1 and {max_q}.")


def ask_question(q_num, total, question_data):
    print(f"\n{'─'*55}")
    print(f"  Question {q_num}/{total}")
    print(f"\n  ❓ {question_data['question']}\n")

    options = question_data["options"]
    for i, opt in enumerate(options):
        print(f"    {i+1}. {opt}")

    start = time.time()
    while True:
        answer = input("\n  Your answer (1-4): ").strip()
        if answer.isdigit() and 1 <= int(answer) <= 4:
            time_taken = time.time() - start
            return int(answer) - 1, round(time_taken, 1)
        print("  ⚠️  Please enter 1, 2, 3, or 4")


def calculate_question_score(correct, time_taken):
    if not correct:
        return 0
    base = 100
    time_bonus = max(0, int(30 - time_taken) * 3)
    return base + time_bonus


def play_quiz():
    name = input("\n  👤 Enter your name: ").strip() or "Player"
    category, questions = choose_category()
    random.shuffle(questions)
    num_q = choose_num_questions(len(questions))
    selected_questions = questions[:num_q]

    print(f"\n{'='*55}")
    print(f"  🎮 Quiz Starting!")
    print(f"  Player   : {name}")
    print(f"  Category : {category}")
    print(f"  Questions: {num_q}")
    print(f"  Scoring  : 100 pts/correct + up to 90 speed bonus")
    print(f"{'='*55}")
    input("\n  Press Enter to start...")

    total_score = 0
    correct_count = 0
    results = []

    for i, q_data in enumerate(selected_questions, 1):
        user_answer, time_taken = ask_question(i, num_q, q_data)
        correct = user_answer == q_data["answer"]
        score = calculate_question_score(correct, time_taken)
        total_score += score

        if correct:
            correct_count += 1
            print(f"\n  ✅ Correct! +{score} points (answered in {time_taken}s)")
        else:
            correct_option = q_data["options"][q_data["answer"]]
            print(f"\n  ❌ Wrong! The answer was: {correct_option}")

        print(f"  💡 {q_data['explanation']}")
        results.append({"question": q_data["question"], "correct": correct, "time": time_taken})

    # Final results
    accuracy = (correct_count / num_q) * 100
    if accuracy == 100:
        grade = "🏆 Perfect Score!"
    elif accuracy >= 80:
        grade = "🌟 Excellent!"
    elif accuracy >= 60:
        grade = "👍 Good Job!"
    elif accuracy >= 40:
        grade = "📚 Keep Practicing!"
    else:
        grade = "💪 Don't Give Up!"

    print(f"\n{'='*55}")
    print(f"  🎉 Quiz Complete! — {grade}")
    print(f"  Player   : {name}")
    print(f"  Score    : {total_score} points")
    print(f"  Correct  : {correct_count}/{num_q} ({accuracy:.0f}%)")
    avg_time = sum(r["time"] for r in results) / len(results)
    print(f"  Avg Time : {avg_time:.1f}s per question")
    print(f"{'='*55}\n")

    # Save score
    save_score({
        "name": name,
        "score": total_score,
        "correct": correct_count,
        "total": num_q,
        "accuracy": round(accuracy, 1),
        "category": category,
    })
    print(f"  ✅ Score saved to leaderboard!\n")


# ─── Main Menu ────────────────────────────────────────────────────────────────

def run():
    print("=" * 55)
    print("   🎯 Quiz Game with Score Tracker")
    print("   Test your knowledge & climb the leaderboard!")
    print("=" * 55)

    while True:
        print("\n  1 → Play Quiz")
        print("  2 → View Leaderboard")
        print("  3 → Quit")

        choice = input("\n  Your choice: ").strip()

        if choice == "1":
            play_quiz()
        elif choice == "2":
            display_leaderboard()
        elif choice == "3":
            print("\n  👋 Thanks for playing!\n")
            break
        else:
            print("  ⚠️  Please enter 1, 2, or 3")


# ─── Entry Point ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    run()
