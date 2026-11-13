import time
from contextlib import contextmanager

from rich import box
from rich.console import Console
from rich.markup import escape
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich.table import Table


console = Console(highlight=False)
err_console = Console(stderr=True, highlight=False)

CATEGORY_COLORS = {
    'Food': 'green',
    'Transportation': 'yellow',
    'Utilities': 'cyan',
    'Education': 'blue',
    'Healthcare': 'red',
    'Entertainment': 'magenta',
    'Others': 'white',
}


# ---------- messages ----------

def success(message):
    console.print(f'[bold green]✔[/bold green] [green]{escape(message)}[/green]')


def error(message):
    err_console.print(f'[bold red]error:[/bold red] [red]{escape(message)}[/red]')


def warning(message):
    console.print(f'[yellow]{escape(message)}[/yellow]')


def info(message):
    console.print(f'[cyan]{escape(message)}[/cyan]')


# ---------- interaction ----------

def ask(prompt):
    return console.input(f'[bold cyan]{escape(prompt)}[/bold cyan] ').strip()


def confirm(prompt):
    answer = ask(f'{prompt} (y/n):').lower()
    return answer == 'y'


def pause():
    if console.is_terminal:
        console.input('[dim]Press Enter to continue...[/dim]')


def clear():
    if console.is_terminal:
        console.clear()


# ---------- animation (skipped automatically when not in a real terminal) ----------

def typewriter(text, style='bold magenta', delay=0.03):
    if not console.is_terminal:
        console.print(text, style=style)
        return
    for char in text:
        console.print(char, end='', style=style, markup=False)
        time.sleep(delay)
    console.print()


@contextmanager
def spinner(message):
    if not console.is_terminal:
        yield
        return
    with console.status(f'[cyan]{escape(message)}[/cyan]', spinner='dots'):
        yield
        time.sleep(0.6)


def progress(label='Working'):
    if not console.is_terminal:
        return
    with Progress(
        TextColumn('[cyan]{task.description}'),
        BarColumn(),
        TextColumn('{task.percentage:>3.0f}%'),
        console=console,
        transient=True,
    ) as bar:
        task = bar.add_task(label, total=20)
        for _ in range(20):
            time.sleep(0.03)
            bar.advance(task)


# ---------- displays ----------

def banner():
    clear()
    typewriter('💰  EXPENSE TRACKER', style='bold magenta')
    console.rule(style='magenta')


def menu(title, items):
    table = Table(
        title=title,
        title_style='bold magenta',
        box=box.ROUNDED,
        border_style='bright_blue',
        show_header=False,
    )
    table.add_column(justify='right', style='bold yellow')
    table.add_column(style='white')
    for key, label in items:
        table.add_row(key, label)
    console.print(table)


def expense_table(expences, title='Expenses'):
    table = Table(
        title=title,
        title_style='bold magenta',
        header_style='bold cyan',
        box=box.ROUNDED,
        border_style='bright_blue',
    )
    table.add_column('No.', justify='right', style='dim')
    table.add_column('Date', style='green')
    table.add_column('Category')
    table.add_column('Description')
    table.add_column('Amount', justify='right', style='bold yellow')

    for index, expence in enumerate(expences, 1):
        color = CATEGORY_COLORS.get(expence['category'], 'white')
        table.add_row(
            str(index),
            expence['date'],
            f"[{color}]{expence['category']}[/{color}]",
            escape(expence['description']),
            f"{expence['amount']:,.2f}",
        )
    console.print(table)


def report_panel(title, rows):
    grid = Table.grid(padding=(0, 2))
    grid.add_column(style='cyan')
    grid.add_column(justify='right', style='bold white')
    for label, value in rows:
        grid.add_row(label, escape(str(value)))
    console.print(
        Panel(grid, title=f'[bold magenta]{escape(title)}[/bold magenta]',
              border_style='magenta', width=50)
    )


def table_report(title, columns, rows):
    table = Table(
        title=title,
        title_style='bold magenta',
        header_style='bold cyan',
        box=box.ROUNDED,
        border_style='bright_blue',
    )
    table.add_column(columns[0])
    for name in columns[1:]:
        table.add_column(name, justify='right')
    for row in rows:
        table.add_row(*row)
    console.print(table)