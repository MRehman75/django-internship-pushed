#ans q1:string(str)sstore text reallife examlpe is name of person.
#       integer(int) store whole number example: age of person
#       float(float) store decimal number example: height of person
#       boolean(true/false) store status example: is user is student?
#ans q2:The print() function displays output on the screen.
#      :The input() function asks the user for input and waits for them to type something.
#      :Regardless of what the user types, input() always returns a string (str).
#ans q3:A variable is a named container that stores data so you can use it later in your program.
#      :rule for named a variable
#      :R1.must start with letter or underscore
#      :R2.can contain letter number and underscore
#      :R3.hyphen are not allowed
#      :R4.can be case sensitive
#      :R5.no space, key words can not be a variable
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