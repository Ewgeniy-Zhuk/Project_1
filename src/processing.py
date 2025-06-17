from typing import List, Dict
from datetime import datetime


operations_filter_by_state = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Функция, которая принимает список словарей и опционально значение для ключа 'state',
    и возвращает новый список словарей.
    """
    return [item for item in data if item.get('state') == state]

print("Фильтрация по умолчанию (EXECUTED)")
print(filter_by_state(operations_filter_by_state))

print("\nФильтрация CANCELED")
print(filter_by_state(operations_filter_by_state, 'CANCELED'))



operations_sort_by_date = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
def sort_by_date(operations, reverse=True):
    sorted_operations = operations.copy()
    sorted_operations.sort(
        key=lambda x: datetime.fromisoformat(x['date']),
        reverse=reverse
    )

    return sorted_operations

print("\nСортировка по убыванию:")
print(sort_by_date(operations_sort_by_date))

print("\nСортировка по возрастанию:")
print(sort_by_date(operations_sort_by_date, reverse=False))


