import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_files_info import schema_get_files_info

arguments = os.sys.argv
if len(arguments) < 2:
    print("Usage: python main.py '<your prompt here>'")
    exit(1)

prompt = arguments[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]

load_dotenv()

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

available_functions = types.Tool(
    function_declarations=[schema_get_files_info],
)

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    ),
)

if response.candidates[0].content.parts[0].function_call:
    for function_call_part in response.candidates[0].content.parts:
        if function_call_part.function_call:
            print(
                f"Calling function: {function_call_part.function_call.name}({function_call_part.function_call.args})"
            )
else:
    print(response.text)

if "--verbose" in arguments:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
