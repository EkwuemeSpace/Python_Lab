import sys
import time

from storage import load_task, save_task, update_task_status, delete_task, file_path

# ---------- colors ----------
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'


# ---------- animations ----------
def typewriter(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def spinner(message, duration=0.8):
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        frame = frames[i % len(frames)]
        sys.stdout.write(f'\r{CYAN}{frame}{RESET} {message}')
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write('\r' + ' ' * (len(message) + 4) + '\r')
    sys.stdout.flush()


def loading_bar(label, width=30, delay=0.02):
    for step in range(width + 1):
        filled = '█' * step
        empty = '░' * (width - step)
        percent = int(step / width * 100)
        sys.stdout.write(f'\r{MAGENTA}{label}{RESET} {GREEN}{filled}{DIM}{empty}{RESET} {percent}%')
        sys.stdout.flush()
        time.sleep(delay)
    print()


# ---------- display ----------
def show_banner():
    print(f'{CYAN}{BOLD}╔══════════════════════════════════╗{RESET}')
    print(f'{CYAN}{BOLD}║{RESET}      {YELLOW}{BOLD}✦  TASK KEEPER  ✦{RESET}          {CYAN}{BOLD}║{RESET}')
    print(f'{CYAN}{BOLD}╚══════════════════════════════════╝{RESET}')


def show_menu():
    print()
    print(f'{BOLD}What would you like to do?{RESET}')
    print(f'  {GREEN}1{RESET}  Add task')
    print(f'  {BLUE}2{RESET}  View tasks')
    print(f'  {YELLOW}3{RESET}  Complete task')
    print(f'  {RED}4{RESET}  Delete task')
    print(f'  {MAGENTA}5{RESET}  Quit')
    print()


def show_tasks(tasks):
    if not tasks:
        print(f'{YELLOW}No tasks to view at the moment.{RESET}')
        return

    print()
    print(f'{BOLD}{CYAN}  ID   STATUS      TITLE{RESET}')
    print(f'{DIM}  ─────────────────────────────────{RESET}')

    done_count = 0
    for task in tasks:
        if task['completed']:
            status = f'{GREEN}✔ done    {RESET}'
            title = f"{DIM}{task['title']}{RESET}"
            done_count += 1
        else:
            status = f'{YELLOW}○ pending {RESET}'
            title = task['title']
        print(f"  {task['id']:<4} {status}  {title}")

    print(f'{DIM}  ─────────────────────────────────{RESET}')
    print(f'  {GREEN}{done_count}{RESET} done / {len(tasks)} total')


# ---------- main loop ----------
def main():
    loading_bar('Starting')
    print()
    show_banner()

    while True:
        show_menu()
        choice = input(f'{BOLD}Enter a number: {RESET}').strip()

        if choice == '1':
            save_task(file_path)

        elif choice == '2':
            spinner('Loading tasks...')
            show_tasks(load_task(file_path))

        elif choice == '3':
            update_task_status(file_path)

        elif choice == '4':
            delete_task(file_path)

        elif choice == '5':
            typewriter(f'{MAGENTA}Goodbye, keep building!{RESET}')
            break

        else:
            print(f'{RED}Invalid choice, enter 1 to 5.{RESET}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{MAGENTA}Goodbye!{RESET}')