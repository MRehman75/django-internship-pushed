import csv
from datetime import datetime

def calculate_average(grade):
    return sum(grade.values()) /len(grade)

def highest_subject(gardes):
    subject= max(gardes, key=gardes.get)
    return subject, gardes[subject]

def lowest_subject(grades):
    subject= min(grades, key=grades.get)
    return subject, grades[subject]

def letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
    
def has_failed(grades):
    return any(marks < 50 for marks in grades.values())

def get_valid_grade(subject):
    while True:
        try:
            grades =float(input(f"Enter marks for {subject}:"))
            if 0 <= grades <= 100:
                return grades
            else:
                print("MARKS should between 0 -100.")
        except ValueError:
            print("invalid input: please enter valid input.")

def generate_report(student_name, grades):
    avg = calculate_average(grades)
    high_sub, high_marks = highest_subject(grades)
    low_sub, low_marks = lowest_subject(grades)
    grade = letter_grade(avg)
    
    report = []
    report.append("=" * 50)
    report.append(f"{'STUDENT REPORT CARD':^50}")
    report.append("=" * 50)
    report.append(f" Student Name : {student_name}")
    report.append("-" * 50)
    report.append(f"{'Subject':<25}{'Marks':>10}")
    report.append("-" * 50)
            
    for subject, mark in grades.items():
        report.append(f"{subject:<25}{mark:<10.2f}")
    
    report.append("-" * 50)
    report.append(f"{'Average:':<25}{avg:>10.2f}")
    report.append(f"{'Highest':<25}{high_sub}({high_marks:.2f})")
    report.append(f"{'Lowest':<25}{low_sub} ({low_marks:.2f})")
    report.append(f"{'Letter Grade':<25}{grade}")
    report.append("=" * 50)
    
    return "\n" .join(report),avg
students = []


filename= f"report_{datetime.now().strftime('%Y-%m-%d')}.txt"

with open(filename, "w") as file:
    while True:
        print("Enter Student Information")
        print("-" * 30)
        
        student_name=input("Student Name:").strip()
        
        grades={}
        
        for i in range(1,6):
            subject=input(f"Enter name of subject {i}").strip()
            grades[subject] = get_valid_grade(subject)
        report, average = generate_report(student_name, grades)
        
        print("\n")
        print(report)
        
        file.write(report + "\n\n")
        students.append({"name":student_name, "grades":grades,"average":average})
        
        choice = input("\nDo you want to enter another student? y/n").strip().lower()
        if choice !="y":
            break

print("\n")
print("=" * 60)
print(f"{'CLASS SUMMARY':^60}")
print("="* 60)

if students:
    class_average=sum(student["average"] for student in students) /len(students)
    top_students = max(students, key=lambda s: s["average"])
    
    failed_students =[student["name"] for student in students if has_failed(student["grades"])]
    
    print(f"Number of Students: {len(students)}")
    print(f"Class Average     : {class_average:.2f}")
    print(f"Top Students      : {top_students["name"]}({top_students['average']:.2f})")
    
    print("\n Students who Failed (any subject below 50): ")
    
    if failed_students:
        for name in failed_students:
            print(f"_{name}")
    else:
        print("None")
        
print("=" * 60)
print(f"\nReport Card EXported to:{filename}")


def export_to_csv(students, filename="student_report.csv"):
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["Name", "Marks", "Grade"])

            for student in students:
                writer.writerow([
                    student["name"],
                    student["marks"],
                    student["grade"]
                ])

        print(f"Student report exported to {filename}")

    except OSError as e:
        print(f"Error exporting report: {e}")


filename = input("Enter CSV filename (without extension): ").strip()

if not filename:
    filename = "student_report"

export_to_csv(students, f"{filename}.csv")
    


        