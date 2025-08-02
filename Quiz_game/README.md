
# 🧠 Quiz Game (Python CLI)

This is a simple **command-line Quiz Game** built with Python. The game allows users to test their general knowledge by answering a series of multiple-choice questions. The game provides instant feedback on the correctness of each answer and shows the final score at the end.

---

## 📁 Project Structure

```
Quiz_game/
├── main.py             # Entry point for the quiz game
├── questions.py        # Contains all quiz questions and answers
└── utils.py            # Helper functions for evaluating and displaying results
```

---

## 🚀 How to Run

1. **Clone the Repository:**

```bash
git clone https://github.com/bertinpaul2000/Python.git
cd Python/Quiz_game
```

2. **Run the Quiz Game:**

Make sure Python 3 is installed on your system. Then, execute:

```bash
python main.py
```

---

## 🎮 Gameplay Features

- Presents a series of multiple-choice questions.
- User selects an answer by typing the corresponding letter.
- Immediate feedback is given after each response.
- Displays the correct answers at the end along with the final score.

---

## 🛠️ Code Overview

- **`main.py`** – Drives the game logic, collects answers, shows results.
- **`questions.py`** – Stores the questions and the correct answers.
- **`utils.py`** – Contains functions like:
  - `check_answer()` – Compares user input with correct answer.
  - `display_score()` – Shows the user's performance summary.

---

## 👨‍🎓 Learning Objectives

Ideal for Python beginners looking to practice:

- Working with functions and modules
- Handling user input and conditionals
- Organizing code for reusability

---

## 🚧 Future Improvements

- Add question categories and difficulty levels.
- Introduce a countdown timer per question.
- Store high scores using files or databases.
- Build a GUI version using `tkinter` or a web version using Flask.

---

## 👨‍💻 Author

Developed by [@bertinpaul2000](https://github.com/bertinpaul2000)

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
