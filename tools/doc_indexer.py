import os
import re
from pathlib import Path
import json

class DocIndexer:
    def __init__(self, root_dir="."):
        self.root_dir = Path(root_dir)
        self.index = {
            "documents": [],
            "categories": {},
            "translations": {}
        }
    
    def scan_documents(self):
        """Сканирование документов в директории"""
        for path in self.root_dir.rglob("*.md"):
            if path.is_file():
                doc_info = self._analyze_document(path)
                self.index["documents"].append(doc_info)
                
                # Категоризация
                category = path.parent.name
                if category not in self.index["categories"]:
                    self.index["categories"][category] = []
                self.index["categories"][category].append(doc_info)
                
                # Поиск переводов
                self._find_translations(path)
    
    def _analyze_document(self, path):
        """Анализ отдельного документа"""
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Извлечение заголовка
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else path.stem
        
        # Извлечение подзаголовков
        headers = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)
        
        return {
            "path": str(path.relative_to(self.root_dir)),
            "title": title,
            "sections": headers,
            "modified": os.path.getmtime(path),
            "size": os.path.getsize(path)
        }
    
    def _find_translations(self, path):
        """Поиск переводов документа"""
        base_name = path.stem
        if base_name.endswith('_ru'):
            original = path.with_name(base_name[:-3] + path.suffix)
            if original.exists():
                self.index["translations"][str(original)] = str(path)
    
    def generate_navigation(self, output_file="navigation.md"):
        """Генерация файла навигации"""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Навигация по документации\n\n")
            
            # Категории
            for category, docs in self.index["categories"].items():
                f.write(f"## {category}\n\n")
                for doc in sorted(docs, key=lambda x: x["title"]):
                    f.write(f"- [{doc['title']}]({doc['path']})\n")
                    for section in doc["sections"]:
                        f.write(f"  - {section}\n")
                f.write("\n")
            
            # Переводы
            if self.index["translations"]:
                f.write("## Переводы\n\n")
                for orig, trans in self.index["translations"].items():
                    f.write(f"- {orig} → {trans}\n")
    
    def save_index(self, output_file="doc_index.json"):
        """Сохранение индекса в JSON"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.index, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    indexer = DocIndexer()
    indexer.scan_documents()
    indexer.generate_navigation()
    indexer.save_index()