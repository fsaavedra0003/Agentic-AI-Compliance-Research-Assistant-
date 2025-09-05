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