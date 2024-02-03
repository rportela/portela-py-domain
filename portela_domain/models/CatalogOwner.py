from typing import Optional

from pydantic import BaseModel


class CatalogOwner(BaseModel):
    name: str
    email: Optional[str] = None
