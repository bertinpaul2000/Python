
# ☕ Coffee Machine (Python CLI Simulation)

This is a simple **command-line Coffee Machine simulation** written in Python. The user can order different types of coffee (espresso, latte, cappuccino), and the program checks for ingredient availability, processes payments, and updates resources.

---

## 📁 Project Structure

```
coffee_machine/
├── main.py             # Runs the main coffee machine loop
├── menu.py             # Defines menu items, ingredients, and prices
├── resources.py        # Stores available water, milk, and coffee quantities
└── money_machine.py    # Handles coin input and payment validation
```

---

## 🚀 How to Run

1. **Clone the Repository:**

```bash
git clone https://github.com/bertinpaul2000/Python.git
cd Python/coffee_machine
```

2. **Run the Coffee Machine**

Make sure Python 3 is installed. Then, run:

```bash
python main.py
```

---

## ☕ Available Drinks

- Espresso
- Latte
- Cappuccino

Each drink has a defined cost and ingredient requirement.

---

## 🔄 Features

- Prints menu and accepts user selection.
- Checks ingredient availability before processing.
- Accepts coin inputs (quarters, dimes, nickels, pennies).
- Calculates if payment is sufficient and returns change.
- Deducts used ingredients from the machine.
- Prints report showing remaining resources and profit.

---

## 🧠 Learning Highlights

Perfect for Python beginners to practice:

- Object-Oriented Programming (OOP)
- Modular file organization
- User input and loop control
- Basic arithmetic operations and conditionals

---

## 🚧 Future Enhancements

- Add new drinks or customizable drink options
- Implement GUI using `tkinter`
- Save report/logs to a file
- Add refill functionality

---

## 👨‍💻 Author

Developed by [@bertinpaul2000](https://github.com/bertinpaul2000)

---

## 📄 License

Licensed under the [MIT License](https://opensource.org/licenses/MIT).
