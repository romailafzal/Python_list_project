work_list = []    #create empty list

#function to add task
def add_task(task):   
    work_list.append({"Work": task , "Completed":False})

#function to update task
def update(index,new_task):
    if index < len(work_list):
        work_list[index]["Work"]=new_task

#function to remove task
def remove(index):
    if index < len(work_list):
        work_list.pop(index)


#function to mark task as complete
def complete(index):
    if index < len(work_list):
        work_list[index]["Completed"]=True

#function to mark task as incomplete
def incomplete(index):
    if index < len(work_list):
        work_list[index]["Completed"]=False


#function to display task
def display():
    for i, task in enumerate(work_list):
        checkbox = '☑' if task['Completed'] else '☐'
        print(f"{checkbox} {task['Work']}")


add_task("learn python")
add_task("learn java")
add_task("join tags")
print("Before update")
display()


update(0,"Learn python & Django")
print("After update")
display()

remove(1)
print("After remove")
display()

complete(0)
print("After completed task 1")
display()

complete(1)
complete(2)
print("After completed all task")
display()