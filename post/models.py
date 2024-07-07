from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from database import Base
from datetime import datetime, timedelta
import uuid
import bcrypt
import jwt


class Post(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String,  index=True)
    content = Column(String)
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    author = relationship("user.models.User", backref="posts")
