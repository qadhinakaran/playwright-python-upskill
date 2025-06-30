# Playwright + Python Upskill Journey 🚀

This repository tracks my learning and practice while upskilling in **Playwright with Python** for automation testing.

---

## 📅 Weekly Progress

### 🔷 Week 1: Python & Playwright Fundamentals
📅 **What I Learned**
* ✅ Set up the Python development environment and installed Playwright
* ✅ Launched browser instances and navigated to web pages using Playwright
* ✅ Wrote and executed the first test script with basic assertions

📁 **Python Practice Topics**
* ✅ Basic Data Types & Operations
* ✅ Control Flow: `if` conditions, `for` and `while` loops
* ✅ Collections: Lists, Tuples, and Dictionaries
* ✅ Functions & Classes: Function definitions and parameterization
* ✅ OOP Concepts: Classes, Objects, Constructors, Inheritance, and Method Overriding

### 🔷 Week 2: String Methods & File Handling Basics
📅 **What I Learned**
* ✅ Indexed, sliced, concatenated, and searched strings (in operator)
* ✅ Used key string methods: split(), strip(), rstrip(), and lstrip()
* ✅ Read text files with open() in read mode using read(), read(n), readline(), and readlines()
* ✅ Iterated over file lines with a for loop
* ✅ Reversed file content line-by-line and wrote it to reverse.txt

📁 **Python Practice Topics**
* ✅ String Operations: indexing [], slicing [start:end], concatenation +, membership tests
* ✅ String Methods: split, strip, rstrip, lstrip
* ✅ File Handling Fundamentals: open, modes (r, w), read, readline, readlines
* ✅ Looping through lists (including lists returned by readlines())
* ✅ Writing to files and verifying output by reading back

### 🔷 Week 3: Pytest Fixtures
📅 **What I Learned**
* ✅ What are pytest fixtures and how they help in tests
* ✅ Fixture scopes: function, class, module, session
* ✅ Setup and teardown using yield in fixtures

📁 **Practice Topics**
* ✅ Reusability in tests using fixtures
* ✅ Scoping strategies in pytest
* ✅ Resource management with yield-based teardown

---

## 📁 Repository Structure

```
playwright-python-upskill/
├──Python Basics
|  └──Week1_Basics/
│     ├── browser_launch.py
│     └── first_test.py
│
|  └──Week2_Fixtures/
│       ├── conftest.py
│       └── test_with_fixtures.py
│
├── README.md
└── .gitignore
```


---

# 1. Clone the repo
git clone https://github.com/yourusername/playwright-python-upskill.git
cd playwright-python-upskill

# 2. Install dependencies
python -m venv venv && source venv/bin/activate  # optional virtual-env
pip install -r requirements.txt                  # pytest + playwright
playwright install                               # downloads browser binaries

# 3. Run all tests
pytest -v

---

📌 Goals
### 🧪 Web Automation with Playwright + Python
- ✅ Set up Python, Playwright, and environment
- ✅ Learn selectors, assertions, and browser automation
- ✅ Use Fixtures to create reusable test setups
- ⏳ Implement Page Object Model (POM)
- ⏳ Automate complex UI workflows
- ⏳ Run tests in parallel across browsers

### 🔗 API Automation with Playwright and Python
- ⏳ Understand REST APIs and HTTP methods
- ⏳ Write API test cases with validations
- ⏳ Chain Web + API test scenarios

### 🧱 Pytest + BDD Framework
- ⏳ Integrate Pytest with BDD (Gherkin)
- ⏳ Write feature files with step definitions
- ⏳ Execute BDD scenarios with fixtures and reports

### 📈 Final Objective
> Become a complete Playwright Python Automation Engineer capable of handling both 
Web UI and API testing using industry-level BDD Frameworks.

