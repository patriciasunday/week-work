# purpose: converts a list of tasks into a certain format to be processed by an LLM
import json

def convert_to_json(tlist: object) -> str:
    '''
    Converts a TaskList object into JSON format.
    
    Args:
      tlist: A TaskList object to be converted.
    Returns:
      A JSON string representing the TaskList object.
    '''
    json_tasks = []
    for task in tlist.tasks:
        json_task = {
            "id": task.id,
            "name": task.name,
            "order": task.order
        }
        json_tasks.append(json_task)
    
    return json.dumps(json_tasks)