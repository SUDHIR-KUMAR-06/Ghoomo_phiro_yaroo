from src.repositories.base import InMemoryRepository
from src.schemas.trek import TrekCreate, TrekListItem, TrekUpdate


class TrekRepository(InMemoryRepository[TrekListItem]):
    def list_filtered(
        self,
        *,
        featured: bool | None = None,
        difficulty: str | None = None,
        region: str | None = None,
        year: int | None = None,
        search: str | None = None,
    ) -> list[TrekListItem]:
        items = self.list()
        if featured is not None:
            items = [item for item in items if item.is_featured is featured]
        if difficulty:
            items = [item for item in items if item.difficulty.value == difficulty]
        if region:
            items = [item for item in items if item.region.lower() == region.lower()]
        if year:
            items = [item for item in items if item.batch_year == year]
        if search:
            query = search.lower()
            items = [item for item in items if query in item.name.lower() or query in item.summary.lower()]
        return items

    def get_by_slug(self, slug: str) -> TrekListItem | None:
        return self.get_one(lambda item: item.slug == slug)

    def create_trek(self, payload: TrekCreate) -> TrekListItem:
        return self.create(TrekListItem, payload.model_dump())

    def update_trek(self, item_id: str, payload: TrekUpdate) -> TrekListItem | None:
        return self.update(item_id, payload.model_dump(exclude_none=True))
