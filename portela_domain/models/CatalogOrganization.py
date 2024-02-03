from typing import Optional

from pydantic import BaseModel

from .CountryCode import CountryCode
from .OrganizationType import OrganizationType


class CatalogOrganization(BaseModel):
    country: CountryCode
    org_type: OrganizationType
    name: str
    description: Optional[str] = None

    def make_id(self) -> str:
        return f"{self.country.value}_{self.org_type.value}_{self.name.lower().replace(' ', '-')}"
