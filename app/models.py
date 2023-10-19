from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer

from app.db import Base


class PostInfo(Base):
    __tablename__ = "Post"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(100))
    user_id = Column(String(50))
