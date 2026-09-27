from utils import get_current_date


def add_document(
    documents: list,
    title: str,
    category: str,
    family: str,
    access_level: str
) -> dict:
    """
    Добавляет новый документ в список.
    Возвращает созданный словарь документа.
    """
    if not title or not category:
        raise ValueError("Название и категория не могут быть пустыми.")

    # Генерация ID: находим максимальный существующий и прибавляем 1
    doc_id = max([doc['id'] for doc in documents], default=0) + 1

    new_doc = {
        "id": doc_id,
        "title": title,
        "category": category,
        "family": family,
        "access": access_level,
        "date_added": get_current_date()
    }
    documents.append(new_doc)
    return new_doc


def find_documents_by_access(documents: list, search_access: str) -> list:
    """
    Ищет документы по уровню доступа.
    Возвращает список найденных словарей.
    """
    return [
        doc for doc in documents
        if doc['access'].lower() == search_access.lower()
    ]


def get_document_status(doc_id: int, documents: list) -> str:
    """
    Возвращает статус документа по его ID.
    (Сохранена логика из ПР1, как требуется в задании).
    """
    for doc in documents:
        if doc['id'] == doc_id:
            return (
                f"Документ '{doc['title']}' доступен. "
                f"Уровень доступа: {doc['access']}"
            )
    return "Документ не найден."
