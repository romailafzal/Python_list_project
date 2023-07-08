"""
This code is a simple task management program
 that allows you to add, update,
 remove, mark tasks as complete or
incomplete, and display the tasks. 
"""
work_list = []    #create empty list

#function to add task
def add_task(task):
    """This function add tasks to the list"""
    work_list.append([task ,False])

#function to update task
def update(index,new_task):
    """This Function update the task by using index"""
    if index < len(work_list):
        work_list[index][0]=new_task

#function to remove task
def remove(index):
    """This Function remove the task by using index"""
    if index < len(work_list):
        work_list.pop(index)
    else:
        print("Invalid index")


#function to mark task as complete
def complete(index):
    """This Function update the task to complete by using index"""
    if index < len(work_list):
        if work_list[index][1] is True:
            print("Task already completed")
        work_list[index][1]=True
    else:
        print("Invalid index")

#function to mark task as incomplete
def incomplete(index):
    """This Function update the task to incomplete by using index"""
    if index < len(work_list):
        if work_list[index][1] is False:
            print("Task already incomplete")
        work_list[index][1]=False
    else:
        print("Invalid index")


#function to display task
def display():
    """ This Function display the list by marking complete as '☑' and incomplete as '☐' """
    if len(work_list) == 0:
        print("No task")
    else:
        for i, task in enumerate(work_list):
            checkbox = '☑' if task[1] else '☐'
            print(f" {[i]} {checkbox} {task[0]}")


def menu():
    """This Function Display the Menu"""
    print("1. Add task")
    print("2. Update task")
    print("3. Remove task")
    print("4. Complete task")
    print("5. Incomplete task")
    print("6. Display task")
    print("7. Exit")
    return int(input("Enter your choice: "))


while True:
    choice = menu()
    if choice == 1:
        newtask = input("Enter task: ")
        add_task(newtask)
    elif choice == 2:
        display()
        update_index = int(input("Enter index: "))
        if update_index < len(work_list):
            up_new_task = input("Enter new task: ")
            update(update_index,up_new_task)
        else:
            print("Invalid index")
    elif choice == 3:
        display()
        if update_index < len(work_list):
            remove_index = int(input("Enter index: "))
            remove(remove_index)
        else:
            print("Invalid index")
    elif choice == 4:
        display()
        complete_index = int(input("Enter index: "))
        complete(complete_index)
    elif choice == 5:
        display()
        incomplete_index = int(input("Enter index: "))
        incomplete(incomplete_index)
    elif choice == 6:
        print("\n*****************************List*********************************\n")
        display()
    elif choice == 7:
        break
    else:
        print("Invalid choice")
        continue
    print("\n*****************************Menu*********************************\n")
