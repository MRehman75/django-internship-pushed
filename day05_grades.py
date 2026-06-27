#ans q17:
#       both dict['key'] and dict.get('key') are used to retrieve values from a dictionary, but they behave differently when the key doesn't exist.
#       dict['key'] Raises a KeyError if the key is not present
#       dict.get('key') Does not raise a KeyError for a missing key. It returns None or the default value you provide.
#ans q18:
#        The most common and Pythonic way to loop through both keys and values of a dictionary at the same time is to use the .items() method.
#        for key, value in student.items():
#ans q19:
#        A set is a built-in Python data type used to store a collection of unique items. Sets are useful when you want to remove duplicates or 
#        perform mathematical set operations like union and intersection.
#        1. Sets Do Not Allow Duplicate Elements 2. Sets Are Unordered 3. Sets Do Not Support Indexing
#ans q20:
#       List:	Checks if a value is in the list. Dictionary:	Checks if a key is in the dictionary.
#       
students ={}

def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else :
        return "F"
    
def add_students():
    name =input("enter student name : ").strip()
    
    if name in students:
        print("name already exict !")
        return 
    email =input("enter email : ").strip()
    
    students[name]={"grades":[],"subjects":[],"email": email}
    print("student add successfully \n")

def add_grade():
    name=input("enter student name : ").strip() 
    if name not in students:
        print("student not fonud \n")
        return
    subject=input("enter subject: ").strip()
    
    while True:
        try:
            grade = float(input("Enter grade (0-100): "))

            if 0 <= grade <= 100:
                students[name]["subjects"].append(subject)
                students[name]["grades"].append(grade)
                print("Grade added successfully.\n")
                break
            else:
                print("Grade should be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")
        
        
def view_students():
    if not students:
        print("no student found")
        return
    print("\n ======STUDENTS=======")
    
    for name, info in students.items():
        if info["grades"]:
            avg=round(sum(info["gardes"]) / len(info["grades"],2))
            letter=get_letter_grade(avg)
        else:
            avg=0
            letter="N/A"
        print(f"Name: {name}")
        print(f"Email: {info['email']}")
        print(f"Subjects: {info['subjects']}")
        print(f"Grades: {info['grades']}")
        print(f"Average: {avg}")
        print(f"Letter: {letter}")
        print("-"*30) 
def top_students():
    if not students:
        print("no student found \n") 
        return
    best_name=None
    best_avg=-1
    
    for name, info in students.items():
        if info["grades"]:
            avg = sum(info["grades"]) / len(info["grades"])
            
            if avg>best_avg:
                best_avg=avg
                best_name=name
    if best_name:
        print("\n ======TOP STUDENTS======")
        print(f"Name: {best_name}")
        print(f"Average: {round(best_avg,2)}")
        print(f"letter grade: {get_letter_grade(best_avg)}\n")
    else:
        print("no garde found\n")
def below_threshold():
    if not students:
        print("no student found.")
        return
    while True:
        try:
            threshold=float(input("enter a threshold: "))
            break
        except ValueError:
            print("please enter a valid number.\n")
    found=False
    
    print("\n student below the threshold.")
    
    for name, info in students.items():
        if info["grades"]:
            avg = sum(info["grades"]) / len(info["grades"]) 
            if avg<threshold:
                found=True
                print(f"{name} -> {round(avg,2)}")
        if not found:
            print("no student found below threshold.")
        print()
def grade_distribution():
    unique_grade=set()
    for info in students.values():
        unique_grade.update(info["grades"])
    if unique_grade:
        print("\n unique grade Awarde")
        print(sorted(unique_grade))
    else:
        print("No grade avalible.")
    print()
while True:
        print("========== GRADE TRACKER ==========")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Students")
        print("4. Find Top Student")
        print("5. Students Below Threshold")
        print("6. Grade Distribution")
        print("7. Exit")  
        
        choice=input("enter your choice 1-7: ")  
        
        if choice=="1":
            add_students()
        elif choice=="2":
            add_grade()
        elif choice=="3":
            view_students()
        elif choice=="4":
            top_students()
        elif choice=="5":
            below_threshold()
        elif choice=="6":
            grade_distribution()
        elif choice=="7":
            break
        else:
            print("invalid choice.\n")
    
            
            
                                  
            