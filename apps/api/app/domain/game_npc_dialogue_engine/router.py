from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.game_npc_dialogue_engine.schemas import AgenticGameNpcDialogueEngineSessionCreate, AgenticGameNpcDialogueEngineSessionResponse
from app.domain.game_npc_dialogue_engine.service import AgenticGameNpcDialogueEngineService

router = APIRouter(prefix="/api/v1/game_npc_dialogue_engine", tags=["Agentic Game Npc Dialogue Engine Domain"])

@router.post("/sessions", response_model=AgenticGameNpcDialogueEngineSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticGameNpcDialogueEngineSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Game Npc Dialogue Engine.
    """
    return AgenticGameNpcDialogueEngineService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticGameNpcDialogueEngineSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticGameNpcDialogueEngineService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
