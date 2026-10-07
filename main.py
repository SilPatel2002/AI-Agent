import os
import argparse
from dotenv import load_dotenv



from openai import OpenAI


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
        {"role": "user", "content": args.user_prompt},
    ]

    response = client.chat.completions.create(
        model="openrouter/free",
        messages = messages,
    )


    if response.usage is None:
        raise RuntimeError("Response's usage property is None: Likely a failed API request")

    if args.verbose == True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    print(response.choices[0].message.content)







if __name__ == "__main__":
    main()
