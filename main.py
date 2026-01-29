import os

from dotenv import load_dotenv

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

load_dotenv()

# Load PostgreSQL database URL from environment variables for security
# Fail explicitly if DATABASE_URL is not set to prevent accidental use of defaults
db = os.getenv("DATABASE_URL")
if not db:
    raise ValueError(
        "DATABASE_URL environment variable is not set. "
        "Please configure your .env file based on .env.example"
    )

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
        "You are focused on the Indian Stock Market.",
        # Important: Use full ticker format with exchange suffix
        # NSE symbols: SYMBOL.NS (e.g., TCS.NS, RELIANCE.NS)
        # BSE symbols: SYMBOL.BO (e.g., TCS.BO)
        (
            "For ticker symbols, always use the complete format with exchange suffix. "
            "For NSE, use SYMBOL.NS (e.g., TCS.NS for Tata Consultancy Services). "
            "For BSE, use SYMBOL.BO."
        ),
        (
            "Format your response using markdown and use tables to display data where possible. "
            "You perform fundamental analysis of the stock and provide insights based on that."
        ),
        "For using the MCP tools, login first before using Kite MCP tools.",
        # Workflow for placing orders: First verify user profile,
        # then get quotes, then place order
        (
            "When asked to place an order on Zerodha Kite via MCP, "
            "make sure you run get_profile, then get_quotes for that instrument "
            "in the form NSE:<symbol>, then use that information to place the order."
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
