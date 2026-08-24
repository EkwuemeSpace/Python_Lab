# NumMystery

NumMystery is a simple number guessing game I built with Python.

The idea is straightforward: the program randomly picks a number between 1 and 10, and the player keeps guessing until they get the right number. The program gives a hint after each wrong guess to let the player know whether their guess was too high or too low.

## What the Game Does

When the program starts, it asks for the player's name and then generates a secret number.

The player enters a number between 1 and 10. If the guess is:

* Lower than the secret number, the game says the guess is too low.
* Higher than the secret number, the game says the guess is too high.
* The same as the secret number, the player wins.

After a successful guess, the player can choose to play another round or exit the game.

## Technologies Used

* Python 3
* Python's `random` module
* `while` loops
* `if`, `elif`, and `else` statements
* Functions
* `try` and `except` for handling invalid input
* User input with `input()`
* f-strings for displaying messages

## Project Structure

```text
python-lab/
└── NumMystery/
    ├── NumMystery.py
    └── README.md
```

## How to Run It

Open your terminal and move into the project folder:

```bash
cd python-lab/NumMystery
```

Then run the program:

```bash
python NumMystery.py
```

If your computer uses `python3` instead of `python`, you can run:

```bash
python3 NumMystery.py
```

## How to Play

After starting the program, enter your name when prompted.

The game will then tell you that it has picked a number between 1 and 10.

Enter your guess and use the feedback from the game to make another guess until you find the secret number.

Once you get the correct number, the game will ask if you want to play again.

To stop playing, enter `no`, `exit`, or `quit`.

## What I Learned From This Project

I built this project to get more comfortable with some of the basic concepts in Python.

One of the main things I practiced was using loops. The game needs to keep running while the player is guessing, so I used `while` loops to control that flow.

I also practiced conditional statements to compare the player's guess with the secret number.

Another important part was handling invalid input. If the player enters something that cannot be converted to an integer, the program catches the error instead of crashing.

I also used Python's `random` module to generate a different secret number for each round.

## Possible Improvements

There are still several things I could add to the game as I continue learning Python:

* Keep track of how many attempts the player makes.
* Add a scoring system.
* Add different difficulty levels.
* Allow the player to choose the number range.
* Set a maximum number of attempts.
* Save the player's best score.
* Add more game statistics.

## Project Status

This is a beginner Python project that I created as part of my Python learning journey.

The main goal was not to build a complicated game, but to practice writing Python code and understand how different programming concepts work together in a small project.
