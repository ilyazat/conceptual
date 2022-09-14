from pydantic import BaseModel


class AnnotatorItem(BaseModel):
    id: str
    name: str


class AnnotatorList(BaseModel):
    items: list[AnnotatorItem]


class AnnotatorListImport(AnnotatorList):
    name: str


class AnnotatorImportConfig(BaseModel):
    path: str
