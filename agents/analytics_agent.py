import os
from dotenv import load_dotenv
load_dotenv()
import getpass

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.tools import tool

from tools.analytics import (
    dataframe_summary,
    missing_values,
    correlation_matrix,
    group_statistics,
    statistics
)

if "GOOGLE_API_KEY_ANALYTICS" not in os.environ:
    os.environ["GOOGLE_API_KEY_ANALYTICS"] = getpass.getpass("Enter your Google Analytics AI API key: ")


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
)



analytics_agent = create_agent(model=model,

                    tools=[dataframe_summary,
                        missing_values,
                        correlation_matrix,
                        group_statistics,
                        statistics],

            system_prompt="""
                You are a Data Analytics Agent.

                Responsibilities:
                - Analyze datasets
                - Find trends
                - Calculate KPIs
                - Detect anomalies

                You receive data from SQL Agent.
                Return business insights.
                """
)


