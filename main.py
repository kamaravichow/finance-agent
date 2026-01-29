from agno.os import AgentOS
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools
from agno.tools.webtools import WebTools

from agno.models.google import Gemini
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.embedder.google import GeminiEmbedder
from agno.vectordb.pgvector import PgVector
from agno.tools.mcp import MCPTools

import os

import dotenv

dotenv.load_dotenv()

# Load PostgreSQL database URL from environment variables for security
db = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/dbname")

# Initialize knowledge base with vector database for RAG (Retrieval Augmented Generation)
# This stores and retrieves relevant investment lessons and strategies from markdown documents
knowledge = Knowledge(
    vector_db=PgVector(
        embedder=GeminiEmbedder(),  # Uses Google's Gemini for embedding generation
        table_name="markdown_documents",
        db_url=db,
    ),
)

# Configure MCP (Model Context Protocol) tools for Zerodha Kite integration
# This enables real-time market data and order placement capabilities
mcp_tools = MCPTools(
    transport="streamable-http",
    url="https://mcp.kite.trade/mcp",
)

# Initialize the AI investment analyst agent with comprehensive tools and instructions
agent = Agent(
    name="Personal Accountant",
    description=(
        "You are an investment analyst that researches stock prices, "
        "analyst recommendations, and stock fundamentals."
    ),
    instructions=[
        "You are focused for Indian Stock Market",
        # Important: Indian stock ticker symbols require exchange suffix
        # (e.g., TCS.NS for NSE, TCS.BO for BSE)
        (
            "For the ticker symbol, use the BSE or NSE symbol "
            "e.g. TCS for Tata Consultancy Services actual symbol is TCS.NS"
        ),
        "Format your response using markdown and use tables to display data where possible."
        "You perform fundamental analysis of the stock and provide insights based on that.",
        "For using the mcp tools, login first before using kite mcp tools ",
        # Workflow for placing orders: First verify user profile,
        # then get quotes, then place order
        (
            "When asked to place order on zerodha kite via mcp, "
            "make sure you run get_profile, then get_quotes for that instrument "
            "in form of NSE:<symbol> then use that information to place order."
        ),
    ],
    model=Gemini(
        id="gemini-flash-latest",
        api_key=os.getenv("GOOGLE_API_KEY"),
        thinking_budget=8285,
        # include_thoughts=True,
    ),
    db=SqliteDb(db_file="personal_accountant.db"),
    add_history_to_context=True,
    enable_agentic_memory=True,
    tools=[
        ReasoningTools(
            add_instructions=True,
            enable_think=True,
            enable_analyze=True,
        ),
        YFinanceTools(
            cache_dir="./yfinance_cache",
            cache_results=True,
        ),
        WebTools(),
        mcp_tools,
    ],
    add_datetime_to_context=True,
    timezone_identifier="Asia/Kolkata",
    cache_session=True,
    markdown=True,
    telemetry=True,
    knowledge=knowledge,
    add_knowledge_to_context=True,
    enable_agentic_knowledge_filters=True,
)

agent_os = AgentOS(
    agents=[agent],
    enable_mcp_server=True,
)
app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="main:app", reload=True)
