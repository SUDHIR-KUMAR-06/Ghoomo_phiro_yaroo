from src.repositories.base import InMemoryRepository
from src.schemas.faq import FAQCreate, FAQItem, FAQUpdate


class FAQRepository(InMemoryRepository[FAQItem]):
    def create_faq(self, payload: FAQCreate) -> FAQItem:
        return self.create(FAQItem, payload.model_dump())

    def update_faq(self, item_id: str, payload: FAQUpdate) -> FAQItem | None:
        return self.update(item_id, payload.model_dump(exclude_none=True))
