from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder

from app.db import get_database
from app.models.annotators import (
    AnnotatorImportConfig,
    AnnotatorItem,
    AnnotatorList,
    AnnotatorListImport,
)

router = APIRouter(prefix="/annotators")


@router.get("/", status_code=200)
async def get_annotators():
    """
    Return list of the available annotators
    Returns:
        AnnotatorList: list of the available for user annotator
    """
    return {"name": "foo"}


@router.post("/", status_code=201)
async def add_one_annotator(annotator: AnnotatorItem, db=Depends(get_database)):
    last_id = await db.annotators.insert_one(jsonable_encoder(annotator))
    return {"description": "annotator has been successfully added"}


@router.get("/{item_id}")
async def get_annotators_by_id(item_id: str, db=Depends(get_database)):
    annotator = await db.annotators.find_one({"id": item_id})
    if annotator:
        return AnnotatorItem(**annotator)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Annotator wasn't found"
        )


@router.get("/test")
async def test(commons: int = Depends(get_database)):
    return commons


@router.post("/import", status_code=status.HTTP_201_CREATED)
async def import_annotators(
    imports: AnnotatorListImport, config: AnnotatorImportConfig
):
    """
    Import custom annotators
    Args:
        imports: list of importing annotators
        config: config for setting up importing annotators
    """
    print(f"{imports=} & {config=}")


@router.put("/update/{item_id}", status_code=status.HTTP_201_CREATED)
async def update_annotator(item_id: str, description):
    return f"Description of the {item_id} was replaced by the {description=}"
