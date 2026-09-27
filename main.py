from models import Family, Category, Access
from models.documents import (
    add_document, find_documents_by_access,
    get_document_status
)
from storage import (
    load_families, save_families,
    load_categories, save_categories,
    load_accesses, save_accesses,
    load_documents, save_documents
)


def init_reference_data():
    """Создает справочники, если они пусты."""
    families = load_families()
    if not families:
        families = [Family(1, "Ивановы"), Family(2, "Петровы")]
        save_families(families)

    categories = load_categories()
    if not categories:
        categories = [
            Category(1, "Личные документы"),
            Category(2, "Образование"),
            Category(3, "Медицина")
        ]
        save_categories(categories)

    accesses = load_accesses()
    if not accesses:
        accesses = [
            Access(1, "Приватный"),
            Access(2, "Для всех")
        ]
        save_accesses(accesses)

    return families, categories, accesses


def main() -> None:
    families, categories, accesses = init_reference_data()
    documents = load_documents(families, categories, accesses)

    while True:
        print("\n--- 📂 FamilyVault (ООП версия) ---")
        print("1. Добавить документ")
        print("2. Показать все документы")
        print("3. Найти по уровню доступа")
        print("4. Проверить статус документа")
        print("5. Сохранить и выйти")

        choice = input("Выберите действие: ")

        try:
            if choice == '1':
                title = input("Название документа: ")

                print("\nДоступные семьи:")
                for f in families:
                    print(f"  {f.id} - {f.name}")
                fam_id = int(input("Введите ID семьи: "))
                family = next((f for f in families if f.id == fam_id), None)

                print("\nДоступные категории:")
                for c in categories:
                    print(f"  {c.id} - {c.name}")
                cat_id = int(input("Введите ID категории: "))
                category = next(
                    (c for c in categories if c.id == cat_id), None)

                print("\nДоступные уровни доступа:")
                for a in accesses:
                    print(f"  {a.id} - {a.level}")
                acc_id = int(input("Введите ID доступа: "))
                access = next((a for a in accesses if a.id == acc_id), None)

                if not (family and category and access):
                    print("❌ Ошибка: неверно указаны ID.")
                    continue

                new_doc = add_document(
                    documents, title, family, category, access)
                print(f"✅ Добавлен: {new_doc}")

            elif choice == '2':
                if not documents:
                    print("📭 Список документов пуст.")
                else:
                    for doc in documents:
                        print(doc)

            elif choice == '3':
                acc_level = input(
                    "Введите уровень доступа (например, Приватный): ")
                found = find_documents_by_access(documents, acc_level)
                if found:
                    for doc in found:
                        print(f"  - {doc}")
                else:
                    print("❌ Ничего не найдено.")

            elif choice == '4':
                doc_id = int(input("Введите ID документа: "))
                print(get_document_status(doc_id, documents))

            elif choice == '5':
                save_documents(documents)
                print("💾 Данные сохранены. До свидания!")
                break

        except ValueError as e:
            print(f"❌ Ошибка ввода: {e}")
        except Exception as e:
            print(f"❌ Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
