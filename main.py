from agno.os import AgentOS
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools
from agno.models.google import Gemini
import os

import dotenv

dotenv.load_dotenv(".env.local")

agent = Agent(
    name="Personal Accountant",
    model=Gemini(id="gemini-flash-latest", api_key=os.getenv("GOOGLE_API_KEY")),
    # reasoning=True,
    db=SqliteDb(db_file="personal_accountant.db"),
    add_history_to_context=True,
    enable_agentic_memory=True,
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(),
    ],
    cache_session=True,
    markdown=True,
    telemetry=True,
)

agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="main:app", reload=True)
