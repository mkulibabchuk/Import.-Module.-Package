from salary import calculate_salary
from people import get_employees

import datetime

def main():
    # Вывод текущей даты
    print(f"Текущая дата: {datetime.datetime.now().date()}")
    
    # Вызываем функции
    calculate_salary()
    get_employees()

if __name__ == "__main__":
    main()