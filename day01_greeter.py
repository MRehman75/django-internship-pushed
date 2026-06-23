full_name = input("enter your full name please")
age =int(input("enter your age"))
internship_goal = input("what are your internship goals")
print("n\"----Internship Profile----")
print(f"Name:{full_name}")
print(f"Age:{age}")
print(f"Goals For Internship:{internship_goal}")

name=input("enter your full name:  ")
age=int(input("enter your age : "))
height=float(input("enter your height in feet eg; 5.1: "))
student=input("are you student? yes/no: ").lower()=="yes"
name_upper=name.upper()
months_old=age*12
student_status="yes" if student else "No"

print("\n" + "=" *40)
print("             WELLCOME       ")
print("="*40)
print(f"Name      :{name_upper}")
print(f"Age years :{age}")
print(f"Age months:{months_old}")
print(f"Height    :{height}ft")
print(f"Student   :{student_status}")
print("="*40)
print("    Thank you for using the system!")
print("="*40)