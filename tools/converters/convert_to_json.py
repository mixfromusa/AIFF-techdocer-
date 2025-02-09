import json
import os
import argparse
import glob
import json

# Константы
DEFAULT_INPUT_PATH = "."
DEFAULT_INPUT_PATTERN = "digest-list.md"
DEFAULT_OUTPUT_NAME = "digest-list.json"

def find_input_file(input_path, pattern):
    # Если input_path не указан, используем текущую директорию
    if input_path is None:
        input_path = "."

    # Если input_path — это директория
    if os.path.isdir(input_path):
        files = glob.glob(os.path.join(input_path, pattern))
        if not files:
            print(f"Error: Input file does not exist. Expected pattern: {pattern}")
            exit(1)
        return files[0]  # Берем первый найденный файл

    # Если input_path — это конкретный файл
    if os.path.isfile(input_path):
        return input_path

    # Если ничего не найдено
    print(f"Error: Input file does not exist. Expected pattern: {pattern}")
    exit(1)

def determine_output_path(output_path, input_path, default_name):
    # Если output_path не указан, сохраняем в той же директории, что и input_path
    if output_path is None or output_path == "same":
        if os.path.isdir(input_path):
            return os.path.join(input_path, default_name)
        return os.path.join(os.path.dirname(input_path), default_name)

    # Если output_path — это директория
    if os.path.isdir(output_path):
        return os.path.join(output_path, default_name)

    # Если output_path — это конкретный файл
    return output_path

import json
import re
from typing import Dict, Union

def parse_digest_list(filepath: str) -> str:
    """
    Парсит файл digest-list, который содержит хеши и пути к файлам.
    Формат строки в файле: "<hash> <filepath>"
    
    Args:
        filepath (str): Путь к файлу digest-list

    Returns:
        str: JSON строка с распарсенными данными
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            
        # Словарь для хранения результатов
        digest_data = {
            "files": {},
            "status": "success"
        }
        
        # Парсим каждую строку
        for line in content.split('\n'):
            line = line.strip()
            if not line:  # Пропускаем пустые строки
                continue
                
            # Используем регулярное выражение для разделения хеша и пути
            # Предполагаем, что хеш и путь разделены одним или несколькими пробелами
            match = re.match(r'^(\S+)\s+(.+)$', line)
            
            if match:
                hash_value, file_path = match.groups()
                digest_data["files"][file_path] = {
                    "hash": hash_value
                }
            
        return json.dumps(digest_data, indent=4, ensure_ascii=False)
        
    except Exception as e:
        error_response = {
            "error": str(e),
            "filename": filepath,
            "status": "error"
        }
        return json.dumps(error_response, indent=4, ensure_ascii=False)

# Пример использования
if __name__ == "__main__":
    # Пример содержимого digest-list файла:
    example_content = """
    5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 /path/to/file1.txt
    a123f45e78901b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2 /path/to/file2.jpg
    """
    
    # Создаем временный файл для тестирования
    with open("test_digest.txt", "w", encoding='utf-8') as f:
        f.write(example_content)
    
    # Парсим файл
    result = parse_digest_list("test_digest.txt")
    print(result)
def main():
    # Инициализация парсера аргументов командной строки
    parser = argparse.ArgumentParser(description="Convert digest-list file to JSON format.")
    parser.add_argument(
        "--input_path", "--ip", "--if", "--in", "--input",
        type=str,
        default=None,
        help="Path to the input file or directory. If not specified, the current directory is used."
    )
    parser.add_argument(
        "--output_path", "--op", "--of", "--out", "--output",
        type=str,
        default="same",
        help="Path to the output file or directory. If 'same', saves to the same directory as the input file."
    )

    args = parser.parse_args()

    # Определяем путь к входному файлу
    input_file = find_input_file(args.input_path, DEFAULT_INPUT_PATTERN)
    # Определяем путь к выходному файлу
    output_file = determine_output_path(args.output_path, input_file, DEFAULT_OUTPUT_NAME)
    # Преобразование файла в JSON
    parsed_data = parse_file_to_json(input_file)

    # Сохранение результата в JSON
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(parsed_data, json_file, indent=4, ensure_ascii=False)

    print(f"Файл успешно преобразован в JSON и сохранен как {output_file}.")

if __name__ == "__main__":
    main()
