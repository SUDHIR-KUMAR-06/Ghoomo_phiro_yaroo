from pydantic import BaseModel

from src.schemas.common import BaseDocument


class FAQBase(BaseModel):
    question: str
    answer: str
    sort_order: int = 0
    is_active: bool = True


class FAQCreate(FAQBase):
    pass


class FAQUpdate(BaseModel):
    question: str | None = None
    answer: str | None = None
    sort_order: int | None = None
    is_active: bool | None = None


class FAQItem(BaseDocument, FAQBase):
    pass
