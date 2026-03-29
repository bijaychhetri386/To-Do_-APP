try:
    with open("tasks.txt","r") as f:
        tasks= f.read().splitlines()
        
except FileNotFoundError:
    tasks=[]

def save_task():
    with open("tasks.txt","w") as f:
        for task in tasks:
            f.write(task +"\n")

def view_task():
    print("\n"+"-" *90)
    if not tasks:
        print("Please add tasks first! ")
    else:
        print("\n Your remaining tasks are:")
        for i,task in enumerate(tasks,1):
            print(f"{i}. {task}")
    print("-"*90)

def add_task():
    task=input("Enter a task you want to add:")
    if task.strip()=="":
        print("Task cannot be empty")
    else:
        tasks.append(task)
        print(f"Added:{task} ")

def delect_task():

    view_task()

    try:
        num=int(input("Enter the task number to delect:"))
        
        if 1<=num <=len(tasks):
            deleted=tasks.pop(num-1)
            print(f"Deleted:{deleted}")

            print("\n Updated Tasks:")
            view_task()
    except ValueError:
        print("Please Enter A Valid Number:")
print("\n" +"="*90)


print("\n            Welcome to your to do app list\n This app make sure you donot forget your remaining task!")

print("=" *90)
while True:
    print("\n" + "-" *90)
    print("   Operations        " )
    print("\n1 . View tasks")
    print("2 . Add a task")
    print("3 . Remove your completed task")
    print("4 . Save and Exit the app")
    print("-" *90 )
    choice=input("Enter your choice please!")
    if choice=="1":
        view_task()

    elif choice =="2":
        add_task()

    elif choice=="3":
        delect_task()

    elif choice=="4":
        save_task()
        print("-"*40)
        print("App terminated")
        print("-"*40)
        break

    else:
        print("Invalid Choice")
        
   


    

