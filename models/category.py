class Category:
    """Категория документа."""

    def __init__(self, category_id: int, name: str) -> None:
        self.id = category_id
        self.name = name

    def __str__(self) -> str:
        return f"Категория: {self.name}"

    @classmethod
    def from_data(cls, data: dict) -> "Category":
        return cls(category_id=data["id"], name=data["name"])

    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name}
