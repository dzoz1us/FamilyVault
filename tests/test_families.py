from models import Family


def test_family_creation():
    family = Family(1, "Ивановы")
    assert family.id == 1
    assert family.name == "Ивановы"
    assert str(family) == "Семья: Ивановы"
