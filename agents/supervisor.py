import os
from dotenv import load_dotenv
load_dotenv()
import getpass

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.tools import tool

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",   
)


print("Supervisor agent invoked")

supervisor_agent = create_agent(model=model,

                     system_prompt=
                     """
                    You are the Supervisor Agent.

                    Your job is to coordinate specialist agents.

                    Available agents:
                    - SQL Agent
                    - Analytics Agent
                    - Report Agent

                    Never perform their work yourself.
                    Decide which agent(s) should handle the request.
                    Return a clear execution plan.
"""
)



