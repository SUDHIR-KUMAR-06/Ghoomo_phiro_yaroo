from src.repositories.base import InMemoryRepository
from src.schemas.departure import Departure, DepartureCreate, DepartureUpdate


class DepartureRepository(InMemoryRepository[Departure]):
    def list_filtered(
        self,
        *,
        trek_id: str | None = None,
        month: int | None = None,
        year: int | None = None,
        region: str | None = None,
        difficulty: str | None = None,
    ) -> list[Departure]:
        items = self.list()
        if trek_id:
            items = [item for item in items if item.trek_id == trek_id]
        if month:
            items = [item for item in items if item.departure_date.month == month]
        if year:
            items = [item for item in items if item.departure_date.year == year]
        if region:
            items = [item for item in items if region.lower() in {tag.lower() for tag in item.tags}]
        if difficulty:
            items = [item for item in items if difficulty.lower() in {tag.lower() for tag in item.tags}]
        return items

    def create_departure(self, payload: DepartureCreate) -> Departure:
        return self.create(Departure, payload.model_dump())

    def update_departure(self, item_id: str, payload: DepartureUpdate) -> Departure | None:
        return self.update(item_id, payload.model_dump(exclude_none=True))
