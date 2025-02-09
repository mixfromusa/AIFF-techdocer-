import os
from pathlib import Path
import json
from datetime import datetime
import subprocess
from typing import Dict, List, Tuple

class ProjectAnalyzer:
    def __init__(self, root_dir: str = ".", history_file: str = "analysis_history.json"):
        self.root_dir = Path(root_dir)
        self.history_file = self.root_dir / ".meta" / "history" / history_file
        self.size_categories = {
            "small": (0, 3072),        # 0-3KB
            "medium": (3072, 10240),   # 3-10KB
            "large": (10240, float('inf'))  # >10KB
        }
        
    def analyze(self) -> Dict:
        """Анализ структуры проекта"""
        current_state = {
            "timestamp": datetime.now().isoformat(),
            "files": self._scan_files(),
            "summary": self._generate_summary()
        }
        
        self._save_history(current_state)
        return current_state
    
    def _scan_files(self) -> List[Dict]:
        """Сканирование файлов проекта"""
        files = []
        for path in self.root_dir.rglob("*"):
            if path.is_file() and not self._should_ignore(path):
                size = path.stat().st_size
                files.append({
                    "path": str(path.relative_to(self.root_dir)),
                    "size": size,
                    "category": self._get_size_category(size),
                    "extension": path.suffix.lower(),
                    "modified": datetime.fromtimestamp(path.stat().st_mtime).isoformat()
                })
        return files
    
    def _get_size_category(self, size: int) -> str:
        """Определение категории размера файла"""
        for category, (min_size, max_size) in self.size_categories.items():
            if min_size <= size < max_size:
                return category
        return "unknown"
    
    def _generate_summary(self) -> Dict:
        """Генерация сводной информации"""
        summary = {
            "total_files": 0,
            "by_size": {category: 0 for category in self.size_categories},
            "by_extension": {},
            "total_size": 0
        }
        
        for path in self.root_dir.rglob("*"):
            if path.is_file() and not self._should_ignore(path):
                size = path.stat().st_size
                ext = path.suffix.lower()
                
                summary["total_files"] += 1
                summary["total_size"] += size
                summary["by_size"][self._get_size_category(size)] += 1
                summary["by_extension"][ext] = summary["by_extension"].get(ext, 0) + 1
        
        return summary
    
    def _should_ignore(self, path: Path) -> bool:
        """Проверка, следует ли игнорировать файл"""
        ignore_patterns = [
            ".git",
            "__pycache__",
            ".idea",
            "venv",
            "node_modules"
        ]
        return any(pattern in str(path) for pattern in ignore_patterns)
    
    def _save_history(self, current_state: Dict):
        """Сохранение истории анализа"""
        self.history_file.parent.mkdir(parents=True, exist_ok=True)
        
        history = []
        if self.history_file.exists():
            with open(self.history_file, 'r') as f:
                history = json.load(f)
        
        history.append(current_state)
        
        with open(self.history_file, 'w') as f:
            json.dump(history, f, indent=2)
    
    @staticmethod
    def get_git_changes() -> Tuple[str, Dict]:
        """Получение изменений через Git"""
        try:
            # Получаем список измененных файлов
            changed_files = subprocess.check_output(
                ["git", "status", "--porcelain"],
                universal_newlines=True
            ).split("\n")
            
            # Получаем статистику изменений
            diff_stats = subprocess.check_output(
                ["git", "diff", "--stat"],
                universal_newlines=True
            )
            
            # Анализируем изменения
            changes = {
                "modified": [],
                "added": [],
                "deleted": [],
                "renamed": []
            }
            
            for file in changed_files:
                if not file:
                    continue
                status = file[:2]
                path = file[3:]
                
                if status == "M ":
                    changes["modified"].append(path)
                elif status == "A ":
                    changes["added"].append(path)
                elif status == "D ":
                    changes["deleted"].append(path)
                elif status == "R ":
                    changes["renamed"].append(path)
            
            return diff_stats, changes
            
        except subprocess.CalledProcessError:
            return "Git repository not found or error occurred", {}

def main():
    analyzer = ProjectAnalyzer()
    
    # Анализ проекта
    analysis = analyzer.analyze()
    
    # Вывод результатов
    print("\n=== Project Analysis ===")
    print(f"\nTotal files: {analysis['summary']['total_files']}")
    print(f"Total size: {analysis['summary']['total_size'] / 1024:.2f} KB")
    
    print("\nFiles by size category:")
    for category, count in analysis['summary']['by_size'].items():
        print(f"- {category}: {count}")
    
    print("\nFiles by extension:")
    for ext, count in analysis['summary']['by_extension'].items():
        print(f"- {ext}: {count}")
    
    # Получение изменений Git
    diff_stats, changes = ProjectAnalyzer.get_git_changes()
    
    print("\n=== Git Changes ===")
    print(f"\nModified: {len(changes['modified'])}")
    print(f"Added: {len(changes['added'])}")
    print(f"Deleted: {len(changes['deleted'])}")
    print(f"Renamed: {len(changes['renamed'])}")
    
    print("\nDetailed Git stats:")
    print(diff_stats)

if __name__ == "__main__":
    main()