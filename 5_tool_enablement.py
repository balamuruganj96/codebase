from langchain_openai import AzureChatOpenAI
from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv()
#decorator to turn a py function to a langchain tool
@tool
def multiply(a: int, b: int) -> int:
    """Multiply a and b."""
    return a * b


llm = AzureChatOpenAI(
    azure_endpoint="https://dbt-poc.openai.azure.com/",
    azure_deployment="dbtpoc",
    api_version="2024-12-01-preview",
    model='GPT-4.1 nano'
)
response=llm.invoke("what is 2*3 and then multiplied by 100")
print(response.content)
print(response.tool_calls)


llm_with_tools=llm.bind_tools([multiply])
resp=llm_with_tools.invoke("what is 2*3 and then multiplied by 100")
print(response.content)
print(resp.tool_calls)
