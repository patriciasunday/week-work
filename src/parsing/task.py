# purpose: defines a task and a list of tasks, providing relevant methods to manipulate them

class Task:
    '''
    Represents a task
    Attributes:
        id (int): The unique identifier for the task.
        name (str): The name of the task.
        order (int): The order of the task relative to others.
    '''

    _id_increment = 0  # Class variable to auto increment task IDs
    def __init__(self, name, order=None):
        Task._id_increment += 1
        self.id = Task._id_increment
        
        self.name = name
        self.order = order

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