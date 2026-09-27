from typing import List
from models.document import Document
from models.family import Family
from models.category import Category
from models.access import Access
from utils import get_current_date


def add_document(
    documents: List[Document],
    title: str,
    family: Family,
    category: Category,
    access: Access
) -> Document:
    """Создаёт объект Document и добавляет его в коллекцию."""
    if not title:
        raise ValueError("Название не может быть пустым.")

    doc_id = max([doc.id for doc in documents], default=0) + 1

    new_doc = Document(
        doc_id=doc_id,
        title=title,
        family=family,
        category=category,
        access=access,
        date_added=get_current_date()
    )
    documents.append(new_doc)
    return new_doc


def find_documents_by_access(
    documents: List[Document],
    search_access: str
) -> List[Document]:
    """Ищет документы по уровню доступа."""
    return (
        [doc for doc in documents
         if doc.access.level.lower() == search_access.lower()]
    )


def get_document_status(doc_id: int, documents: List[Document]) -> str:
    """Возвращает статус документа по его ID."""
    for doc in documents:
        if doc.id == doc_id:
            return (
                f"Документ '{doc.title}' доступен."
                f"Уровень доступа: {doc.access.level}"
            )
    return "Документ не найден."
