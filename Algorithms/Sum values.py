def sum_values():
    user_input = input("Enter a number or a blank line to exit: ")
    if user_input == "":
        return 0.0
    return float(user_input) + sum_values()


print("Total sum", sum_values())
