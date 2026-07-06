# Contact Book CLI Application

## Overview

This project is a professional Command Line Interface (CLI) Contact Book application developed in Python using Object-Oriented Programming (OOP). The application allows users to manage contacts efficiently with persistent storage using JSON files and export data to CSV.

---

## Features

* Add a new contact
* View all contacts
* View a single contact
* Edit existing contacts
* Delete contacts
* Search by:

  * Name
  * Phone Number
  * Email
  * Tags
* Birthday reminders

  * Birthdays this month
  * Birthdays in the next 7 days
* Automatic JSON data loading on startup
* Automatic JSON saving on exit
* Export contacts to CSV
* Input validation
* Exception handling to prevent crashes

---

## Technologies Used

* Python 3.x
* Object-Oriented Programming
* JSON
* CSV
* Regular Expressions
* Datetime Module

---

## Project Structure

```
contact_book/
│
├── main.py
├── contact.py
├── contact_book.py
├── storage.py
├── utils.py
├── contacts.json
├── contacts_export.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How to Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Requirements

This project uses only Python's standard library.

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python main.py
```

---

## Menu Options

```
1. Add Contact
2. View All Contacts
3. View Contact
4. Edit Contact
5. Delete Contact
6. Search Contact
7. Birthdays This Month
8. Birthdays Next 7 Days
9. Export to CSV
0. Exit
```

---

## Data Storage

Contacts are automatically stored in:

```
contacts.json
```

The file is loaded automatically when the application starts and saved automatically when it exits.

---

## CSV Export

Select **Export to CSV** from the menu.

The application creates:

```
contacts_export.csv
```

---

## Error Handling

The application safely handles:

* Invalid phone numbers
* Invalid email addresses
* Invalid birthday format
* Missing files
* Invalid JSON files
* Invalid menu choices
* Unexpected user input

The program is designed to continue running without crashing.

---

## Author

Python Contact Book CLI Project
