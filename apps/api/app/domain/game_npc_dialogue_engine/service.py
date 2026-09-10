from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.game_npc_dialogue_engine.models import AgenticGameNpcDialogueEngineSession, AgenticGameNpcDialogueEngineItem
from app.domain.game_npc_dialogue_engine.schemas import AgenticGameNpcDialogueEngineSessionCreate, AgenticGameNpcDialogueEngineItemCreate

class AgenticGameNpcDialogueEngineService:
    @staticmethod
    def create_session(db: Session, data: AgenticGameNpcDialogueEngineSessionCreate) -> AgenticGameNpcDialogueEngineSession:
        db_obj = AgenticGameNpcDialogueEngineSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticGameNpcDialogueEngineSession:
        return db.query(AgenticGameNpcDialogueEngineSession).filter(AgenticGameNpcDialogueEngineSession.id == session_id).first()
