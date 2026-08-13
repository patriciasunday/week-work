# purpose: reads a list of tasks from user input to builds TaskList and Task objects
from src.parsing import task

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
        '''Reads tasks from user input via cli and builds a TaskList object.
        
        Returns:
            A Tasklist object containing Tasks read from user input.
        '''
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

        return self.user_tasklist