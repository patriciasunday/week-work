# purpose: reads a list of tasks from user input and stores them in a markdown file
import task

user_tasklist = task.TaskList()

 # get task list from user
while True:
    print("Good morning! Please enter a task for the week or type 'done' to finish:")
    choice = input()
    if choice.lower() == "done":
        break
    else:
        current_task = task.Task(choice)
        user_tasklist.tasks.append(current_task)

# print/test confirm task list
if len(user_tasklist.tasks) > 0:
    print("Tasks for the week:")
    i = 1
    for task in user_tasklist.tasks:
        print("Task", i, ":", task.name)
        i += 1
    del i
else:
    print("No tasks for the week!")