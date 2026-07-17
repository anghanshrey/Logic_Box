<div align="center">

```
██╗      ██████╗  ██████╗ ██╗ ██████╗    ██████╗  ██████╗ ██╗  ██╗
██║     ██╔═══██╗██╔════╝ ██║██╔════╝    ██╔══██╗██╔═══██╗╚██╗██╔╝
██║     ██║   ██║██║  ███╗██║██║         ██████╔╝██║   ██║ ╚███╔╝ 
██║     ██║   ██║██║   ██║██║██║         ██╔══██╗██║   ██║ ██╔██╗ 
███████╗╚██████╔╝╚██████╔╝██║╚██████╗    ██████╔╝╚██████╔╝██╔╝ ██╗
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝ ╚═════╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
```

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=20&duration=2200&pause=500&color=2C5364&center=true&vCenter=true&multiline=true&repeat=true&width=750&height=100&lines=Pattern+Generator+%2B+Number+Analyzer;while+True%3A+%E2%86%92+match%2Fcase+%E2%86%92+for+for;Star+Triangles+%E2%80%A2+Even%2FOdd+%E2%80%A2+Running+Sums;Built+for+Red+%26+White+Skill+Education)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![Libraries](https://img.shields.io/badge/External_Libraries-None_Required-black?style=for-the-badge)
![Assignment](https://img.shields.io/badge/Assignment-Logic_Box-2C5364?style=for-the-badge)

</div>

## 🧭 Table of Contents

[Overview](#-project-overview) • [Objective](#-objective) • [Example Output](#-example-output) • [Flow](#-program-flow) • [Features](#-features) • [Skills](#-skills-demonstrated) • [Getting Started](#-getting-started) • [Structure](#-project-structure) • [Video](#-video) • [Assumptions](#-assumptions) • [Tech Stack](#-tech-stack) • [Contact](#-contact-me)

---

## 📌 Project Overview

**Logic Box** is a simple, menu-based Python program that runs in the console. It lets the user pick from a small menu and then does one of two things: draw a star pattern, or look closely at a range of numbers (telling which are even, which are odd, and adding them all up).

The program keeps showing the menu again and again until the user chooses to exit, so it works like a small, repeatable tool rather than a one-time script.

<div align="center">

| 🔺 Pattern Printing | 🔢 Number Analysis | 🔁 Menu Loop |
|:---:|:---:|:---:|
| nested `for` loops | even / odd + sum | `while True` + `match` |

</div>

> Built for **Logic Box — Red & White Skill Education.**
> *"Quality is our Motto."*

---

## 🎯 Objective

Create a small interactive Python console app that shows how loops, conditions, and menus work together:

- Showing a repeating menu with `while True`
- Choosing what to do next with `match` / `case`
- Using nested loops to build a pattern
- Using `if` / `else` to check even and odd numbers
- Adding numbers together in a loop

---

## ✨ Features

- Shows a simple numbered menu every time the program runs
- **Option 1:** Asks for a number of rows and prints a star pattern that grows one row at a time
- **Option 2:** Asks for a start and end number, then:
  - Tells the user whether each number in that range is even or odd
  - Adds up all the numbers in the range and shows the total
- **Option 3:** Exits the program with a goodbye message
- Keeps looping back to the menu after each task, so the user can try again without restarting the program

---

## 🌊 Program Flow

<details open>
<summary><b>Click to collapse / expand the flow diagram</b></summary>

```mermaid
flowchart TD
    A([▶ Program Starts]) --> B[📋 Menu Is Shown]
    B --> C{User Picks Option}
    C -->|1| D[Ask rows → print star pattern]
    C -->|2| E[Ask start & end → check even/odd & sum]
    C -->|3| F([👋 Print goodbye & stop])
    D --> B
    E --> B

    style A fill:#0f2027,stroke:#2C5364,color:#fff
    style F fill:#0f2027,stroke:#2C5364,color:#fff
    style B fill:#2C5364,stroke:#0f2027,color:#fff
    style C fill:#2C5364,stroke:#0f2027,color:#fff
    style D fill:#16323f,stroke:#2C5364,color:#fff
    style E fill:#16323f,stroke:#2C5364,color:#fff
```

</details>

| Step | Stage | Description |
|:---:|---|---|
| 1 | **Show Menu** | Print the welcome text and the three menu options |
| 2 | **Take Choice** | Read the user's choice as a number and match it to an option |
| 3 | **Do the Task** | Run the pattern printer, the number analyzer, or exit |
| 4 | **Repeat** | Go back to Step 1 unless the user chose to exit |

---

## 🎬 Example Output

<details open>
<summary><b>▶ Option 1 — Pattern (Rows = 4)</b></summary>

```
Welcome to the Pattern Generator and Number Analyzer!
Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your Choice:1
Enter the number of rows for the pattern: 4
Pattern:

*
**
***
****
```

</details>

<details open>
<summary><b>▶ Option 2 — Number Range (2 to 5)</b></summary>

```
Enter your Choice:2
Enter the start of the range:2
Enter the end of the range:5
Number 2 is Even
Number 3 is odd
Number 4 is Even
Number 5 is odd
Sum of all numbers from 2 to 5 is: 14
```

</details>

<details open>
<summary><b>▶ Option 3 — Exit</b></summary>

```
Enter your Choice:3
Exiting the program. Goodbye!
```

</details>

> 💡 Notice the pattern's first line is always blank — that's because the loop counts rows from `0`, so the very first row prints zero stars. This is a normal, expected part of how the loop is written.

---

## 🎯 Skills Demonstrated

<div align="center">

![Menu Loop](https://img.shields.io/badge/Menu_Loop_(while_True)-████████████-2C5364?style=flat-square)
![Match Case](https://img.shields.io/badge/match_%2F_case-███████████-2C5364?style=flat-square)
![Nested Loops](https://img.shields.io/badge/Nested_for_Loops-████████████-2C5364?style=flat-square)
![Conditionals](https://img.shields.io/badge/if_%2F_else_Conditions-██████████-2C5364?style=flat-square)
![Running Total](https://img.shields.io/badge/Running_Total_(sum)-███████████-2C5364?style=flat-square)

</div>

- Building a menu that repeats using `while True`
- Directing the program's flow with `match` / `case`
- Printing shapes using loops inside loops
- Checking even and odd numbers with the `%` operator
- Keeping a running total while looping through a range

---

## ✅ Assignment Requirements Checklist

| Requirement | Status |
|---|:---:|
| Show a repeating menu until the user exits | ✅ |
| Let the user generate a star pattern | ✅ |
| Let the user analyze a range of numbers | ✅ |
| Show which numbers are even and which are odd | ✅ |
| Calculate and show the sum of the range | ✅ |
| Give the user a clean way to exit the program | ✅ |
| Uploaded with a simple, descriptive README | ✅ |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- No external libraries required

### Installation

```bash
git clone https://github.com/<your-username>/logic-box.git
cd logic-box
```

### Usage

```bash
python Logic_Box.py
```

When it runs, you'll see a menu. Type:
- `1` to draw a star pattern
- `2` to check numbers in a range for even/odd and get their sum
- `3` to exit the program

---

## 🎥 Video

Video link : https://drive.google.com/drive/folders/1OJMU2fV5-LjlDUGYVQ9MhGXtaX9Aq1rh?usp=sharing

---

## 📁 Project Structure

```
logic-box/
├── Logic_Box.py   # Main script
└── README.md      # Project documentation
```

---

## ⚠️ Assumptions

- The user always types a valid whole number for the menu choice; entering letters or symbols will crash the program, since no extra error handling was added beyond the negative-rows check.
- For Option 1, a negative number of rows shows an "Enter valid Number" message instead of a pattern, but the program does not ask again — it simply moves on.
- For Option 2, the start value is expected to be less than or equal to the end value; if `start` is bigger than `end`, the range will simply be empty and nothing will print.
- Choosing an option outside 1, 2, or 3 currently does nothing and just returns to the top of the loop, since there's no "invalid choice" message.

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Concepts demonstrated:** `while` loops, `match`/`case`, nested `for` loops, `if`/`else`, the `%` (modulo) operator, running totals

---

## 📬 Contact Me

<div align="center">

[![Gmail](https://img.shields.io/badge/Email-shreyanghan205%40gmail.com-2C5364?style=for-the-badge&logo=gmail&logoColor=white)](mailto:shreyanghan205@gmail.com)

</div>

---

<div align="center">

*"Quality is our Motto."* — Red & White Skill Education

</div>
