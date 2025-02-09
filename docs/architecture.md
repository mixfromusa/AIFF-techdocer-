# Архитектура проектов

## Общая структура
```mermaid
graph TD
    CID[CID Project] --> |Использует| KB[KnowledgeBase]
    KB --> |Предоставляет| Tools[Инструменты]
    KB --> |Предоставляет| Docs[Документация]
    KB --> |Интегрирует| AI[ИИ-сервисы]
    
    Tools --> PageExtractor[page_extractor.py]
    Tools --> DocIndexer[doc_indexer.py]
    Tools --> Translator[translator.py]
    
    AI --> MonicaAI[Monica AI]
    AI --> OtherAI[Другие ИИ]
    
    Docs --> WriterSide[JetBrains Writerside]
    Docs --> MPS[JetBrains MPS]
    Docs --> IDEA[IntelliJ IDEA]