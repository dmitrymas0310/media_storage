from fastapi import APIRouter, Depends, HTTPException, status

from src.repositories.category import CategoryRepository, get_category_repository
from src.schemas.category_schemas import CategoryCreate

# APIRouter - зачем нужен???
router = APIRouter()

@router.post("/")
async def create_category(
    category_date: CategoryCreate, 
    repository: CategoryRepository = Depends(get_category_repository)
):
    if repository.get_by_name(category_date.name):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST       
        )
      
    
    category = repository.create(category_date.model_dump())

    return category

