from typing import List, Dict
from collections import defaultdict
import sys
import io

# Устанавливаем кодировку UTF-8 для вывода
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def parse_digest_list(content: str):
    # Инициализация переменных
    current_buffer: List[str] = []  # Буфер для текущих 5 строк
    records: List[Dict] = []  # Список всех записей
    current_category = None  # Текущая категория
    categories_count = defaultdict(int)  # Счетчик элементов по категориям
    no_category_count = 0  # Счетчик элементов без категории

    # Разбиваем текст на строки
    lines = content.split('\n')
    
    for line in lines:
        line = line.strip()
        
        # Если строка пустая и есть данные в буфере
        if not line and current_buffer:
            # Создаем запись из буфера
            record = process_buffer(current_buffer)
            if record:
                records.append(record)
                # Подсчитываем категории
                if record.get('category'):
                    categories_count[record['category']] += 1
                else:
                    no_category_count += 1
            # Очищаем буфер
            current_buffer = []
        elif line:  # Если строка не пустая
            # Добавляем строку в буфер
            current_buffer.append(line)
            if len(current_buffer) > 5:  # Держим только последние 5 строк
                current_buffer.pop(0)

    # Обрабатываем последний буфер, если он не пустой
    if current_buffer:
        record = process_buffer(current_buffer)
        if record:
            records.append(record)
            if record.get('category'):
                categories_count[record['category']] += 1
            else:
                no_category_count += 1

    return {
        'categories': dict(categories_count),
        'no_category': no_category_count,
        'total_records': len(records)
    }

def process_buffer(buffer: List[str]) -> Dict:
    """Обрабатывает буфер строк и создает запись"""
    if not buffer:
        return None

    record = {
        'raw_data': buffer,
        'category': None,
        'name': None,
        'date': None,
        'description': None
    }

    # Ищем категорию (строка с эмодзи и "view | remove from digest")
    for line in buffer:
        if '(view | remove from digest)' in line:
            category = line.split('(')[0].strip()
            record['category'] = category
            break

    # Ищем имя и дату
    for line in buffer:
        if '—' in line:  # Строка с датой и именем
            parts = line.split('—')
            record['date'] = parts[0].strip()
            record['name'] = parts[1].strip()
            break

    # Последняя непустая строка обычно описание
    for line in reversed(buffer):
        if line and not line.endswith('(Mini tool)'):
            record['description'] = line
            break

    return record

# Читаем файл и анализируем его
with open('converters/digest-list.md', 'r', encoding='utf-8') as file:
    content = file.read()

result = parse_digest_list(content)

# Выводим результаты
print("\nКоличество элементов по категориям:")
for category, count in sorted(result['categories'].items()):
    print(f"{category}: {count}")

print(f"\nЭлементов без категории: {result['no_category']}")
print(f"Всего записей: {result['total_records']}")