import os
from typing import Optional, List
from fastapi import APIRouter, UploadFile, File, Form
from pydantic import BaseModel
from dotenv import load_dotenv


from src.graph.agent_graph import build_graph
from src.graph.state import GraphState, ResearchRequest