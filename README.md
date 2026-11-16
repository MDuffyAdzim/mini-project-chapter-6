# 🎓 Student Skill Manager

A Python mini project developed as part of the learning journey through **Python Crash Course (3rd Edition), Chapter 6 — Dictionaries**.

## 📖 Overview

Student Skill Manager is a Python-based program designed to manage student skill information through an interactive terminal interface.

The program allows users to view student information, explore competencies expected by the university, check skills recorded in individual student profiles, and discover unique skills across the student database.

This project aims to demonstrate how Python dictionaries and other fundamental programming concepts can be combined to organize and process structured information.

It also illustrates how accessible skill information can help students identify competencies they may want to develop for their future careers.

## ✨ Features

### 1. Display All Students
Displays all student information stored in the system, including Student ID (NPM), name, major, and registered skills.

### 2. Required Campus Skills
Displays the core competencies expected by the university. Students can use this list as a reference when identifying skills to develop for their career preparation.

### 3. Check Student Skills
Allows users to enter a student's NPM and a specific skill to check whether that skill is recorded in the student's profile.

### 4. Display Unique Skills
Collects skills from all student profiles, removes duplicate entries, and displays the results in alphabetical order.

### 5. Exit Program
Allows users to exit the application and end the current session.

## 🛠️ Technologies Used

- **Python 3.12.13** — Programming language.
- **Visual Studio Code** — Development environment.

## 🧠 Python Concepts Applied

This project applies fundamental Python concepts, including:

- **Dictionaries:** Store student information using NPM as the key.
- **Nested Dictionaries:** Organize each student's name, major, and skills.
- **Lists:** Store individual student skills and campus-required competencies.
- **For Loops:** Iterate through student records and skill collections.
- **While Loops:** Keep the interactive menu running.
- **Conditional Statements:** Control menu navigation and skill-checking logic.
- **Dictionary Methods:** Use `.items()` and `.get()` to access dictionary data.
- **Membership Operators:** Use `in` and `not in` to check whether data exists.
- **Set:** Remove duplicate skills.
- **Sorting:** Use `sorted()` to arrange unique skills alphabetically.
- **String Methods:** Use `.join()` to combine skill names into readable output.
- **Exception Handling:** Use `try-except` to handle invalid numeric input.
- **Loop Control:** Use `continue` and `break` to control program execution.

## 🗂️ Data Structure

The program uses a nested dictionary as its primary data structure.

Each student is identified by their NPM, which serves as the dictionary key.

Each student record contains:

| Key | Description | Data Type |
|---|---|---|
| `name` | Student's name | String |
| `major` | Student's academic major | String |
| `skills` | List of registered skills | List |

The program also uses a separate list named `demand_skill` to store competencies expected by the university.

## 🚀 How to Run

### Prerequisites

- Python 3 installed on your computer.
- A terminal or code editor such as Visual Studio Code.

### Steps

1. Clone or download this repository.
2. Open the project folder in Visual Studio Code.3. Open the terminal in the project directory.
4. Run the following command:

```bash
python student_skill_manager.py
```

5. Follow the interactive menu displayed in the terminal.

## 📌 Project Scope

This is a fundamental Python learning project.

Student records and campus-required skills are predefined directly in the source code. The current version supports viewing and checking information but does not include persistent database storage or user-driven student record management.

## 🎯 Learning Objectives

- Understand and apply Python dictionaries.
- Work with nested data structures.
- Process collections using loops and conditional statements.
- Use dictionary methods and membership operators.
- Apply sets and sorting to process data.
- Build a simple interactive terminal-based application.
- Develop problem-solving and programming skills through a practical project.

## 👨‍💻 Author

**Muhammad Duffy Adzim**

Python Fundamentals Learning Journey

Future AI Engineer 🚀