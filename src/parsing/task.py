# purpose: defines a task and a list of tasks, providing relevant methods to manipulate them

class Task:
    '''
    Represents a task
    Attributes:
        name (str): The name of the task.
    '''
    def __init__(self, name):
        self.name = name

class TaskList:
    '''
    Represents a list of tasks.
    Attributes:
        tasks (list): A list of Task objects.
    '''
    def __init__(self, tasks=None):
        '''
        Initialize a TaskList object.
        
        :param tasks: Optional list of Task objects. Set to an empty list if not provided.
        '''
        self.tasks = tasks if tasks is not None else []

    def move_task(self, task, new_position):
        '''
        Move a task to a new position in the task list.

        :param task: The Task object to move.
        :param: new_position: The new position (1-based index) to move the task to.
        '''
        while task in self.tasks:
            self.tasks.remove(task)
        self.tasks.insert(new_position-1, task)