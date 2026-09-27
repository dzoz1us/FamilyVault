from documents import (
    add_document,
    find_documents_by_access,
    get_document_status
)
from storage import save_data, load_data

DATA_FILE = 'data/documents.json'


def main() -> None:
    """Основная функция запуска приложения."""
    documents = load_data(DATA_FILE)

    while True:
        print("\n--- 📂 FamilyVault ---")
        print("1. Добавить документ")
        print("2. Показать все документы")
        print("3. Найти по уровню доступа")
        print("4. Проверить статус документа")
        print("5. Сохранить и выйти")

        choice = input("Выберите действие: ")

        try:
            if choice == '1':
                title = input("Название документа: ")
                category = input("Категория: ")
                family = input("Семья: ")
                access = input("Уровень доступа (Приватный/Для всех): ")
                new_doc = add_document(
                    documents, title, category, family, access
                )
                print(f"✅ Добавлен документ ID: {new_doc['id']}")

            elif choice == '2':
                if not documents:
                    print("📭 Список документов пуст.")
                else:
                    print("\n--- Все документы ---")
                    for doc in documents:
                        print(
                            f"ID: {doc['id']} | {doc['title']} | "
                            f"Семья: {doc['family']} | Доступ: {doc['access']}"
                        )

            elif choice == '3':
                acc = input("Введите уровень доступа: ")
                found = find_documents_by_access(documents, acc)
                if found:
                    print(f"\n🔍 Найдено документов: {len(found)}")
                    for doc in found:
                        print(f"  - {doc['title']} (Семья: {doc['family']})")
                else:
                    print("❌ Ничего не найдено.")

            elif choice == '4':
                doc_id = int(input("Введите ID документа: "))
                status = get_document_status(doc_id, documents)
                print(status)

            elif choice == '5':
                save_data(documents, DATA_FILE)
                print("💾 Данные сохранены. До свидания!")
                break
            else:
                print("⚠️ Неверный выбор. Попробуйте снова.")

        except ValueError as e:
            print(f"❌ Ошибка ввода: {e}")
        except Exception as e:
            print(f"❌ Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
