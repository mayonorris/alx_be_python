# Programming Paradigm — OOP, Exceptions & Testing (Week Project)

**Repository:** `alx_be_python`  
**Directory:** `programming_paradigm`

This week you’ll wire together three pillars of professional Python: **Object-Oriented Programming**, **robust exception handling**, and **unit testing**. You’ll design small, focused modules and verify behavior via the command line and tests.

---

## 🚀 Overview

You will implement and/or test four deliverables:

1) **Bank Account (OOP + CLI glue)**  
   - `bank_account.py` — encapsulates balance, deposit/withdraw/display behaviors  
   - `main-0.py` — uses command-line arguments to exercise the class

2) **Robust Division (exceptions + CLI)**  
   - `robust_division_calculator.py` — safe division with error handling  
   - `main.py` — parses CLI args and prints the result string

3) **Unit Tests for SimpleCalculator (testing basics)**  
   - `simple_calculator.py` — **provided** class (add/subtract/multiply/divide)  
   - `test_simple_calculator.py` — your tests using `unittest`

4) **Library Management (OOP interactions)**  
   - `library_management.py` — `Book` + `Library` classes; print available books  
   - `main.py` (provided in the task statement) — demonstrates end-to-end usage

---

## 🎯 Learning Objectives

- Explain OOP core concepts: **classes, objects, encapsulation, abstraction**.  
- Define classes & create objects; distinguish **instance attributes**, **instance methods**, and the role of `self`.  
- Differentiate **syntax errors** vs **exceptions**; handle exceptions with `try / except / else / finally`; raise custom errors.  
- Understand the value of **testing**; write **unit tests** with `unittest` and run them via test runners.  

---

## 📁 Project Layout (expected)

```text
alx_be_python/
└─ programming_paradigm/
├─ bank_account.py
├─ main-0.py # CLI for BankAccount (provided pattern)
├─ robust_division_calculator.py
├─ main.py # CLI for robust division (provided pattern)
├─ simple_calculator.py # provided
├─ test_simple_calculator.py # your tests
└─ library_management.py
```


> **Naming/paths matter** — checkers typically regex-match file names and exact output strings.

---

## 🧰 Prerequisites & Setup

- Python **3.10+** recommended
- (Optional) virtual environment

```bash
cd alx_be_python/programming_paradigm
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
python -m pip install --upgrade pip
```

## 📄 License (MIT)

Copyright © 2025 Mayo Takémsi Norris KADANGA