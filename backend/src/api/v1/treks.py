from fastapi import APIRouter, Query

from src.schemas.common import PaginatedResponse
from src.schemas.trek import TrekListItem
from src.services.service_registry import get_registry

router = APIRouter(prefix="/treks")


@router.get("", response_model=PaginatedResponse[TrekListItem])
def list_treks(
    featured: bool | None = None,
    difficulty: str | None = None,
    region: str | None = None,
    year: int | None = None,
    search: str | None = None,
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100),
):
    service = get_registry().content_service
    repository = get_registry().trek_repository
    items = service.get_treks(featured=featured, difficulty=difficulty, region=region, year=year, search=search)
    start = (page - 1) * limit
    end = start + limit
    return PaginatedResponse(items=items[start:end], pagination=repository.paginate(items, page, limit))


@router.get("/{slug}", response_model=TrekListItem)
def get_trek(slug: str):
    return get_registry().content_service.get_trek_by_slug(slug)
