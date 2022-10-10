import json
from pathlib import Path
from typing import Optional

from app.db import get_database
from app.dreamworks.const import (
    ANNOTATOR_DIR_NAME,
    ASSISTANT_DISTS_DIR_NAME,
    SKILLS_DIR_NAME,
)


class DreamComponent:
    components = {
        "annotator": ANNOTATOR_DIR_NAME,
        "assistant": ASSISTANT_DISTS_DIR_NAME,
        "skills": SKILLS_DIR_NAME,
    }

    def __init__(self, dream_root: Optional[Path, str]) -> None:
        """
        Args:
            dream_root: path to Dream module
        """
        self.dream_root = (
            dream_root if isinstance(dream_root, Path) else Path(dream_root)
        )

    def get_list(self, component_name: str, to_json: bool = False) -> Optional[list, str]:
        """
        Fetch list of all items in the package in Dream Component

        Args:
            component_name: name of the component, i.e. 'annotator', 'assistant'
            to_json: if True method returns json string

        Returns:
            list_of_packages_in_component: list or json string of packages in Dream package
        """

        component_path: Path = self.dream_root / self.__class__.components[component_name]
        list_of_packages_in_component = []

        for item in component_path.iterdir():
            list_of_packages_in_component.append(item.name)

        if to_json:
            list_of_packages_in_component = json.dumps({component_name: list_of_packages_in_component})

        return list_of_packages_in_component

    def load_to_db(self) -> None:
        """
        Loads packages of component to MongoDB
        """
        db = get_database()

        for component in self.__class__.components:
            items = self.get_list(component)

            for item in items:
                await getattr(db, component).insert_one({"id": None, "name": item})
