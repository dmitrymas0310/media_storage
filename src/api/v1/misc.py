from fastapi import APIRouter

from configs.app import settings
from schemas.misc_schema import HelthCheckSchema

router = APIRouter()


@router.get("/health", response_model=HelthCheckSchema)
def health():
    return HelthCheckSchema(status="ok", version=settings.app.app_version)
