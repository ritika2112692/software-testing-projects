Selenium-based testing using Edge WebDriver

Local HTML Todo List with login/signup functionality

Target audience: MCA (AI & ML) student or developer

markdown
Copy
Edit
# Enhanced Todo List Automation (MCA AI/ML Project)

This project demonstrates automated UI testing of a feature-rich Todo List web application using **Selenium WebDriver** with Python. The HTML-based app includes login and signup features, and the test suite validates core functionalities like user registration, login, and task management.

## 🔧 Features

- ✅ Automated browser tests using Selenium
- ✅ Edge WebDriver integration
- ✅ HTML-based Todo App with:
  - User login/signup
  - Add/edit/delete todo items
  - LocalStorage-based user and task persistence
- ✅ Modular test structure (`BaseTest`)
- ✅ Simple and stylish UI with animations

## 📂 Project Structure

.
├── base_test.py # Selenium test base for login/signup automation
├── enhanced_todo_list.html # HTML frontend with todo list + login system
├── msedgedriver.exe # Edge browser driver
├── EULA # License file (if any)
└── README.md # This file

markdown
Copy
Edit

## 🚀 How to Run the Test

1. Make sure you have **Python 3.12+** and **Selenium** installed:

```bash
pip install selenium
Launch the HTML file in a browser locally or serve it using a lightweight server if needed.

Run the test:

bash
Copy
Edit
python base_test.py
⚠️ Ensure the file paths in base_test.py point correctly to your local msedgedriver.exe and enhanced_todo_list.html.

💡 Ideal For
MCA students (AI & ML specialization)

Beginners learning Selenium automation

Practicing test-driven web development
