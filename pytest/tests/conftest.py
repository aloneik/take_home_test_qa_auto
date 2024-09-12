import pytest
import requests

from typing import List
from lxml import etree

from tests.utils.programming_language_popularity import (
    ProgrammingLanguagePopularity,
    cell_to_string,
    get_popularity,
)


TARGET_PAGE_URL = (
    "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
)


@pytest.fixture(scope="session")
def programming_language_popularity() -> List[ProgrammingLanguagePopularity]:
    page = requests.get(TARGET_PAGE_URL)
    tree = etree.fromstring(page.text, etree.HTMLParser())
    table = tree.xpath("//table[contains(@class,'wikitable')]/tbody")[0]
    rows = table.getchildren()

    programming_language_popularity: List[ProgrammingLanguagePopularity] = []

    website_col = 0
    popularity_col = 1
    frontend_tech_col = 2
    backtend_tech_col = 3
    database_col = 4
    note_col = 5

    # The first row is headers
    for row in rows[1:]:
        columns = row.getchildren()

        popularity_table_row = ProgrammingLanguagePopularity(
            website=cell_to_string(columns[website_col]),
            popularity=get_popularity(columns[popularity_col]),
            frontend=cell_to_string(columns[frontend_tech_col]).split(","),
            backend=cell_to_string(columns[backtend_tech_col]).split(","),
            database=cell_to_string(columns[database_col]).split(","),
            notes=cell_to_string(columns[note_col]),
        )

        programming_language_popularity.append(popularity_table_row)

    return programming_language_popularity
