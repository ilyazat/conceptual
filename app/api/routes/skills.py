from fastapi import APIRouter, status

from app.models.skills import SkillList, SkillsImportConfig, SkillsListImport

router = APIRouter(prefix="/skills")


@router.get("/")
async def get_skills():
    """
    Return list of the available skills
    Returns:
        SkillList: list of the available for user skill
    """
    return {"name": "foo"}


@router.post("/import", status_code=status.HTTP_201_CREATED)
async def import_skills(imports: SkillsListImport, config: SkillsImportConfig):
    """
    Import custom skills
    Args:
        imports: list of importing skills
        config: config for setting up importing skills
    """
    return f"{imports=} & {config=}"


@router.put("/update/{item_id}", status_code=status.HTTP_201_CREATED)
async def update_skill(item_id: str, description):
    return f"Description of the {item_id} was replaced by the {description=}"
