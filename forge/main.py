#!/usr/bin/env python3

import re
import sys
import subprocess

from dotenv import load_dotenv
from octoai.client import Client

load_dotenv()

client = Client()


def execute():
    completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Pretend you are scripting in a unix shell. I will give you a task and you will provide the "
                           "command to perform that task. Output the command to be run in triple backticks like "
                           "this: ```<shell command>```. Do not provide any other text or explanation of the command."
            },
            {
                "role": "user",
                "content": "The task: " + ' '.join(sys.argv[4:])
            }
        ],
        model="mixtral-8x7b-instruct",
        max_tokens=128,
        presence_penalty=0,
        temperature=0.1,
        top_p=0.1
    )

    res = completion.__dict__['choices'][0].__dict__['message'].__dict__['content']

    pattern = r'```([^`]+)```'

    # Find all matches
    matches = re.findall(pattern, res, re.MULTILINE | re.DOTALL)

    # Extract the content between the "```"
    if matches:
        command = matches[0]
    else:
        command = res

    # Define the command you want to execute

    # Execute the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Check the result
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Error executing command. Error message: ")
        print(result.stderr)


if __name__ == "__main__":
    execute()
