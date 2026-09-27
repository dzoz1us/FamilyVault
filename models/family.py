class Family:
    """Семья, владеющая документами."""

    def __init__(self, family_id: int, name: str) -> None:
        """Создать объект семьи."""
        self.id = family_id
        self.name = name

    def __str__(self) -> str:
        """Строковое представление семьи."""
        return f"Семья: {self.name}"

    @classmethod
    def from_data(cls, data: dict) -> "Family":
        """Создать объект семьи из словаря JSON."""
        return cls(
            family_id=data["id"],
            name=data["name"]
        )

    def to_dict(self) -> dict:
        """Преобразовать объект в словарь для JSON."""
        return {
            "id": self.id,
            "name": self.name
        }
