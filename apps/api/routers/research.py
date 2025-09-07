import os
from typing import Optional, List
from fastapi import APIRouter, UploadFile, File, Form
from pydantic import BaseModel
from dotenv import load_dotenv


from src.graph.agent_graph import build_graph
from src.graph.state import GraphState, ResearchRequest
from src.tools.loaders import save_and_prepare_docs, crawl_url_to_text
from src.retrieval.vectorstore import ensure_index

load_dotenv()
router = APIRouter(tags=["research"])


class IngestResponse(BaseModel):
    added_files: List[str]
    index_path: str


@router.post("/ingest", response_model=IngestResponse)
async def ingest_endpoint(
    files: Optional[List[UploadFile]] = None,
    url: Optional[str] = Form(None), 
):
    raw_dir = os.getenv("RAW_DOCS_PATH", "./data/raw")
    os.makedirs(raw_dir, exist_ok=True)
    added = []

    if url:
        path = await crawl_url_to_text(url, raw_dir)
        added.append(path)

    if files:
        more = await save_and_prepare_docs(files, raw_dir)
        added.extend(more)

    index_path = os.getenv("VECTOR_INDEX_PATH", "./data/index/faiss_index")
    ensure_index(raw_dir, index_path)  # builds or updates

    return IngestResponse(added_files=added, index_path=index_path)

@router.post("/query")
async def query_endpoint(req: ResearchRequest):
    # Build the minimal graph: retrieve -> summarize
    app = build_graph()
    state: GraphState = {"query": req.query, "docs": [], "answer": "", "citations": []}
    result: GraphState = app.invoke(state)
    return 
         
         
         
     
