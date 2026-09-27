from models.family import Family
from models.category import Category
from models.access import Access


class Document:
    """Документ, хранящийся в системе."""

    def __init__(
        self,
        doc_id: int,
        title: str,
        family: Family,
        category: Category,
        access: Access,
        date_added: str
    ) -> None:
        self.id = doc_id
        self.title = title
        self.family = family
        self.category = category
        self.access = access
        self.date_added = date_added

    def __str__(self) -> str:
        return (
            f"Документ '{self.title}' | Семья: {self.family.name} | "
            f"{self.category} | {self.access} | Дата: {self.date_added}"
        )

    def change_access(self, new_access: Access) -> None:
        """Изменить уровень доступа к документу."""
        self.access = new_access

    @classmethod
    def from_data(
        cls,
        data: dict,
        families: list[Family],
        categories: list[Category],
        accesses: list[Access]
    ) -> "Document":
        """Создать объект документа из словаря JSON."""
        family = next((f for f in families if f.id == data["family_id"]), None)
        category = next((c for c in categories if c.id ==
                        data["category_id"]), None)
        access = next((a for a in accesses if a.id == data["access_id"]), None)

        if not (family and category and access):
            raise ValueError("Не найдены связанные объекты для документа.")

        return cls(
            doc_id=data["id"],
            title=data["title"],
            family=family,
            category=category,
            access=access,
            date_added=data["date_added"]
        )

    def to_dict(self) -> dict:
        """Преобразовать объект в словарь для JSON."""
        return {
            "id": self.id,
            "title": self.title,
            "family_id": self.family.id,
            "category_id": self.category.id,
            "access_id": self.access.id,
            "date_added": self.date_added
        }
