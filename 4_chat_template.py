from langchain_openai import AzureChatOpenAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm = AzureChatOpenAI(
    azure_endpoint="https://dbt-poc.openai.azure.com/",
    azure_deployment="dbtpoc",
    api_version="2024-12-01-preview",
    model='GPT-4.1 nano'
)

messages = [
    ("system", "You are a senior data engineer in {domain}. i just need header or bullet points .not long context"),
    ("human", "{question}"),
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"domain": "supply chain management", "question": 'what are the 5 strong business data quality checks you can include in the gold '})
print(prompt)
result = llm.invoke(prompt)
print(result)
