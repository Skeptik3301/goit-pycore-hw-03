from datetime import datetime  

def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - date_obj
        return delta.days
    except ValueError:
        print("Помилка: неправильний формат дати. Використовуйте формат YYYY-MM-DD.")
        return None

print(get_days_from_today("2025-10-20"))
