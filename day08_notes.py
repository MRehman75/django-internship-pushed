#ans q30:
#        These file modes are commonly used with functions like open() in Python (and are similar in many other languages):
#        'r' (Read) Opens an existing file for reading. if file not exict crash
#        'w' (Write) Opens a file for writing. create file if not exict and if already exict then delete exicting data.
#        'a' (Append) Opens a file for writing at the end. create file if not exict if file already exict then exicting data preserved  new data add at end of file.
#        'r+' (Read and Write. Opens an existing file for both reading and writing. file must exict  and not delete exictig data in file.
#ans q31:
#        The with statement is used to automatically manage resources such as files. When you open a file with with, Python ensures the file is closed automatically,
#        even if an error occurs while processing it. with out "with" there is no surity to close file user have to put file.close() to close file.
#ans q32:
#        JSON (JavaScript Object Notation) is a lightweight, text-based format for storing and exchanging structured data. Although it originated from JavaScript,
#        it is language-independent and is supported by virtually all modern programming languages, including Python.
#        Plain text is just unstructured characters. The program has to interpret what each line or value means.
#ans q33:
#        Python's try, except, else, and finally blocks are used for exception handling, allowing your program to respond gracefully to errors instead of crashing.
#        try: Contains code that may raise an exception.
#        except: Handles specific exceptions if they occur.
#        else: Runs only when the try block completes without any exceptions.
#        finally: Runs regardless of whether an exception occurred, making it ideal for cleanup operations such as closing files or releasing resources.
import json
from datetime import datetime

FILENAME ="notes.json"
def load_notes():
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except(json.JSONDecodeError, OSError):
        print("Warning: could not read note file. starting with an empty note list.")
        return []
def save_notes(notes):
    try:
        with open(FILENAME, 'w') as file:
            return json.dump(notes, file, indent=4)
    except OSError:
        print("Error: unable to save file.")
        
def add_notes(notes):
    title = input("Enter Title: ").strip()
    body = input("Enter body of file: ").strip()
    
    if not title:
        print("Title should not be empty.")
        return
    
    note = {"title":title, "body":body, "created_at":datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "updated_at":None}
    notes.append(note)
    print("Notes Add Successfully.")
    
def view_notes(notes):
     if not notes:
         print("NOT found any notes")
         return
     print("\n=======Notes=========")
     for i, note in enumerate(notes, start=1):
         print(f"{i}. {note['title']}")    
         print(f" Created: {note['created_at']}")
         if note['updated_at']:
             print("    Updated: {note['updated_at']}")
         print()

def view_singal_note(notes):
    if not notes:
        print("No notes avalible.")
        return
    try:
        number = int(input("Enter number of note: "))
        if number < 1 or number > len(notes):
            print("Invalid note number.")
            return
        note = notes[number - 1]
        
        print("\n------------------------------")
        print("Title:", note["title"])
        print("Created:", note["created_at"])
        
        if note["updated_at"]:
            print("Updated_at:", note["updated_at"])
        
        print("\nBody:")
        print(note["body"])
        print("--------------------------------")
    except ValueError:
        print("please enter a valid number.")

def search_notes(notes):
    if not notes:
        print("No notes avalible.")
        return
    keyword = input("Enter keyword:").lower()
    
    found= False
    for i, note in enumerate(notes, start=1):
        if (keyword in note["title"].lower() or keyword in note["body"].lower()):
            print(f"\n{i}. {note["title"]}")
            print(note["body"])
            found = True
            
    if not found:
        print("No matched notes found.")

def delete_notes(notes):
    if not notes:
        print("No notes avilable.")
        return
    try:
        number = int(input("Enter notes Number to delete: "))
        
        if number < 1 or number > len(notes):
            print("Invalid notes number.")
            return
        deleted = notes.pop(number - 1)
        print(f" Deleted: ", deleted["title"])
    except ValueError:
        print("please enter a valid number.")
        
def edit_notes(notes):
    if not notes:
        print("no notes avilable.")
        return
    try:
        number = int(input("Enter notes number you want to edit: "))
        
        if number < 1 or number > len(notes):
            print("please enter a valid number.")
            return
        note = notes[number - 1]
        
        print(f"Current Title: {note['title']}")
        new_title = input("New title (leave blank to keep)").strip()
        
        print(f"Current body: {note['body']}")
        new_body = input("New body (leave blank to keep)").strip()
        
        if new_title:
            note["title"] = new_title
        if new_body:
            note["body"] = new_body
            
        note["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Note updated.")
    except ValueError:
        print("enter a valid number.")
        
def main():
    notes = load_notes()
    
    while True:
        print("\n============NOTES APP==================")
        print("1. Add note")
        print("2. View all notes")
        print("3. View a single note")
        print("4. Search notes")
        print("5. Delete note")
        print("6. Edit note (Bonus)")
        print("7. Save and Exit")
        
        chioce = input("Choose an option.")
        if chioce == "1":
             add_notes(notes)
        elif chioce == "2":
            view_notes(notes)
        elif chioce == "3":
            view_singal_note(notes)
        elif chioce == "4":
            search_notes(notes)
        elif chioce == "5":
            delete_notes(notes)
        elif chioce == "6":
            edit_notes(notes)
        elif chioce == "7":
            save_notes(notes)
            print("Notes saved.")
            print("Good Bye!")
            break
        else:
            print("invalid option try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n Program Inerrupted.")
        
         
        
        
        