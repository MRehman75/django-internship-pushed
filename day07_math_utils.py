#ans q25:
#        A parameter and an argument are related, but they are used at different times.
#        Parameter: A variable listed in a function's definition. It acts as a placeholder for the value the function will receive.
#        Argument: The actual value you pass to the function when you call it.
#ans q26:
#        The return statement is used to send a value back from a function to the place where the function was called. It also ends the function immediately, 
#        so any code after return is not executed.
#        If a function does not have a return statement, Python automatically returns None.
#ans q27:
#        *args:Used to pass a variable number of positional arguments.Inside the function, it behaves like a tuple
#       **kwargs: Used to pass a variable number of keyword arguments.Inside the function, it behaves like a dictionary
#ans q28:
#        Variable scope defines where a variable can be accessed in a program.
#        A local variable is created inside a function and can only be used within that function.
#       A global variable is created outside all functions and can be used anywhere in the program.
#ans q29:
#       Review of week one : day 02 was hardest because the operator and their calculation and testing the logic is working correctly other wise overall going perfectly
#       and very intrestingly like guessing game and grade traker was very intresting. thanks to our senior software engineer to found me capable for this. thank you!
import math
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) +1, 2):
        if n % i == 0:
            return False
    return True
def factorial(n):
    if n < 0 :
        return "invalid input"
    result = 1
    for i in range(1, n):
        result *= i
    return result
def fibonacci(n):
    if n <= 0:
        return []
    sequence =[0,1]
    if n == 1:
        return [0]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
    
def is_palindrome(text):
    cleaned= text.replace(" ","").lower()
    return cleaned == cleaned[::-1]

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f-32) * 5/9

def bmi_calculate(weight_kg,height_m):
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        categore = "Under_weight"
    elif bmi < 25:
        categore = "Normal"
    elif bmi < 30:
        categore = "Over_weight"
    else:
        categore = "Obese"
    return bmi, categore
while True:
    print("\n ================MATH UTILITIES MENU===================")
    print("1. Prime check.")
    print("2.Factorial ")
    print("3. Fibonacci ")
    print("4. Palindrome Check")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to celsius")
    print("7. BMI Calculator")
    print("0. Exit")
    
    choice=input("enter your choice: ")
    if choice =="1":
       n =int( input("Enter Number: "))
       print(" Prime : ", is_prime(n))
    elif choice =="2":
        n=int(input("Enter Number: "))
        print("Factorial: ",factorial(n))
    elif choice=="3":
        n=int(input("Enter how many terms: "))
        print("Fibonacci: ", fibonacci(n))
    elif choice =="4":
        n=input("Enter text: ")
        print("Palindrome : ", is_palindrome(n))
    elif choice == "5":
        n= float(input("enter temp in celsius: "))
        print("Celsius to Fahrenheit :",celsius_to_fahrenheit(n))
    elif choice == "6":
        n=float(input("enter temp in fahernheit: "))
        print("Fahrenheit to celsius: ",fahrenheit_to_celsius(n))
    elif choice == "7":
        w=float(input("enter weight in kg"))
        h=float(input("enter height in m"))
        bmi,categore=bmi_calculate(w,h)
        print(f" BMI: {bmi:.2f}, Category: {categore}")
    elif choice=="0":
        print("Exit Pro...")
        break
    else:
        print("invalid choice: try again")