import os

HISTORY_FILE = os.path.join(os.path.dirname(__file__), "history.txt")

def ensure_history_exists():
    open(HISTORY_FILE, "a").close()

def show_history():
    ensure_history_exists()
    with open(HISTORY_FILE, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    if not lines:
        print("no history to show")
    else:
        for line in reversed(lines):
            print(line)

def clear_history():
    open(HISTORY_FILE, "w").close()
    print("history cleared successfully")

def save_to_history(equation, result):
    ensure_history_exists()
    with open(HISTORY_FILE, "a") as f:
        f.write(f"{equation} = {result}\n")

def calculator(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("invalid input format. please use: number1 operator number2")
        return

    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("invalid numbers")
        return

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("error: division by zero is not allowed")
            return
        result = num1 / num2
    else:
        print("error: unsupported operator")
        return

    if isinstance(result, float) and result.is_integer():
        result = int(result)

    print("result:", result)
    save_to_history(user_input, result)

def main():
    print("welcome to calculator")
    while True:
        user_input = input("enter calculation (or type 'history', 'clear', 'exit'): ").strip()
        if user_input.lower() == 'exit':
            print('good bye')
            break
        elif user_input.lower() == 'history':
            show_history()
        elif user_input.lower() == 'clear':
            clear_history()
        else:
            calculator(user_input)

if __name__ == "__main__":
    main()