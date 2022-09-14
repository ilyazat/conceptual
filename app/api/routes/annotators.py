from fastapi import APIRouter
from fastapi import status
from app.models.annotators import AnnotatorList, AnnotatorListImport, AnnotatorImportConfig

router = APIRouter(prefix="/annotators")


@router.get("/", status_code=200)
async def get_annotators():
    """
    Return list of the available annotators
    Returns:
        AnnotatorList: list of the available for user annotator
    """
    return {"name": "foo"}


@router.post("/import", status_code=status.HTTP_201_CREATED)
async def import_annotators(imports: AnnotatorListImport, config: AnnotatorImportConfig):
    """
    Import custom annotators
    Args:
        imports: list of importing annotators
        config: config for setting up importing annotators
    """
    print(f'{imports=} & {config=}')


@router.put("/update/{item_id}", status_code=status.HTTP_201_CREATED)
async def update_annotator(item_id: str, description):
    return f"Description of the {item_id} was replaced by the {description=}"
