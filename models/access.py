class Access:
    """Уровень доступа к документу."""

    def __init__(self, access_id: int, level: str) -> None:
        self.id = access_id
        self.level = level

    def __str__(self) -> str:
        return f"Доступ: {self.level}"

    @classmethod
    def from_data(cls, data: dict) -> "Access":
        return cls(access_id=data["id"], level=data["level"])

    def to_dict(self) -> dict:
        return {"id": self.id, "level": self.level}
