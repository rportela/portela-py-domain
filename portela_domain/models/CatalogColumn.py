from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class CatalogColumn(BaseModel):
    """
    The catalog column represents a data column.
    This should be used to represent a column in a table or a view.
    """

    name: str
    data_type: str
    precision: Optional[int] = None
    scale: Optional[int] = None
    description: Optional[str] = None
    is_nullable: Optional[bool] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    tags: Optional[List[str]] = None
