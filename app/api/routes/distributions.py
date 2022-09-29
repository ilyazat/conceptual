from fastapi import APIRouter
from fastapi import status
from app.models.distributions import (
    DistributionList,
    DistributionListImport,
    DistributionImportConfig,
)

router = APIRouter(prefix="/distribution")


@router.get("/")
async def get_distribution():
    """
    Return list of the available distribution
    Returns:
        SkillList: list of the available for user skill
    """
    return {"name": "foo"}


@router.post("/import", status_code=status.HTTP_201_CREATED)
async def import_distribution(
    imports: DistributionListImport, config: DistributionImportConfig
):
    """
    Import custom distribution
    Args:
        imports: list of importing distributions
        config: config for setting up importing distributions
    """
    print(f"{imports=} & {config=}")


@router.put("/update/{item_id}", status_code=status.HTTP_201_CREATED)
async def update_distribution(item_id: str, description):
    return f"Description of the {item_id} was replaced by the {description=}"
