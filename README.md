# Python Lab

Python Lab is my personal Python learning repository, created as part of my journey toward becoming a software engineer.

This repository is where I practice Python by building small programs, solving problems, experimenting with ideas, and gradually applying the concepts I learn through the Talent Nation software engineering curriculum.

The goal is not simply to complete exercises or collect working programs. I am using these projects to develop the ability to understand problems, break them down, write and debug code, test solutions, and explain the decisions behind my implementations.

## Learning Focus

My Python learning is currently focused on building a strong foundation before moving into more advanced software engineering concepts.

The areas I am working through include:

* Programming fundamentals
* Computational thinking and problem solving
* Variables and data types
* Conditional statements
* Loops and control flow
* Strings
* Functions and scope
* Python data structures
* Object-oriented programming
* Algorithms and data structures
* Advanced Python features
* Modules and packages
* Virtual environments
* Testing
* Error handling
* Concurrency

As I progress, the repository will grow with more projects and exercises that demonstrate these concepts in practice.

## Learning Approach

I am following an adaptive learning approach rather than simply going through lessons one after another.

For each important concept, I aim to move through several stages:

```text
Learn
   ↓
Understand
   ↓
Predict
   ↓
Implement
   ↓
Debug
   ↓
Test
   ↓
Apply
   ↓
Transfer
```

This means that getting a program to work is only part of the process.

I also want to be able to explain how the code works, identify problems, handle edge cases, debug failures, and apply the same idea to a different problem.

## Projects

Projects in this repository are intentionally kept at different levels of difficulty.

Some are small exercises designed to practice a single concept, while others will combine multiple concepts into a more complete application.

### NumMystery

**NumMystery** is a simple command-line number guessing game.

The program generates a random number between 1 and 10 and allows the player to keep guessing until the correct number is found. It also provides feedback when a guess is too high or too low and handles invalid input.

This was one of my early projects for practicing Python fundamentals.

Concepts practiced include:

* Functions
* Variables
* User input
* Conditional statements
* `while` loops
* Error handling
* The `random` module
* String formatting
* Program flow

Project:

```text
NumMystery/
├── NumMystery.py
└── README.md
```

### Task Keeper CLI V2

**Task Keeper CLI V2** is a command-line task management application built with Python.

It allows users to create tasks, view saved tasks, mark tasks as completed, and delete tasks through an interactive terminal interface.

This is the second version of my CLI task manager. It builds on my previous attempt with improvements to code organisation, data persistence, input validation, and the overall terminal experience.

The application stores task records in a JSON file, allowing tasks to remain available between program sessions. It also features an animated welcome screen and a colourful task display to improve the user experience.

Concepts practiced include:

* Functions and modular programming
* Lists and dictionaries
* File handling
* JSON serialization and deserialization
* Reading and writing persistent data
* Exception handling
* Input validation
* Loops and conditional statements
* Modules and packages
* Python imports
* The `pathlib` module
* The `sys` and `time` modules
* Terminal colours and text animation
* Application entry points using `if __name__ == "__main__":`

Project:

```text
Task_Keeper/
├── data/
│   └── tasks.json
│
├── package/
│   ├── __init__.py
│   ├── storage.py
│   └── utils.py
│
├── main.py
└── README.md
```

## Repository Structure

The repository will continue to evolve as I progress through my learning path.

```text
Python_Lab/
│
├── NumMystery/
│   ├── NumMystery.py
│   └── README.md
│
├── Task_Keeper/
│   ├── data/
│   │   └── tasks.json
│   │
│   ├── package/
│   │   ├── __init__.py
│   │   ├── storage.py
│   │   └── utils.py
│   │
│   ├── main.py
│   └── README.md
│
└── README.md
```

Additional projects and exercises will be added as new concepts are introduced.

## Engineering Skills I Am Building

Beyond learning Python syntax, I am using these projects to develop broader software engineering skills.

### Problem Solving

Learning how to take a problem, identify the requirements, break it into smaller parts, and develop a logical solution before writing code.

### Debugging

Learning to investigate problems instead of randomly changing code.

My debugging process is gradually becoming:

```text
Observe
   ↓
Reproduce
   ↓
Read the error
   ↓
Identify the failure
   ↓
Form a hypothesis
   ↓
Test the hypothesis
   ↓
Fix
   ↓
Verify
```

### Testing

Learning to think about expected behaviour, edge cases, and how to verify that a solution actually works.

### Code Quality

As my skills improve, I am learning to think beyond code that simply works and consider:

* Readability
* Maintainability
* Simplicity
* Error handling
* Testing
* Performance
* Reusability
* Design decisions

### Documentation

I am also learning how to use official documentation as part of the development process instead of relying entirely on tutorials or AI-generated answers.

The goal is to become comfortable finding information, understanding documentation, testing what I find, and applying it correctly.

## AI-Assisted Learning

AI is part of my learning workflow, but the goal is not to use AI as a replacement for understanding.

When using AI-generated code or explanations, I aim to understand:

* What the code is doing
* Why it works
* What assumptions it makes
* What could go wrong
* How I could modify it
* How I could verify it independently

The long-term goal is to become capable of solving unfamiliar problems independently, with AI serving as a tool rather than a substitute for engineering ability.

## Tools and Technologies

My primary focus in this repository is Python.

As my broader software engineering journey develops, I will also work with technologies such as:

* Python
* JavaScript
* HTML
* CSS
* React
* Go
* REST APIs
* Databases
* Git and GitHub

Technologies will be introduced progressively as they become relevant to the learning path.

## Running the Projects

Clone the repository:

```bash
git clone https://github.com/EkwuemeSpace/Python_Lab.git
```

Move into the repository:

```bash
cd Python_Lab
```

Navigate to the project you want to run.

For example, to run NumMystery:

```bash
cd NumMystery
python NumMystery.py
```

On systems where Python is accessed using `python3`:

```bash
python3 NumMystery.py
```

To run Task Keeper CLI V2, navigate into its project directory:

```bash
cd Task_Keeper
python3 main.py
```

Individual projects may have additional setup instructions in their own README files.

## Progress

This repository is a work in progress.

I will continue adding projects, exercises, experiments, and improvements as I move through my Python learning path.

The code in this repository represents my progress over time. Some early projects may be simple, and I may revisit them later to improve their structure, readability, testing, or overall design.

## What Success Looks Like

The purpose of this repository is bigger than simply learning Python.

The long-term goal is to become capable of taking an unfamiliar software problem and working through it independently:

```text
Understand the problem
       ↓
Clarify the requirements
       ↓
Break the problem down
       ↓
Choose an approach
       ↓
Write the code
       ↓
Test it
       ↓
Debug it
       ↓
Review it
       ↓
Improve it
       ↓
Explain the solution
```

Python Lab is one part of that journey.

---

**Learning by building, breaking, debugging, and improving.**