### TO DO  CONSOLE APPP 
print("--- TO-DO-LIST APP ---")
print("1. Add New Tasks \n2. View Current Tasks \n3. Mark Tasks as done \n4. Delete Taks \n5. Exit")
tasks=[]

while True:
    number= input("Enter your choice : ")
    if number =='1' :
        task=input("Enter task : ")
        tasks.append({"title":task,"done":False})
        print("Task added!")
       
    elif number =='2':
        if not tasks:
            print("No tasks yet.")
        else:
            print("\n Your Tasks: ")    
            for i,task in enumerate(tasks,1):
                status="✔️" if task["done"] else"❌"
                print(f"{i}.{task}")

    elif number =='3':
        task_no=int(input("Enter the task number to mark as done:"))
        if 0<task_no<=len(tasks):
            tasks[task_no-1]["done"]=True
            print("Task marked as done!")
        else:
            print("Invalid Task number.")    

    elif number =='4':
        task_no=int (input("Enter the task to be deleted"))
        if 0<task_no<=len(tasks):
            removed=tasks.pop(task_no-1)
            print(f"Removed:{removed['title']}")
        else:
            print("Invalid task  number. ")  

    elif number =='5':
        print("GOODBYE")
        break

    else:
        print("Please choose a valid option (1-5). ")







