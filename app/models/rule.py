from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Rule(Base):
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, index=True)
    action_type = Column(String)
    action_config = Column(String)
    active = Column(Boolean, default=True)