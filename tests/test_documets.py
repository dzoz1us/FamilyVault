import pytest
from models import Family, Category, Access, Document
from models.documents import (
    add_document,
    find_documents_by_access,
    get_document_status
)


def test_document_creation():
    """Создание документа с объектами Family, Category, Access."""
    family = Family(1, "Ивановы")
    category = Category(1, "Личные документы")
    access = Access(1, "Приватный")

    doc = Document(
        doc_id=1,
        title="Паспорт",
        family=family,
        category=category,
        access=access,
        date_added="2026-09-27"
    )

    assert doc.id == 1
    assert doc.family.name == "Ивановы"
    assert doc.category.name == "Личные документы"
    assert doc.access.level == "Приватный"
    assert "Паспорт" in str(doc)


def test_change_access():
    """Изменение уровня доступа через объект Access."""
    family = Family(1, "Ивановы")
    category = Category(1, "Личные документы")
    access_private = Access(1, "Приватный")
    access_public = Access(2, "Для всех")

    doc = Document(1, "Паспорт", family, category, access_private, "2026-09-27")
    doc.change_access(access_public)

    assert doc.access.level == "Для всех"


def test_add_document():
    """Добавление документа в коллекцию."""
    family = Family(1, "Ивановы")
    category = Category(1, "Личные документы")
    access = Access(1, "Приватный")
    docs = []

    doc = add_document(docs, "Паспорт", family, category, access)

    assert len(docs) == 1
    assert doc.id == 1
    assert doc.family.name == "Ивановы"
    assert doc.category.name == "Личные документы"
    assert doc.access.level == "Приватный"


def test_add_document_empty_title_raises_error():
    """Пустое название должно вызывать ValueError."""
    family = Family(1, "Ивановы")
    category = Category(1, "Личные документы")
    access = Access(1, "Приватный")
    docs = []

    with pytest.raises(ValueError):
        add_document(docs, "", family, category, access)


def test_find_documents_by_access():
    """Поиск документов по уровню доступа."""
    family = Family(1, "Ивановы")
    category = Category(1, "Личные документы")
    access_private = Access(1, "Приватный")
    access_public = Access(2, "Для всех")

    docs = [
        Document(1, "A", family, category, access_private, "2026-09-27"),
        Document(2, "B", family, category, access_public, "2026-09-27"),
    ]

    result = find_documents_by_access(docs, "приватный")

    assert len(result) == 1
    assert result[0].title == "A"


def test_get_document_status():
    """Проверка статуса существующего и несуществующего документа."""
    family = Family(1, "Ивановы")
    category = Category(1, "Личные документы")
    access = Access(1, "Приватный")

    docs = [
        Document(1, "Паспорт", family, category, access, "2026-09-27"),
    ]

    status_found = get_document_status(1, docs)
    assert "Паспорт" in status_found
    assert "Приватный" in status_found

    status_missing = get_document_status(99, docs)
    assert status_missing == "Документ не найден."