import datetime

# Имитация базы данных в оперативной памяти (список словарей)
documents = []


def add_document(doc_list: list, title: str, category: str, family: str, access_level: str) -> None:
    """
    Добавляет новый документ в список.
    Выполняет преобразование типов и создает словарь.
    """
    doc_id = len(doc_list) + 1
    # Преобразование типов: приводим дату к строке
    date_added = str(datetime.date.today()) 
    
    new_doc = {
        "id": doc_id,
        "title": title,
        "category": category,
        "family": family,
        "access": access_level,
        "date_added": date_added
    }
    doc_list.append(new_doc)
    print(f"✅ Документ '{title}' добавлен в архив семьи {family}.")


def show_all_documents(doc_list: list) -> None:
    """
    Выводит все документы из списка.
    Использует условную конструкцию для проверки на пустоту.
    """
    if not doc_list:
        print("📭 Список документов пуст.")
        return

    print("\n--- 📂 Все документы ---")
    for doc in doc_list:
        print(f"ID: {doc['id']} | {doc['title']} | Категория: {doc['category']} | "
              f"Семья: {doc['family']} | Доступ: {doc['access']}")


def find_documents_by_access(doc_list: list, search_access: str) -> None:
    """
    Ищет документы по уровню доступа.
    Использует цикл и условия для фильтрации.
    """
    found_docs = []
    for doc in doc_list:
        # Приводим к нижнему регистру для удобства поиска
        if doc["access"].lower() == search_access.lower():
            found_docs.append(doc)

    if found_docs:
        print(f"\n🔍 Найдены документы с уровнем доступа '{search_access}':")
        for doc in found_docs:
            print(f"  - {doc['title']} (Семья: {doc['family']})")
    else:
        print(f"\n❌ Документы с уровнем доступа '{search_access}' не найдены.")


# Основной сценарий выполнения программы
if __name__ == "__main__":
    print("Добро пожаловать в FamilyVault!")

    # 1. Добавляем документы
    add_document(documents, "Паспорт РФ", "Личные документы", "Ивановы", "Приватный")
    add_document(documents, "Свидетельство о браке", "Семейные документы", "Ивановы", "Для всех")
    add_document(documents, "Диплом о высшем образовании", "Образование", "Петровы", "Приватный")

    # 2. Показываем все документы
    show_all_documents(documents)

    # 3. Ищем документы по уровню доступа
    find_documents_by_access(documents, "Приватный")
    find_documents_by_access(documents, "Для всех")