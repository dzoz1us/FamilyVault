import pytest
from documents import (
    add_document,
    find_documents_by_access,
    get_document_status
)


def test_add_document():
    """Проверяет добавление документа."""
    docs = []
    doc = add_document(docs, "Паспорт", "Личное", "Ивановы", "Приватный")
    assert len(docs) == 1
    assert doc['title'] == "Паспорт"
    assert doc['id'] == 1
    assert doc['access'] == "Приватный"


def test_find_documents_by_access():
    """Проверяет поиск по уровню доступа."""
    docs = [
        {"id": 1, "title": "A", "access": "Приватный"},
        {"id": 2, "title": "B", "access": "Для всех"}
    ]
    result = find_documents_by_access(docs, "приватный")
    assert len(result) == 1
    assert result[0]["title"] == "A"


def test_get_document_status():
    """Проверяет получение статуса документа."""
    docs = [{"id": 1, "title": "Паспорт", "access": "Приватный"}]
    status = get_document_status(1, docs)
    assert "Паспорт" in status
    assert "Приватный" in status


def test_add_empty_document_raises_error():
    """Проверяет, что пустое название вызывает ошибку."""
    docs = []
    with pytest.raises(ValueError):
        add_document(docs, "", "Личное", "Ивановы", "Приватный")
