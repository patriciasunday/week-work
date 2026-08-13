# purpose: to run full program logic (read tasks from input, convert tasks, 
# feed to llm, process results, and output results)
from src.parsing import task_converter
from src.parsing import task_reader

reader = task_reader.TaskReader()
tasklist = reader.read_from_cli()
json_output = task_converter.convert_to_json(tasklist)

# only output if there's tasks
if json_output != "[]":
    print(json_output)