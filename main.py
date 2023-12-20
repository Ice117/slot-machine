import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|")
            else:
                print(column[row])

def deposit():
    while True:
        amount = input("Quando você gostaria de depositar ? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("A quantia precisa ser maior que 0")
        else:
            print("Digite um numero")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Quantas apostas gostaria de fazer ? (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Selecione um numero de 1 a 3")
        else:
            print("Digite um numero")

    return lines

def get_bet():
    while True:
        bet = input("Quando você gostaria de apostar ? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"A quantia precisa ser entre ${MIN_BET} - ${MAX_BET}")
        else:
            print("Digite um numero")

    return bet

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("Voce não tem saldo o suficiente")
        else:
            break


    print(f"Você apostou {bet} em {lines} linhas. total da aposta: ${total_bet}")

main()