import os
from dotenv import load_dotenv
load_dotenv()
import getpass
from tools.database import get_schema, execute_query,list_tables

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.tools import tool

if "GOOGLE_API_KEY_REPORT" not in os.environ:
    os.environ["GOOGLE_API_KEY_REPORT"] = getpass.getpass("Enter your Google report AI API key: ")


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
)




sql_agent = create_agent(
    model=model,
    tools=[
        get_schema,
        execute_query,
        list_tables
    ],
    system_prompt="""
You are a SQL Database Agent.

Your job:
- Understand database structure.
- Write PostgreSQL queries.
- Execute queries.
- Return accurate answers.

Always:
1. Call get_schema first.
2. Use execute_query for database questions.

Never:
- Guess tables.
- Guess columns.
- Create fake data.
"""
)


response = sql_agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What our total revenue?"
            }
        ]
    }
)

print(response["messages"][-1].content[0]["text"])