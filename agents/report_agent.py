import os
from dotenv import load_dotenv
load_dotenv()
import getpass

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.tools import tool

from tools.report import create_markdown_report, create_pdf_report

if "GOOGLE_API_KEY_REPORT" not in os.environ:
    os.environ["GOOGLE_API_KEY_REPORT"] = getpass.getpass("Enter your Google report AI API key: ")


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
)


print("Report agent invoked")


report_agent = create_agent(model=model,

                            tools = [
    create_markdown_report,
    create_pdf_report
],
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


# response = report_agent.invoke(
#     {
#         "messages": [
#             {
#                 "role": "user",
#                 "content": "Who is the president of usa?"
#             }
#         ]
#     }
# )

# print(response["messages"][-1].content)