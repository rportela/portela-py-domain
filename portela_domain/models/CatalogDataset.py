from typing import List, Optional

from pydantic import BaseModel

from .CatalogTable import CatalogTable


class CatalogDataset(BaseModel):
    organization_id: str
    name: str
    description: Optional[str] = None
    tables: Optional[List[CatalogTable]] = None

    def make_id(self) -> str:
        return f"{self.organization_id}__{self.name.lower().replace(' ', '-')}"
