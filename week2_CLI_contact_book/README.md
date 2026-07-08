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
<img width="1209" height="600" alt="image" src="https://github.com/user-attachments/assets/cf671ae2-bac4-4d7f-bf9c-ea83c1f2f307" />
<img width="1254" height="602" alt="image" src="https://github.com/user-attachments/assets/85fa7a4c-b303-4fed-9b81-af970ca8f870" />
<img width="1232" height="590" alt="image" src="https://github.com/user-attachments/assets/4085a222-b57d-467b-8bcd-571ca82fc0e6" />
<img width="1218" height="555" alt="image" src="https://github.com/user-attachments/assets/2fd94637-2472-49de-89a7-07709627c9dd" />
<img width="1238" height="583" alt="image" src="https://github.com/user-attachments/assets/9d767e7b-d218-4f3a-8175-676ef17be441" />
<img width="1203" height="544" alt="image" src="https://github.com/user-attachments/assets/1b8c6d65-0e89-4af1-974f-d7fc20c9f40c" />
<img width="940" height="463" alt="image" src="https://github.com/user-attachments/assets/2b586d29-f396-4acb-b6cb-47b2df57f4b5" />
<img width="1193" height="609" alt="image" src="https://github.com/user-attachments/assets/ace0d83d-b998-40a7-8673-428ef5a68cc7" />








