from uuid import UUID
from typing import Optional

from pydantic import BaseModel

class CategoryBase(BaseModel): 
    name: str
    desc: Optional[str] = None

class CategoryCreate(CategoryBase): 
    pass

class CategoryUpdate(BaseModel): 
    # Что обозначает None??? 
    name: Optional[str] = None
    desc: Optional[str] = None


class CategoryResponse(CategoryBase):
    uuid: UUID

    # Что это??? 
    class Config:
        from_attributes = True