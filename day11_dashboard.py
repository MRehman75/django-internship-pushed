#ans q38:
#       A Python module is a file containing Python code (functions, classes, variables, or executable statements) that you can reuse in other Python programs.
#      Modules help organize code and avoid rewriting common functionality.
#      1. import math :This imports the entire module. You access its functions and constants using the module name.
#      2. from math import sqrt :This imports only the sqrt function directly into your program's namespace.
#ans q39:
#        math : Provides mathematical functions and constants.
#       random : Generates random numbers and makes random selections.
#      datetime : Works with dates and times. 
#      os : Interacts with the operating system.
#       json : Reads and writes JSON data.
#ans q40:
#        os.path.join() is a function in the os.path module that combines directory and file names into a valid file path.
#        String concatenation can easily produce incorrect paths
#ans q41:
#        The collections.Counter class is a dictionary-like class from Python's collections module that counts 
#         how many times each item appears in an iterable (such as a list, string, or tuple).
#         from collections import Counter
#         words = ["apple", "banana", "apple", "orange", "banana", "apple"]
#         counts = Counter(words)
#         print(counts)
#        Counter({'apple': 3, 'banana': 2, 'orange': 1})
from datetime import datetime, date
import os
import random
import string
import collections
import re
import platform
import getpass

print("=" * 60)
print("DEVELOPER DASHBOARD")
print("=" * 60)

print("\nSECTION 1 - TIME")

now = datetime.now()

print("Current Date:", now.strftime("%Y-%m-%d"))
print("Current Time:", now.strftime("%H:%M:%S"))
print("Day of Week:", now.strftime("%A"))
print("Week Number:", now.strftime("%U"))

birthday = input("Enter your next birthday (MM-DD): ")

try:
    month, day = map(int, birthday.split("-"))
    today = date.today()
    next_birthday = date(today.year, month, day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, month, day)
    print("Days until next birthday:", (next_birthday - today).days)
except:
    print("Invalid birthday format.")

past = input("Enter any past date (YYYY-MM-DD): ")

try:
    past_date = datetime.strptime(past, "%Y-%m-%d").date()
    print("Days since that date:", (date.today() - past_date).days)
except:
    print("Invalid date format.")

print("\nSECTION 2 - FILE SYSTEM")

entries = os.listdir(".")
py_total = 0
latest_file = None
latest_time = 0

for item in entries:
    if os.path.isfile(item):
        size = os.path.getsize(item) / 1024
        print(f"{item:<35} {size:.2f} KB")

        if item.endswith(".py"):
            py_total += os.path.getsize(item)

        modified = os.path.getmtime(item)
        if modified > latest_time:
            latest_time = modified
            latest_file = item

print(f"\nTotal size of .py files: {py_total / 1024:.2f} KB")

if latest_file:
    print("Most recently modified file:", latest_file)

print("\nSECTION 3 - PASSWORD GENERATOR")

while True:
    length = int(input("Password length (minimum 8): "))
    if length >= 8:
        break

upper = random.choice(string.ascii_uppercase)
lower = random.choice(string.ascii_lowercase)
digit = random.choice(string.digits)
symbol = random.choice(string.punctuation)

remaining = random.choices(
    string.ascii_letters + string.digits + string.punctuation,
    k=length - 4,
)

password_list = [upper, lower, digit, symbol] + remaining
random.shuffle(password_list)
password = "".join(password_list)

score = 0

if length >= 8:
    score += 1
if length >= 12:
    score += 1
if any(c.isupper() for c in password):
    score += 1
if any(c.islower() for c in password):
    score += 1
if any(c.isdigit() for c in password):
    score += 1
if any(c in string.punctuation for c in password):
    score += 1

if score <= 3:
    strength = "Weak"
elif score <= 5:
    strength = "Medium"
else:
    strength = "Strong"

print("Generated Password:", password)
print("Strength:", strength)

print("\nSECTION 4 - TEXT STATISTICS")

text = input("Paste text:\n")

words = re.findall(r"\b\w+\b", text.lower())
sentences = len(re.findall(r"[.!?]+", text))

avg_length = sum(len(word) for word in words) / len(words) if words else 0

ignore = {
    "the", "a", "an", "is", "of", "to", "in", "on",
    "at", "for", "and", "or", "it", "be", "as",
    "by", "with", "this", "that"
}

filtered = [w for w in words if len(w) > 2 and w not in ignore]

if filtered:
    common = collections.Counter(filtered).most_common(1)[0][0]
else:
    common = "None"

print("Word Count:", len(words))
print("Sentence Count:", sentences)
print("Average Word Length:", round(avg_length, 2))
print("Most Common Word:", common)

print("\nSECTION 5 - SYSTEM INFO")

print("OS:", platform.system())
print("Python Version:", platform.python_version())
print("Username:", getpass.getuser())
print("Home Directory:", os.path.expanduser("~"))
print("=" * 60)