# purpose: to run full program logic (read tasks from input, convert tasks, 
# feed to llm, process results, and output results)
from src.parsing import task_converter
from src.parsing import task_reader
from src.clients import gemini

reader = task_reader.TaskReader()
tasklist = reader.read_from_cli()
json_output = task_converter.convert_to_json(tasklist)

# only output if there's tasks
if json_output != "[]":
    print(json_output)

# test llm
client = gemini.build_connection()
interaction = gemini.send_prompt(client, "Hey, this is a test message to gemini thru a python program. Please respond with a msg")
response = gemini.get_text_response(interaction)
print(response)