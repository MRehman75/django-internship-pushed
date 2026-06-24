#ans q5:
#     / = regular division → gives the exact quotient (including decimals).
#     // = floor division → gives the quotient rounded down to the nearest whole number.
#     For 17 divided by 5:
#      output:
#      17 / 5 = 3.4
#      17 // 5 = 3
#ans q6:
#      The % operator is called the modulus (or modulo) operator.
#       It returns the remainder after division. use case is checking a number is even or odd.
#       Example:
#       17 % 5
#       output:
#       2
#ans q7:
#       while asking any number from user input() take it as string
#       to do arthimatic we have to convetr in int or float type
#        error : TypeError: can only concatenate str (not "int") to str
#ans q8:
#      Comparison operators compare two values and return either True or False.
#      == equal to =! not equal to > greater then < less then >= greater then equak to <= less then equal to
#      age =18 print(age >=18) output:  true

while True:

    mode = input("choose mode normal/advanced: ").lower()

    while True:
        try:
            num1 = float(input("enter first number : "))
            break
        except ValueError:
            print("errorMessage= enter a valid number please")

    while True:
        try:
            num2 = float(input("enter the second number : "))
            break
        except ValueError:
            print("error= please enter a valid number")

    # ================= NORMAL MODE =================
    if mode == "normal":

        operator = input("enter an operator + - * / // % ** : ")

        if operator == "+":
            print("Result: ", num1 + num2)

        elif operator == "-":
            print("Result: ", num1 - num2)

        elif operator == "*":
            print("Result: ", num1 * num2)

        elif operator == "/":
            if num2 == 0:
                print("number cannot divide by zero")
            else:
                print("Result: ", num1 / num2)

        elif operator == "//":
            if num2 == 0:
                print("number cannot divide by zero")
            else:
                print("Result: ", num1 // num2)

        elif operator == "%":
            if num2 == 0:
                print("number cannot divide by zero")
            else:
                print("Reminder: ", num1 % num2)

        elif operator == "**":
            print("Result: ", num1 ** num2)

        else:
            print("invalid operator")

        

    # ================= ADVANCED MODE =================
    elif mode == "advanced":

        print("\n======== ADVANCED ========")
        print(f"{num1} + {num2} = {num1 + num2}")
        print(f"{num1} - {num2} = {num1 - num2}")
        print(f"{num1} * {num2} = {num1 * num2}")

        if num2 == 0:
            print(f"{num1} / {num2} = Error (divide by zero)")
            print(f"{num1} // {num2} = Error (divide by zero)")
            print(f"{num1} % {num2} = Error (divide by zero)")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
            print(f"{num1} // {num2} = {num1 // num2}")
            print(f"{num1} % {num2} = {num1 % num2}")

        print(f"{num1} ** {num2} = {num1 ** num2}")
        # BONUS for advanced mode
        print("\n===== BONUS +2 PTS =====")
        print("Advanced calculator shows all operations at once ✔")
        print("Handles divide-by-zero safely ✔")

    else:
        print("invalid mode selected")

    again = input("\nDo you want to calculate again? (yes/no): ").lower()

    if again != "yes":
        print("good bye!")
        break