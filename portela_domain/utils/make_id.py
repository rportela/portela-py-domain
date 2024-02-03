from portela_domain.models.CountryCode import CountryCode
from portela_domain.models.OrganizationType import OrganizationType


def make_organization_id(
    country: CountryCode, org_type: OrganizationType, name: str
) -> str:
    return f"{country.value}_{org_type.value}_{name.lower().replace(' ', '-')}"


def make_dataset_id(organization_id: str, name: str) -> str:
    return f"{organization_id}__{name.lower().replace(' ', '-')}"


def make_table_id(dataset_id: str, name: str) -> str:
    return f"{dataset_id}__{name.lower().replace(' ', '-')}"


def make_column_id(table_id: str, name: str) -> str:
    return f"{table_id}__{name.lower().replace(' ', '-')}"
