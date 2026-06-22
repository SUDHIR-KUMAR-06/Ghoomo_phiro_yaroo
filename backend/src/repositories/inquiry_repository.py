from src.repositories.base import InMemoryRepository
from src.schemas.inquiry import InquiryRecord


class InquiryRepository(InMemoryRepository[InquiryRecord]):
    pass
