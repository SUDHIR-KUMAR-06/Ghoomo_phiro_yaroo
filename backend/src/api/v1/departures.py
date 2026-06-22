from fastapi import APIRouter, Query

from src.schemas.common import PaginatedResponse
from src.schemas.departure import Departure
from src.services.service_registry import get_registry

router = APIRouter(prefix="/departures")


@router.get("", response_model=PaginatedResponse[Departure])
def list_departures(
    trek_id: str | None = None,
    month: int | None = Query(default=None, ge=1, le=12),
    year: int | None = None,
    region: str | None = None,
    difficulty: str | None = None,
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100),
):
    service = get_registry().content_service
    repository = get_registry().departure_repository
    items = service.get_departures(trek_id=trek_id, month=month, year=year, region=region, difficulty=difficulty)
    start = (page - 1) * limit
    end = start + limit
    return PaginatedResponse(items=items[start:end], pagination=repository.paginate(items, page, limit))
