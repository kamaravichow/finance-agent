from agno.agent import Agent
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.embedder.google import GeminiEmbedder
from agno.knowledge.reader.markdown_reader import MarkdownReader
from agno.vectordb.pgvector import PgVector
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(".env.local")

db = "postgresql://postgres:fk4ye1eoojlsq4umn1dgi19cot37phrv@turntable.proxy.rlwy.net:59648/railway"

knowledge = Knowledge(
    vector_db=PgVector(
        embedder=GeminiEmbedder(),
        table_name="markdown_documents",
        db_url=db,
    ),
)


# ./knowledge/** all the markdown files under this directory
for file in Path("./knowledge").glob("**/*.md"):
    print("Processing file: ", file)
    knowledge.add_content(
        path=file,
        reader=MarkdownReader(),
    )



    
