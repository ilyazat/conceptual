from pydantic import BaseModel


class DistributionItem(BaseModel):
    id: str
    name: str


class DistributionList(BaseModel):
    items: list[DistributionItem]


class DistributionListImport(DistributionList):
    name: str


class DistributionImportConfig(BaseModel):
    path: str
