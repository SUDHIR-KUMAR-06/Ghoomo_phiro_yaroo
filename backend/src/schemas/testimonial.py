from pydantic import BaseModel, Field

from src.schemas.common import BaseDocument


class TestimonialBase(BaseModel):
    name: str
    initials: str
    route_label: str
    rating: int = Field(ge=1, le=5)
    quote: str
    is_featured: bool = True


class TestimonialCreate(TestimonialBase):
    pass


class TestimonialUpdate(BaseModel):
    name: str | None = None
    initials: str | None = None
    route_label: str | None = None
    rating: int | None = None
    quote: str | None = None
    is_featured: bool | None = None


class TestimonialItem(BaseDocument, TestimonialBase):
    pass
