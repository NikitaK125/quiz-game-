# 🎯 Quiz Game with Score Tracker

A Python quiz game with **4 categories**, **speed-based scoring**, **explanations** for every answer, and a **persistent leaderboard** saved to a file!

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 💻 Demo

```
=======================================================
   🎯 Quiz Game with Score Tracker
=======================================================

  1 → Play Quiz
  2 → View Leaderboard
  3 → Quit

  👤 Enter your name: Nikita

  📚 Choose a Category:
    1 → Python
    2 → General Knowledge
    3 → Technology
    4 → Math
    5 → 🎲 Random Mix

───────────────────────────────────────────────────────
  Question 1/5

  ❓ What is the result of 3 ** 2 in Python?

    1. 6
    2. 9
    3. 8
    4. 32

  Your answer (1-4): 2

  ✅ Correct! +145 points (answered in 4.8s)
  💡 ** is the exponent operator. 3**2 = 3² = 9.

=======================================================
  🎉 Quiz Complete! — 🌟 Excellent!
  Player   : Nikita
  Score    : 623 points
  Correct  : 4/5 (80%)
  Avg Time : 6.2s per question
=======================================================
```

---

## ✨ Features

- 📚 **4 categories** — Python, General Knowledge, Technology, Math
- 🎲 **Random Mix mode** — questions from all categories
- ⚡ **Speed bonus scoring** — answer faster for more points
- 💡 **Explanations** — learn why each answer is correct
- 🏆 **Persistent leaderboard** — top 10 scores saved to file
- 🎖️ **Grade system** — Perfect / Excellent / Good / Keep Practicing
- 🔀 **Shuffled questions** — different order every game
- ✅ Zero external dependencies

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/quiz-game.git

# Navigate into folder
cd quiz-game

# Run the game
python quiz_game.py
```

---

## 🧪 Run Tests

```bash
python test_quiz_game.py
```

---

## 📁 Project Structure

```
quiz-game/
│
├── quiz_game.py          # Main game
├── test_quiz_game.py     # Unit tests
├── requirements.txt      # Dependencies (none!)
├── scores.json           # Auto-created leaderboard file
└── README.md             # You are here
```

---

## 🏆 Scoring System

| Factor | Points |
|---|---|
| Correct answer | +100 base |
| Speed bonus (per second under 30s) | +3 pts/sec |
| Max possible per question | +190 pts |
| Wrong answer | 0 pts |

---

## 📊 Grade System

| Accuracy | Grade |
|---|---|
| 100% | 🏆 Perfect Score! |
| 80–99% | 🌟 Excellent! |
| 60–79% | 👍 Good Job! |
| 40–59% | 📚 Keep Practicing! |
| Below 40% | 💪 Don't Give Up! |

---

## 🌱 Future Improvements

- [ ] Add more question categories (Science, Sports, Movies)
- [ ] Timed countdown per question
- [ ] Multiplayer mode
- [ ] GUI version using Tkinter
- [ ] Load questions from an external JSON file

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

Made with ❤️ and Python by **YOUR_NAME**  
⭐ Star this repo if you found it helpful!
