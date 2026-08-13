import os

WIDTH = 70


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def top_border():
    print("=" * WIDTH)


def middle_border():
    print("-" * WIDTH)


def bottom_border():
    print("=" * WIDTH)


def empty_line():
    print(" " * WIDTH)


def show_header():
    print()
    top_border()
    print("🧮 SMART CALCULATOR".center(WIDTH))
    print("Simple • Fast • Reliable".center(WIDTH))
    bottom_border()


def show_menu():
    print()
    top_border()
    print("MAIN MENU".center(WIDTH))
    middle_border()
    empty_line()
    print("  [1]  ➕  Addition".ljust(WIDTH))
    print("  [2]  ➖  Subtraction".ljust(WIDTH))
    print("  [3]  ✖️  Multiplication".ljust(WIDTH))
    print("  [4]  ➗  Division".ljust(WIDTH))
    print("  [5]  📜  Calculation History".ljust(WIDTH))
    print("  [6]  🚪  Exit".ljust(WIDTH))
    empty_line()
    bottom_border()


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print()
            top_border()
            print("⚠️ INVALID INPUT".center(WIDTH))
            print("Please enter numbers only.".center(WIDTH))
            bottom_border()
            print()


def format_number(number):
    if number.is_integer():
        return int(number)
    return round(number, 4)


def show_result(calculation):
    print()
    top_border()
    print("✨ RESULT ✨".center(WIDTH))
    middle_border()
    empty_line()
    print(calculation.center(WIDTH))
    empty_line()
    bottom_border()
    print()
    print("✅ Calculation completed successfully!".center(WIDTH))
    print()


def show_history(history):
    print()
    top_border()
    print("📜 CALCULATION HISTORY".center(WIDTH))
    middle_border()

    if len(history) == 0:
        empty_line()
        print("No calculations yet.".center(WIDTH))
        empty_line()

    else:
        empty_line()

        for number, calculation in enumerate(history, start=1):
            text = f"{number}. {calculation}"

            if len(text) > WIDTH:
                text = text[:WIDTH]

            print(text.center(WIDTH))

        empty_line()

    bottom_border()


def calculator():

    history = []

    while True:

        clear_screen()

        show_header()
        show_menu()

        choice = input("\n👉 Enter your choice (1-6): ").strip()

        if choice == "6":

            clear_screen()

            print()
            top_border()
            print("👋 THANK YOU".center(WIDTH))
            print("FOR USING SMART CALCULATOR".center(WIDTH))
            bottom_border()
            print()

            break

        if choice == "5":

            clear_screen()

            show_header()
            show_history(history)

            input("\n↩ Press ENTER to return to menu...")
            continue

        if choice not in ["1", "2", "3", "4"]:

            print()
            top_border()
            print("❌ INVALID CHOICE".center(WIDTH))
            middle_border()
            print("Please select an option from 1 to 6.".center(WIDTH))
            bottom_border()

            input("\n↩ Press ENTER to continue...")
            continue

        print()
        top_border()
        print("🔢 ENTER NUMBERS".center(WIDTH))
        bottom_border()

        num1 = get_number("\n🔢 Enter first number  : ")
        num2 = get_number("🔢 Enter second number : ")

        if choice == "1":

            result = num1 + num2
            symbol = "+"

        elif choice == "2":

            result = num1 - num2
            symbol = "-"

        elif choice == "3":

            result = num1 * num2
            symbol = "×"

        else:

            if num2 == 0:

                print()
                top_border()
                print("⚠️ CALCULATION ERROR".center(WIDTH))
                middle_border()
                print("Division by zero is not allowed.".center(WIDTH))
                print("Please enter a non-zero number.".center(WIDTH))
                bottom_border()

                input("\n↩ Press ENTER to continue...")
                continue

            result = num1 / num2
            symbol = "÷"

        result = format_number(result)

        calculation = (
            f"{format_number(num1)} {symbol} "
            f"{format_number(num2)} = {result}"
        )

        history.append(calculation)

        show_result(calculation)

        input("↩ Press ENTER to continue...")


if __name__ == "__main__":
    calculator()