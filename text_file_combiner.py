import os
import hashlib
from pathlib import Path
from typing import List, Dict, Set, Tuple
import difflib
import math
import time

# Константы
MAX_SOURCE_FILE_SIZE = 50 * 1024  # 50 KB
MAX_RESULT_FILE_SIZE = 50 * 1024 * 1024  # 50 MB
MAX_TOKENS_PER_FILE = 1000
SIMILARITY_THRESHOLD = 0.8  # 80% схожести (различия менее 20%)
SUBSET_THRESHOLD = 0.9  # 90% для определения подмножества

# Расширения текстовых файлов
TEXT_EXTENSIONS = {
    '.txt', '.log', '.md', '.py', '.js', '.html', '.css', '.json',
    '.xml', '.yaml', '.yml', '.ini', '.cfg', '.conf', '.sh', '.bat',
    '.cmd', '.ps1', '.java', '.cpp', '.c', '.h', '.hpp', '.cs',
    '.php', '.rb', '.pl', '.sql', '.tsx', '.jsx', '.ts'
}

# Игнорируемые директории
IGNORED_DIRS = {
    'CID', 'node_modules', 'dist', 'build', '.git', '.idea', '.vscode',
    'bin', 'obj', '__pycache__'
}

def calculate_similarity_hash(content: str) -> str:
    """Создает хеш для проверки схожести содержимого"""
    # Используем simhash-подобный подход для нечеткого сравнения
    words = content.split()
    if not words:
        return hashlib.md5(content.encode()).hexdigest()
    
    # Берем каждое третье слово для ускорения сравнения
    sample = ' '.join(words[::3])
    return hashlib.md5(sample.encode()).hexdigest()

def are_files_similar(content1: str, content2: str) -> bool:
    """Проверяет схожесть двух файлов"""
    similarity = difflib.SequenceMatcher(None, content1, content2).ratio()
    return similarity > SIMILARITY_THRESHOLD

def is_subset(smaller: str, larger: str) -> bool:
    """Проверяет, является ли один текст подмножеством другого"""
    words_smaller = set(smaller.split())
    words_larger = set(larger.split())
    
    if not words_smaller:
        return False
        
    common_words = words_smaller.intersection(words_larger)
    similarity_ratio = len(common_words) / len(words_smaller)
    return similarity_ratio > SUBSET_THRESHOLD

class TextFileCombiner:
    def __init__(self, source_dir: str, output_dir: str):
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.processed_files: Set[str] = set()
        self.file_mapping: Dict[str, List[Tuple[str, int, int]]] = {}
        self.current_file_number = 1
        self.current_content: List[str] = []
        self.current_line_count = 0
        self.total_files = 0
        self.processed_count = 0
        self.start_time = time.time()

    def should_ignore_dir(self, dir_path: Path) -> bool:
        """Проверяет, нужно ли игнорировать директорию"""
        return any(ignored in str(dir_path) for ignored in IGNORED_DIRS)

    def is_text_file(self, file_path: Path) -> bool:
        """Проверяет, является ли файл текстовым"""
        return file_path.suffix.lower() in TEXT_EXTENSIONS

    def format_content(self, file_path: Path, content: str) -> str:
        """Форматирует содержимое файла для markdown"""
        ext = file_path.suffix.lower()[1:]  # убираем точку
        if ext in ['md', 'txt', 'log']:
            return f"\n## {file_path}\n\n{content}\n"
        else:
            return f"\n## {file_path}\n\n```{ext}\n{content}\n```\n"

    def write_current_batch(self):
        """Записывает текущую партию файлов"""
        if not self.current_content:
            return

        output_file = self.output_dir / f"combined_{self.current_file_number:04d}.md"
        content = "".join(self.current_content)
        
        # Добавляем метаданные
        metadata = f"""---
files_count: {len(self.current_content)}
similarity_hash: {calculate_similarity_hash(content)}
size_bytes: {len(content.encode('utf-8'))}
---

"""
        with output_file.open('w', encoding='utf-8') as f:
            f.write(metadata + content)

        print(f"Создан файл: {output_file} ({len(self.current_content)} файлов)")
        
        self.current_file_number += 1
        self.current_content = []
        self.current_line_count = 0

    def process_file(self, file_path: Path):
        """Обрабатывает один файл"""
        if file_path in self.processed_files:
            return

        try:
            if not file_path.is_file() or file_path.stat().st_size > MAX_SOURCE_FILE_SIZE:
                return

            with file_path.open('r', encoding='utf-8') as f:
                content = f.read()

            # Проверяем на дубликаты и подмножества
            for existing_content in self.current_content:
                if are_files_similar(content, existing_content) or \
                   is_subset(content, existing_content) or \
                   is_subset(existing_content, content):
                    return

            formatted_content = self.format_content(file_path, content)
            content_size = len(formatted_content.encode('utf-8'))
            
            # Проверяем, нужно ли начать новый файл
            if (self.current_line_count + formatted_content.count('\n') > MAX_TOKENS_PER_FILE or
                sum(len(c.encode('utf-8')) for c in self.current_content) + content_size > MAX_RESULT_FILE_SIZE):
                self.write_current_batch()

            start_line = self.current_line_count + 1
            self.current_content.append(formatted_content)
            self.current_line_count += formatted_content.count('\n')
            end_line = self.current_line_count

            # Сохраняем информацию для навигационного файла
            output_file = f"combined_{self.current_file_number:04d}.md"
            if output_file not in self.file_mapping:
                self.file_mapping[output_file] = []
            self.file_mapping[output_file].append((str(file_path), start_line, end_line))
            
            self.processed_files.add(file_path)
            
            # Обновляем прогресс
            self.processed_count += 1
            elapsed_time = time.time() - self.start_time
            if self.processed_count % 10 == 0:  # Показываем каждые 10 файлов
                print(f"Обработано файлов: {self.processed_count}/{self.total_files} "
                      f"({(self.processed_count/self.total_files*100):.1f}%) "
                      f"Прошло времени: {elapsed_time:.1f} сек")

        except (UnicodeDecodeError, PermissionError):
            # Пропускаем файлы, которые нельзя прочитать как текст
            pass

    def count_files(self):
        """Подсчитывает общее количество файлов для обработки"""
        count = 0
        for path in self.source_dir.rglob('*'):
            if path.is_file() and self.is_text_file(path) and not self.should_ignore_dir(path.parent):
                count += 1
        return count

    def process_directory(self):
        """Рекурсивно обрабатывает директорию"""
        print("Подсчет файлов...")
        self.total_files = self.count_files()
        print(f"Найдено файлов для обработки: {self.total_files}")
        
        print("Начинаем обработку файлов...")
        for path in self.source_dir.rglob('*'):
            if path.is_file() and self.is_text_file(path) and not self.should_ignore_dir(path.parent):
                self.process_file(path)

        # Записываем последнюю партию файлов
        if self.current_content:
            self.write_current_batch()

        # Создаем навигационный файл
        self.create_navigation_file()

    def create_navigation_file(self):
        """Создает навигационный файл"""
        navigation_content = "# Навигация по объединенным файлам\n\n"
        
        for output_file, file_entries in self.file_mapping.items():
            navigation_content += f"\n## {output_file}\n\n"
            for source_file, start_line, end_line in file_entries:
                navigation_content += f"- {source_file}\n  - Строки: {start_line}-{end_line}\n"

        nav_file = self.output_dir / "navigation.md"
        with nav_file.open('w', encoding='utf-8') as f:
            f.write(navigation_content)
        
        print(f"Создан навигационный файл: {nav_file}")

def main():
    # Текущая директория как источник
    source_dir = "."
    # Создаем поддиректорию для результатов
    output_dir = "./combined_output"
    
    print("Запуск обработки файлов...")
    start_time = time.time()
    
    combiner = TextFileCombiner(source_dir, output_dir)
    combiner.process_directory()
    
    elapsed_time = time.time() - start_time
    print(f"\nОбработка завершена за {elapsed_time:.1f} секунд")
    print(f"Обработано файлов: {combiner.processed_count}")
    print(f"Результаты сохранены в {output_dir}")

if __name__ == "__main__":
    main()