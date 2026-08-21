# purpose: to enforce/enable task reasoning business logic
import json
from src.parsing import task

def build_prompt(task_json: str) -> str:
    """
    Builds a prompt for the LLM to process tasks.
    
    Args:
      task_json: A JSON string representing the list of tasks.
    Returns:
        A string containing the full prompt for the LLM.
    """
    prompt_header = """You are a task reasoning organizer. You will be given a 
    list of tasks in JSON format. Your job is to analyze the tasks, determine their dependencies, 
    and return the sorted list of tasks in JSON format. Your response should be a valid JSON array, 
    without any additional text. Your reasoning must be consistent and logical, resulting in the 
    same task order every time, ensuring duplicate tasks are eliminated, and spelling mistakes
    are corrected. Here is the list of tasks in JSON format:\n"""
    return prompt_header + task_json

# output result func: takes in llm response, parses into tasks & returns sorted tasklist obj
def get_processed_tasks(task_json: str) -> task.TaskList:
    """
    Processes an LLM response to extract a sorted list of Tasks
    
    Args:
        task_json: A JSON string of the LLM's response containing the sorted tasks.
    Returns:
        A TaskList object containing the sorted Tasks.
    """
    sorted_list = task.TaskList()
    tasks = json.loads(task_json)
    for t in tasks:
        sorted_list.tasks.append(task.Task(t['name'], id=t['id'], order=t['order']))
    return sorted_list