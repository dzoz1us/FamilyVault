import datetime


# Возвращает текущую дату в формате ГГГГ-ММ-ДД
def get_current_date() -> str:
    return str(datetime.date.today())
