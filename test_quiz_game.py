import unittest
import os
import json
from quiz_game import calculate_question_score, load_scores, save_score, QUESTIONS

class TestQuizGame(unittest.TestCase):

    TEST_FILE = "scores.json"

    def tearDown(self):
        # Clean up test score file after each test
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    # ── Score Calculation Tests ────────────────────────────────────────────

    def test_correct_answer_gives_points(self):
        score = calculate_question_score(True, 5.0)
        self.assertGreater(score, 0)

    def test_wrong_answer_gives_zero(self):
        score = calculate_question_score(False, 5.0)
        self.assertEqual(score, 0)

    def test_fast_answer_scores_higher(self):
        fast_score = calculate_question_score(True, 2.0)
        slow_score = calculate_question_score(True, 25.0)
        self.assertGreater(fast_score, slow_score)

    def test_very_slow_answer_no_bonus(self):
        score = calculate_question_score(True, 60.0)
        self.assertEqual(score, 100)  # base only, no time bonus

    def test_base_score_is_100(self):
        # At exactly 30 seconds, time bonus = 0
        score = calculate_question_score(True, 30.0)
        self.assertEqual(score, 100)

    # ── Leaderboard Tests ──────────────────────────────────────────────────

    def test_save_and_load_score(self):
        entry = {"name": "TestUser", "score": 500, "correct": 4,
                 "total": 5, "accuracy": 80.0, "category": "Python"}
        save_score(entry)
        scores = load_scores()
        self.assertEqual(len(scores), 1)
        self.assertEqual(scores[0]["name"], "TestUser")

    def test_leaderboard_sorted_by_score(self):
        save_score({"name": "Alice", "score": 300, "correct": 3,
                    "total": 5, "accuracy": 60.0, "category": "Math"})
        save_score({"name": "Bob", "score": 500, "correct": 5,
                    "total": 5, "accuracy": 100.0, "category": "Math"})
        scores = load_scores()
        self.assertGreaterEqual(scores[0]["score"], scores[1]["score"])

    def test_leaderboard_max_10_entries(self):
        for i in range(15):
            save_score({"name": f"Player{i}", "score": i * 100,
                        "correct": 3, "total": 5,
                        "accuracy": 60.0, "category": "General Knowledge"})
        scores = load_scores()
        self.assertLessEqual(len(scores), 10)

    def test_empty_leaderboard(self):
        scores = load_scores()
        self.assertEqual(scores, [])

    # ── Questions Database Tests ───────────────────────────────────────────

    def test_all_categories_exist(self):
        for cat in ["Python", "General Knowledge", "Technology", "Math"]:
            self.assertIn(cat, QUESTIONS)

    def test_each_question_has_4_options(self):
        for cat, questions in QUESTIONS.items():
            for q in questions:
                self.assertEqual(len(q["options"]), 4,
                    f"Question in {cat} doesn't have 4 options: {q['question']}")

    def test_answer_index_is_valid(self):
        for cat, questions in QUESTIONS.items():
            for q in questions:
                self.assertIn(q["answer"], [0, 1, 2, 3],
                    f"Invalid answer index in {cat}: {q['question']}")

    def test_each_question_has_explanation(self):
        for cat, questions in QUESTIONS.items():
            for q in questions:
                self.assertIn("explanation", q)
                self.assertGreater(len(q["explanation"]), 0)


if __name__ == "__main__":
    unittest.main()
