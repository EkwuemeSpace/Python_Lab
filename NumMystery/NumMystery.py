import random

def number_puzzle():
    print("🎉 Welcome to the Number Puzzle Game!")
    name = input("What should I call you? ")

    while True:
        secret_code = random.randint(1, 10)
        print(f"\nAlright {name}, I’ve picked a secret number between 1 and 10.")
        print("Can you guess it? 🤔")

        while True:
            try:
                guess = int(input("👉 Enter your guess: "))
            except ValueError:
                print("❌ Error: ONLY numbers allowed!")
                continue

            if guess < 1 or guess > 10:
                print("⚠️ Please choose a number between 1 and 10 only.")
                continue

            if guess < secret_code:
                print(f"Too low, {name}! Try again 🔽")
            elif guess > secret_code:
                print(f"Too high, {name}! Try again 🔼")
            else:
                print(f"🎊 Congratulations {name}, you cracked the code! 😊")
                break

        # Ask if the user wants to play again or exit
        choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if choice in ["no", "exit", "quit"]:
            print(f"👋 Thanks for playing, {name}! See you next time.")
            break

# Run the game
number_puzzle()
