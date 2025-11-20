import uuid
from typing import Any
from src.models.base import Base, BaseModelMixin
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


from sqlalchemy import Column, String, Text, ForeignKey

from src.configs.app import settings 



class Post(Base, BaseModelMixin):

    __tablename__ = "posts"

    media_id = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    desc = Column(Text)

    category_id = Column(UUID(as_uuid=True), ForeignKey("category.uuid", ondelete="SET NULL"), nullable=True)

    category = relationship("Category", back_populates="posts", lazy="select")

    def __repr__(self) -> str:
        return f""
    
    def to_dict(self) -> dict[str, Any]:
        return {}
    
