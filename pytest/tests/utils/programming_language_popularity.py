import re

from dataclasses import dataclass
from typing import List
from lxml import etree


@dataclass()
class ProgrammingLanguagePopularity:
    website: str
    popularity: int
    frontend: List[str]
    backend: List[str]
    database: List[str]
    notes: str

    def __str__(self) -> str:
        return (
            f"{self.website} "
            f"(Frontend:{','.join(self.frontend)}|"
            f"Backend:{','.join(self.backend)})"
            f" has {self.popularity} "
            f"unique visitors per month."
        )


def cell_to_string(element: etree.Element) -> str:
    texts = list(map(lambda x: x.strip(), element.itertext()))
    text = "".join(texts).strip()
    return re.sub(r"\[\d+\]|\n", "", text)


# Expects popularity in the following formats: 1,000,000; 1.000.000. Extracts only the number
def get_popularity(popularity_cell: etree.Element) -> int:
    text = cell_to_string(popularity_cell).replace(",", "").replace(".", "")
    if " " in text:
        text = text.split(" ")[0]
    popularity = int(text)
    return popularity
