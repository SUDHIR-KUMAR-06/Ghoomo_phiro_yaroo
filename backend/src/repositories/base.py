from __future__ import annotations

from collections.abc import Callable
from copy import deepcopy
from datetime import datetime, timezone
from math import ceil
from typing import Generic, TypeVar
from uuid import uuid4

from pydantic import BaseModel

from src.schemas.common import PaginationMeta

T = TypeVar("T", bound=BaseModel)


class InMemoryRepository(Generic[T]):
    def __init__(self, items: list[T] | None = None):
        self._items: list[T] = list(items or [])

    def list(self) -> list[T]:
        return deepcopy(self._items)

    def get_by_id(self, item_id: str) -> T | None:
        for item in self._items:
            if getattr(item, "id", None) == item_id:
                return deepcopy(item)
        return None

    def get_one(self, predicate: Callable[[T], bool]) -> T | None:
        for item in self._items:
            if predicate(item):
                return deepcopy(item)
        return None

    def create(self, model: type[T], payload: dict) -> T:
        now = datetime.now(timezone.utc)
        item = model(id=str(uuid4()), created_at=now, updated_at=now, **payload)
        self._items.append(item)
        return deepcopy(item)

    def update(self, item_id: str, updates: dict) -> T | None:
        for index, item in enumerate(self._items):
            if getattr(item, "id", None) != item_id:
                continue
            merged = item.model_dump()
            merged.update({key: value for key, value in updates.items() if value is not None})
            merged["updated_at"] = datetime.now(timezone.utc)
            updated = item.__class__(**merged)
            self._items[index] = updated
            return deepcopy(updated)
        return None

    def delete(self, item_id: str) -> bool:
        for index, item in enumerate(self._items):
            if getattr(item, "id", None) == item_id:
                self._items.pop(index)
                return True
        return False

    def paginate(self, items: list[T], page: int, limit: int) -> PaginationMeta:
        total = len(items)
        pages = ceil(total / limit) if limit else 1
        return PaginationMeta(page=page, limit=limit, total=total, pages=pages)
