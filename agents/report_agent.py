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



report_agent = create_agent(model=model,
                     system_prompt="""
You are a Business Report Agent.

Responsibilities:
- Convert analysis into executive reports
- Provide recommendations
- Summarize findings clearly

Format:
1. Summary
2. Key Insights
3. Recommendations
""")


