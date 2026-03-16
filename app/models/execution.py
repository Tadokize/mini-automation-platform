from sqlalchemy import Column, Integer, String, DateTime, JSON
from datetime import datetime
from app.database import Base

class Execution(Base):
    __tablename__ = "executions"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer)
    rule_id = Column(Integer)
    status = Column(String)
    result = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)