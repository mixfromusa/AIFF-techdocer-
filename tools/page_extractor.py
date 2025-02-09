import requests
import os
from pathlib import Path
import json
import time
from bs4 import BeautifulSoup
import logging
from datetime import datetime

class PageExtractor:
    def __init__(self, base_url=None, output_dir="extracted_pages"):
        """
        Инициализация экстрактора страниц
        :param base_url: Базовый URL документации
        :param output_dir: Директория для сохранения страниц
        """
        self.base_url = base_url or "https://www.jetbrains.com/help/writerside"
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Настройка логирования
        self.setup_logging()
        
        # Файл с состоянием
        self.state_file = self.output_dir / "extractor_state.json"
        self.load_state()

    def setup_logging(self):
        """Настройка логирования"""
        log_file = self.output_dir / "extractor.log"
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def load_state(self):
        """Загрузка состояния экстрактора"""
        if self.state_file.exists():
            with open(self.state_file, 'r') as f:
                self.state = json.load(f)
        else:
            self.state = {
                "last_page": None,
                "extracted_pages": [],
                "last_run": None
            }
            self.save_state()

    def save_state(self):
        """Сохранение состояния экстрактора"""
        self.state["last_run"] = datetime.now().isoformat()
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)

    def extract_page(self, page_url):
        """
        Извлечение конкретной страницы
        :param page_url: URL страницы для извлечения
        :return: (bool, str) - (успех операции, имя файла или сообщение об ошибке)
        """
        try:
            self.logger.info(f"Извлечение страницы: {page_url}")
            
            # Получаем страницу
            response = requests.get(page_url)
            response.raise_for_status()
            
            # Парсим HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Извлекаем основной контент
            content = self.extract_content(soup)
            
            # Генерируем имя файла из URL
            file_name = self.generate_filename(page_url)
            output_file = self.output_dir / file_name
            
            # Сохраняем в Markdown
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Обновляем состояние
            self.state["last_page"] = page_url
            self.state["extracted_pages"].append({
                "url": page_url,
                "file": str(file_name),
                "timestamp": datetime.now().isoformat()
            })
            self.save_state()
            
            self.logger.info(f"Страница сохранена в: {file_name}")
            return True, file_name
            
        except Exception as e:
            error_msg = f"Ошибка при извлечении страницы {page_url}: {str(e)}"
            self.logger.error(error_msg)
            return False, error_msg

    def extract_content(self, soup):
        """
        Извлечение и форматирование контента страницы
        :param soup: BeautifulSoup объект страницы
        :return: str - отформатированный Markdown контент
        """
        # Находим основной контент
        main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='content')
        
        if not main_content:
            raise ValueError("Не удалось найти основной контент страницы")
        
        # Извлекаем заголовок
        title = soup.find('h1')
        title_text = title.get_text() if title else "Без заголовка"
        
        # Формируем Markdown
        markdown = f"# {title_text}\n\n"
        
        # Добавляем метаданные
        markdown += "## Метаданные\n"
        markdown += f"- Источник: {self.base_url}\n"
        markdown += f"- Дата извлечения: {datetime.now().isoformat()}\n\n"
        
        # Конвертируем основной контент
        markdown += self.html_to_markdown(main_content)
        
        return markdown

    def html_to_markdown(self, element):
        """
        Конвертация HTML в Markdown
        :param element: BeautifulSoup элемент
        :return: str - Markdown текст
        """
        # Здесь должна быть логика конвертации HTML в Markdown
        # Для демонстрации возвращаем просто текст
        return element.get_text()

    def generate_filename(self, url):
        """
        Генерация имени файла из URL
        :param url: URL страницы
        :return: str - имя файла
        """
        # Убираем базовый URL и расширение
        name = url.replace(self.base_url, '').strip('/')
        # Заменяем специальные символы
        name = name.replace('/', '_').replace('\\', '_')
        # Добавляем расширение
        return f"{name}.md"

def main():
    """
    Пример использования:
    python page_extractor.py https://www.jetbrains.com/help/writerside/discover-writerside.html
    """
    import sys
    
    # Получаем URL из аргументов командной строки или используем тестовый URL
    url = sys.argv[1] if len(sys.argv) > 1 else "https://www.jetbrains.com/help/writerside/discover-writerside.html"
    
    extractor = PageExtractor()
    success, result = extractor.extract_page(url)
    
    if success:
        print(f"Страница успешно извлечена и сохранена в: {result}")
    else:
        print(f"Ошибка: {result}")

if __name__ == "__main__":
    main()