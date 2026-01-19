from agno.os import AgentOS
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.anthropic import Claude

agent = Agent(
    name="Personal Accountant",
    model=Claude(id="claude-sonnet-4-5"),
    db=SqliteDb(db_file="personal_accountant.db"),
    add_history_to_context=True,
    markdown=True,
)

agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="personal_accountant:app", reload=True)