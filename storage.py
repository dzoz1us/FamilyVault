import json
import os
from typing import List
from models import Document, Family, Category, Access

DATA_DIR = "data"
FAMILIES_FILE = os.path.join(DATA_DIR, "families.json")
CATEGORIES_FILE = os.path.join(DATA_DIR, "categories.json")
ACCESSES_FILE = os.path.join(DATA_DIR, "accesses.json")
DOCUMENTS_FILE = os.path.join(DATA_DIR, "documents.json")


def _save_to_json(data: list, filename: str) -> None:
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def _load_from_json(filename: str) -> list:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_families(families: List[Family]) -> None:
    _save_to_json([f.to_dict() for f in families], FAMILIES_FILE)


def load_families() -> List[Family]:
    return [Family.from_data(item) for item in _load_from_json(FAMILIES_FILE)]


def save_categories(categories: List[Category]) -> None:
    _save_to_json([c.to_dict() for c in categories], CATEGORIES_FILE)


def load_categories() -> List[Category]:
    return ([Category.from_data(item) for
             item in _load_from_json(CATEGORIES_FILE)])


def save_accesses(accesses: List[Access]) -> None:
    _save_to_json([a.to_dict() for a in accesses], ACCESSES_FILE)


def load_accesses() -> List[Access]:
    return [Access.from_data(item) for item in _load_from_json(ACCESSES_FILE)]


def save_documents(documents: List[Document]) -> None:
    _save_to_json([d.to_dict() for d in documents], DOCUMENTS_FILE)


def load_documents(
    families: List[Family],
    categories: List[Category],
    accesses: List[Access]
) -> List[Document]:
    raw_data = _load_from_json(DOCUMENTS_FILE)
    documents = []
    for item in raw_data:
        try:
            doc = Document.from_data(item, families, categories, accesses)
            documents.append(doc)
        except ValueError as e:
            print(f"⚠️ Ошибка загрузки документа: {e}")
    return documents
