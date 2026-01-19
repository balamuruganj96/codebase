from tiktoken import encoding_for_model
import tiktoken 

enc = encoding_for_model("gpt-4o-mini")
#enc = tiktoken.get_encoding("cl100k_base")
text = """what are the 7 LLM Generation Parameters .give me explanation of each in brief and its use.by default whats the value"""
tokens = enc.encode(text)
print(len(tokens))  # number of tokens
print(tokens)       # token IDs
