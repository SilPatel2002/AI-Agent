import os
import argparse
import json
from prompts import system_prompt
from dotenv import load_dotenv
from openai import OpenAI
from functions.call_function import available_functions, call_function


def main():

    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")

    if api_key is None:
        raise RuntimeError("OPENROUTER_API_KEY is not set in the environment variables.")


    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`


    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    response = client.chat.completions.create(
        model="openrouter/free",
        messages = messages,
        tools=available_functions,
        temperature=0,
    )


    if response.usage is None:
        raise RuntimeError("Response's usage property is None: Likely a failed API request")

    

    if args.verbose == True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")


    message = response.choices[0].message

    if message.tool_calls is None:
        print(message.content)
        return
    
    for tool_call in message.tool_calls:
        result_message = call_function(tool_call)
        if not result_message["content"]:
            raise Exception("Something ain't right")

        if args.verbose == True:
            print(f"-> {result_message['content']}")



    







if __name__ == "__main__":
    main()
