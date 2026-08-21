# purpose: to run full program logic (read tasks from input, convert tasks, 
# feed to llm, process results, and output results)
from src.parsing import task_converter
from src.parsing import task_reader
from src.clients import gemini
from src.processing import task_processor

# get tasks from user input (cli) to json
reader = task_reader.TaskReader()
tasklist = reader.read_from_cli()
json_output = task_converter.convert_to_json(tasklist)

# send tasks to llm for processing 
prompt = task_processor.build_prompt(json_output)
interaction = gemini.send_prompt(gemini.build_connection(), prompt)
tasklist = task_processor.get_processed_tasks(gemini.get_text_response(interaction))

print("Here are your sorted tasks:")
for task in tasklist.tasks:
    print(f"{task.order}: {task.name}")