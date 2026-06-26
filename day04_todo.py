#ans q13:
#       Both lists and tuples are used to store multiple values in Python, but they differ in an important way:
#       list is mute able can perform crud but slow & tuple not perform crud but faster.
#       we use tuple where we cant want to change like constant data and protect data and faster in performance.
#       return multiple value from function and use dictionry keys
#ans q14:
#        list.append add the item at the end of the e.g list fruits = ["apple", "banana"] fruits.append("orange") print(fruits)
#        list.insert add the item at specific position in list e.g fruits = ["apple", "banana"] fruits.insert(1, "orange") print(fruits)
#ans q15:
#        List comprehension is a short and powerful way to create a new list in a single line using a loop. syntax [expression for item in iterable]
#        result=[] for x in range (10) if x% 2==0 reslut.append(x) rewrite is following:    
#        result = [x for x in range(10) if x % 2 == 0]
#ans q16:
#        pop() removes and returns an element from a list.By default, it removes the last element.
#        If the list is empty, Python raises an error: IndexError: pop from empty list
tasks=[]
priority_order={"high":1,"medium":2,"low":3}

def add_tasks():
    title=input("enter the tasks title: ").strip()
    
    while True:
        priority=input("enter the priority of the task high,medium,low: ").strip().lower()
        if priority in priority_order:
            break
        print("invalid priority: please enter high medium or low")
       
    tasks.append({"Title":title,"status":"PENDING","priority":priority})
    print("task added successfully\n")
def view_tasks(filter_status=None):
    if not tasks:
        print("no task avalble.\n")
        return
    filtered=tasks
    if filter_status:
        filtered=[task for task in tasks if task ["status"]==filter_status]
    if not filtered:
        print("no match tasks \n")
        return
    sorted_tasks=sorted(filtered, key=lambda task: priority_order[task["priority"]])
    
    print("\n====TASKS LIST====")
    
    for index, task in enumerate(sorted_tasks, start=1):
        print(f"{index}. [{task['status']}] {task['priority'].upper()} {task['Title']}")
        print()
        
        
def mark_done():
    if not tasks:
        print("no task avalble \n")
        return
    view_tasks()
    try:
        number =int(input("enter task number to mark done. "))
        if 1 <=number <= len(tasks):
            tasks[number-1] ["status"]="DONE"
            print("task mark as done. \n")
        else:
            print("invalid tas number. \n")
            
    except ValueError:
        print("error: enter a valid number. \n")

def remove_task():
    if not tasks:
        print("no task avalible \n")
        return
    view_tasks()
    try:
        number =int(input("enter tasks number to remove. "))
        if 1 <= number <=len(tasks):
            removed =tasks.pop(number-1)
            print(f" Rmoved: {removed['Title']} \n")
        else:
            print("invalid task number \n")
            
            
    except ValueError:
        print("error: please enter valid number \n")
while True:
    print("============TO-DO LIST==============") 
    print("1. Add task")
    print("2. View all tasks")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. View pending tasks")
    print("6. View done tasks")
    print("7. Quit")
    choice=input("choose an option 1-7: ")
    if choice == "1":
        add_tasks()
    elif choice=="2":
        view_tasks()
    elif choice=="3":
        mark_done()
    elif choice=="4":
        remove_task()
    elif choice=="5":
        view_tasks("PENDING")
    elif choice =="6":
        view_tasks("DONE")
    elif choice=="7":
        total=len(tasks)
        done=sum(task["status"]==["done"] for task in tasks )
        pending=total-done
        
        print("\n======SUMMARY=====")
        print(f"Total tasks: {total}")
        print(f"done tasks: {done}")
        print(f"pending tasks {pending}")
        print("goodbye!")
        break
    else:
        print("invalid choice: please valid number of choice 1-7 \n")
        

              
         