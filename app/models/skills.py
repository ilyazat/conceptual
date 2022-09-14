from pydantic import BaseModel


class SkillItem(BaseModel):
    id: str
    name: str


class SkillList(BaseModel):
    items: list[SkillItem]


class SkillsListImport(SkillList):
    name: str


class SkillsImportConfig(BaseModel):
    path: str
