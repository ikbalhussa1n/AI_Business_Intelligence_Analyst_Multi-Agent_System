import os
from dotenv import load_dotenv
load_dotenv()
import getpass

from langchain.agents import create_agent
from langchain.tools import tool


from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-Coder-7B-Instruct",
    huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"],
    task="text-generation",
)


model = ChatHuggingFace(llm=llm)


sql_agent = create_agent(
    model=model,

    system_prompt=
    """
    You are a SQL Database Agent.

    Responsibilities:
    - Convert questions into SQL
    - Understand database schemas
    - Generate optimized queries

    Rules:
    - Only output SQL
    - Never invent tables
    - Ask for schema if missing
    """
)



