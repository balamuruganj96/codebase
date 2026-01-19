from openai import OpenAI
import tiktoken

client = ()

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {
        "role": "user",
        "content": "what are the 7 LLM Generation Parameters .give me explanation of each in brief and its use.by default whats the value"
    }
]

model = "gpt-4o-mini"

enc = tiktoken.encoding_for_model(model)

def count_message_tokens(messages):
    tokens = 0
    for msg in messages:
        tokens += 3  # OpenAI chat markup overhead (approx)
        tokens += len(enc.encode(msg["content"]))
        tokens += len(enc.encode(msg["role"]))
    tokens += 3  # final assistant priming
    return tokens

input_tokens = count_message_tokens(messages)

print("Input tokens:", input_tokens)
