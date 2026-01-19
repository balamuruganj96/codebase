from langchain_openai import AzureChatOpenAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
from dotenv import load_dotenv
load_dotenv()

llm = AzureChatOpenAI(
    azure_endpoint="https://dbt-poc.openai.azure.com/",
    azure_deployment="dbtpoc",
    api_version="2024-12-01-preview",
    model='GPT-4.1 nano'
)


def parse_the_output(result):
    usage = result.response_metadata.get("token_usage", {})
    prompt_tokens = usage.get("prompt_tokens")
    completion_tokens = usage.get("completion_tokens")
    total_tokens = usage.get("total_tokens")
    print(f"Tokens -> Prompt: {prompt_tokens}, Completion: {completion_tokens}, Total: {total_tokens}")

chat_history=[]
chat_history.append(SystemMessage('You are a helpful AI assistant'))
while True:
    input_string=input('You:')
    if input_string=='exit':
        break
    chat_history.append(HumanMessage(content=input_string))
    result=llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print(f'AI:{result.content}  token info:{parse_the_output(result)}')
print(chat_history)
