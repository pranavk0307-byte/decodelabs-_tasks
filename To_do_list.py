def task():
    task = [] 
    print("welcome to TO DO LIST")

    total_task = int(input("enter how many task you want to do Today : "))
    
    for i in range(1,total_task+1): 
        task_name = input(f"enter task {i} =")
        task.append(task_name)
        
    print(f"todays task is : {task}")

    while True:
        operation = int(input("enter 1 for Add\nenter 2 for update\nenter 3 for delete\nenter 4 for View\nenter 5 for Exit/stop"))
        if operation == 1:
            add = input("enter the task you wanted to add : ")
            task.append(add)
            print(f"task {add} has been succesfully added")
        
        elif operation == 2:
            updated_val = input("enter the task name you want to update :")
            if updated_val in task:
                up = input("enter new task =")
                ind = task.index(updated_val)
                task[ind] = up
                print(f"updated task {up}")
            
        elif operation == 3 :
             delete_val = input("whcih task you want to delete :")
        if delete_val in task:
                ind = task.index(delete_val)
                del task[ind]
                print(f"task value {delete_val} has been deleted")

        elif operation == 4 :
            print(f"total task = {task}")
            
        elif operation == 5:
            print("closing the program")
            break
        else :
            print("invalid input")

task()          #callig the function 