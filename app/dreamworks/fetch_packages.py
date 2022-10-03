import json
from pathlib import Path
from typing import Optional

from app.dreamworks.const import (
    ANNOTATOR_DIR_NAME,
    ASSISTANT_DISTS_DIR_NAME,
    SKILLS_DIR_NAME,
)


class PackagesList:
    packages = {
        "annotator": ANNOTATOR_DIR_NAME,
        "assistant": ASSISTANT_DISTS_DIR_NAME,
        "skills": SKILLS_DIR_NAME,
    }

    def __init__(self, dream_root: Optional[Path, str]) -> None:
        self.dream_root = (
            dream_root if isinstance(dream_root, Path) else Path(dream_root)
        )

    def get_list(self, package: str, to_json: bool = False) -> Optional[list, str]:
        """
        Fetch list of all items in the package in Dream

        Args:
            package: name of the package, i.e. 'annotator', 'assistant'
            to_json: if True method returns json string

        Returns:
            list_of_packages: python list or json string of packages in Dream package
        """

        package_path: Path = self.dream_root / self.__class__.packages[package]
        list_of_packages = []

        for item in package_path.iterdir():
            list_of_packages.append(item.name)

        if to_json:
            list_of_packages = json.dumps({package: list_of_packages})

        return list_of_packages
