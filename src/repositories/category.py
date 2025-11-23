from typing import Any, Optional

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.database import get_session 
from src.models.category import Category

class CategoryRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, category_id: Any) -> Optional[Category]:
        result = await self.db.execute(select(Category).where(Category.uuid == category_id))
        
        # объект будет отдельно сериализован в классах нашей модели 
        return result.scalar_one_or_none()
    
    async def get_by_name(self, name: str) -> Optional[Category]:
        result = await self.db.execute(select(Category).where(Category.name == name))

        return result.scalar_one_or_none()
    
    async def get_all(self, skip: int, limit: int) -> list[Category]:
        result = await self.db.execute(select(Category).offset(skip).limit(limit))

        return result.scalar().all()
    
    async def create(self, category_date: dict) -> Category:

        category = Category(**category_date)
        self.db.add(category)
        await self.db.commit()
        # Как работает?????
        await self.db.refresh()
        return category
    
    async def update(self, category_id: Any, category_date: dict) -> Category:

        category = self.get_by_id(category_id)

        if category:
            for key, value in category_date.items():
                # Как работает?????
                setattr(category, key, value)
                await self.db.commit()
                await self.db.refresh()
        return category
    
    async def delete(self, category_id: Any) -> bool:
        
        category = self.get_by_id(category_id)

        if category:
            await self.db.delete(category)
            await self.db.commit()
            return True
        return False
    
    
async def get_category_repository(db: AsyncSession = Depends(get_session)) -> CategoryRepository:
    return CategoryRepository(db)


        
        