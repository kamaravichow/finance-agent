from agno.agent import Agent
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.embedder.google import GeminiEmbedder
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.vectordb.pgvector import PgVector
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# Load PostgreSQL database URL from environment variables for security
db = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/dbname")

# Initialize knowledge base with vector database
knowledge = Knowledge(
    vector_db=PgVector(
        embedder=GeminiEmbedder(),
        table_name="markdown_documents",
        db_url=db,
    ),
)

# Process all markdown files in the knowledge directory
# This populates the vector database with embedded content for semantic search
for file in Path("./knowledge").glob("**/*.md"):
    print("Processing file: ", file)
    knowledge.add_content(
        path=file,
        reader=MarkdownReader(),
    )
