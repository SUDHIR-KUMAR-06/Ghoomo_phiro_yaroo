from src.repositories.base import InMemoryRepository
from src.schemas.testimonial import TestimonialCreate, TestimonialItem, TestimonialUpdate


class TestimonialRepository(InMemoryRepository[TestimonialItem]):
    def create_testimonial(self, payload: TestimonialCreate) -> TestimonialItem:
        return self.create(TestimonialItem, payload.model_dump())

    def update_testimonial(self, item_id: str, payload: TestimonialUpdate) -> TestimonialItem | None:
        return self.update(item_id, payload.model_dump(exclude_none=True))
