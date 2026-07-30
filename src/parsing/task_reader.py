# purpose: reads a list of tasks from user input to builds a TaskList and Task objects
import task

# encapsulating reading logic into a class allows for future expansion of reading logic 
# e.g. reading from a file, etc.
class TaskReader:
    '''
    Represents a tool that reads tasks from user input and builds a TaskList.
    Attributes:
        user_tasklist (TaskList): A TaskList object containing tasks read from user input.
    '''
    def __init__(self):
        '''Initialize a TaskReader object.'''
        self.user_tasklist = task.TaskList()

    def read_from_cli(self):
        '''Read tasks from user input via cli and build a TaskList object.'''
        # prompt user for Tasks + add to TaskList
        print("Welcome User!\n")
        while True:
            print("Please enter a task for the week or type 'done' to finish:")
            choice = input()
            if choice.lower() == "done":
                break
            else:
                current_task = task.Task(choice)
                self.user_tasklist.tasks.append(current_task) 

        # print/test confirm task list
        if len(self.user_tasklist.tasks) > 0:
            print("\nTasks for the week:")
            i = 1
            for current_task in self.user_tasklist.tasks:
                print("Task", i, ":", current_task.name)
                i += 1
            del i
        else:
            print("No tasks for the week!")