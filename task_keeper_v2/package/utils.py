from package.storage import DATA_FILE

import time, sys

# Terminal colours
CYAN = "\033[96m"
PURPLE = "\033[95m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
GREY = "\033[90m"
BOLD = "\033[1m"
RESET = "\033[0m"


def animate_text(message, delay=0.025):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def welcome():

    # Clear terminal
    print("\033[2J\033[H", end="")

    print(CYAN + BOLD)
    print("  ╔══════════════════════════════════════════════════╗")
    print("  ║                                                  ║")
    print("  ║             T A S K   K E E P E R                ║")
    print("  ║                                                  ║")
    print("  ║                YOUR PRODUCTIVITY HUB             ║")
    print("  ║                                                  ║")
    print("  ╚══════════════════════════════════════════════════╝")
    print(RESET)

    time.sleep(0.5)

    animate_text(GREEN + BOLD + "\n  Welcome aboard! Let's get things done." + RESET)

    print(WHITE + "\n  Task Keeper is your personal task management")
    print("  companion, designed to help you stay organised,")
    print("  manage your responsibilities and track your progress.")
    print(RESET)

    time.sleep(0.4)

    print(PURPLE + BOLD + "\n  ┌────────────────── AVAILABLE ACTIONS ──────────────────┐" + RESET)

    menu = [
        (CYAN, "01", "ADD TASK", "Create a new task"),
        (GREEN, "02", "VIEW TASKS", "View all your tasks"),
        (YELLOW, "03", "COMPLETE TASK", "Mark a task as completed"),
        (PURPLE, "04", "DELETE TASK", "Remove a task from your list"),
        (GREY, "05", "EXIT APPLICATION", "Close Task Keeper")
    ]

    for color, number, title, description in menu:
        print(f"  {color}{BOLD}  [{number}]  {title:<20}{RESET} {WHITE}{description}{RESET}")
        time.sleep(0.15)

    print(PURPLE + BOLD + "  └───────────────────────────────────────────────────────┘" + RESET)

    print(CYAN + "\n  " + "─" * 55 + RESET)

    print(GREEN + BOLD + "  Stay focused. Stay consistent. Keep achieving!" + RESET)

    print(CYAN + "  " + "─" * 55 + RESET)

    return input(YELLOW + BOLD + "\n  Choose an operation (1-5): " + RESET).strip()



# Terminal colours
CYAN = "\033[96m"
PURPLE = "\033[95m"
GREEN = "\033[92m"
WHITE = "\033[97m"
GREY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def goodbye():

    frames = [
        r"""
             ______________________
            |                      |
            |      TASK KEEPER     |
            |______________________|
                    |      |
                    |______|
                 ______________
                /_____________/
        """,

        r"""
                  O
                 /|\
                 / \
             __________________
            |                  |
            |    CLOSING...    |
            |__________________|
                 ______________
                /_____________/
        """,

        r"""
                  O
                 /|\
                 / \
             __________________
            |                  |
            |                  |
            |__________________|
                 ______________
                /_____________/
        """,

        r"""
                  O
                 /|\
                 / \
             __________________
            |                  |
            |      OFFLINE     |
            |__________________|
                 ______________
                /_____________/
        """
    ]

    # Animate computer shutdown
    for frame in frames:
        print("\033[2J\033[H", end="")
        print(CYAN + frame + RESET)
        time.sleep(0.7)

    print("\033[2J\033[H", end="")

    print(PURPLE + BOLD)
    print("  ╔══════════════════════════════════════════════╗")
    print("  ║                                              ║")
    print("  ║              TASK KEEPER v1.0                ║")
    print("  ║                                              ║")
    print("  ╚══════════════════════════════════════════════╝")
    print(RESET)

    print(CYAN + BOLD)
    print("       THANK YOU FOR USING TASK KEEPER!")
    print(RESET)

    print(WHITE + "\n       Closing your workspace safely..." + RESET)

    # Animated progress bar
    total = 30

    for i in range(total + 1):
        progress = int((i / total) * 100)
        bar = "█" * i + "░" * (total - i)

        sys.stdout.write(
            f"\r       {CYAN}[{bar}]{RESET} "
            f"{GREEN}{progress}%{RESET}"
        )
        sys.stdout.flush()
        time.sleep(0.06)

    print("\n")

    time.sleep(0.5)

    print(GREEN + BOLD)
    print("       ✓ All tasks safely preserved.")
    print("       ✓ Workspace closed successfully.")
    print(RESET)

    print(PURPLE + BOLD)
    print("\n       KEEP BUILDING. KEEP ACHIEVING.")
    print(RESET)

    print(GREY + "       Thank you. See you again!\n" + RESET)
