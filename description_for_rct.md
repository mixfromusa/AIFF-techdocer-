# Пояснения к таблице классификации цифровых ресурсов

## meta

- title: Пояснения к таблице классификации цифровых ресурсов
- description: Пояснения к таблице классификации цифровых ресурсов
- type: note
- date.created: 15.01.2025
- date.modified: 15.01.2025
- author: Mikhail K

## instruction for AI

### Задачи проверки и улучшения

- Языковая корректность: исправление грамматических и орфографических ошибок
- Структура документа: анализ и оптимизация
- Стилистическое соответствие: проверка на соответствие общепринятым нормам
- Именование: проверка корректности названий переменных и полей
- Структура таблицы: анализ полноты и корректности полей
- Логическая целостность: выявление и исправление противоречий
- Оптимизация: поиск возможностей для сокращения без потери смысла
- Общий анализ: выявление прочих возможностей для улучшения

## list of columns with description

### note.date.created

- title: Дата создания ресурса
- description: свойство, унаследованное от object, содержащее дату создания ресурса
- type: timestamp
- required: true

### note.date.modified

- title: Дата изменения ресурса
- description: свойство, унаследованное от object, содержащее дату последнего редактирования ресурса
- type: timestamp
- required: true

### note.author.title

- title: Автор ресурса
- description: Функция, унаследованная от actor, возвращающая короткое имя или псевдоним автора ресурса
- type: string(255)
- required: true

### source.type

- title: Тип источника
- description: свойство, унаследованное от object, определяющее тип источника
- type: set(sources.types)
- recommended_values: user.memo.card, user.knowledgeBase, prompt.context, user.manual, system.generated, user.work.repo, user.work.wiki, user.work.tracker, user.work.other, external.resource
  
### source.path

- title: Путь к источнику
- description: свойство path, содержащее путь к источнику, преимущественно в виде URL
- type: string.url
- required: false

### note.title

- title: Заголовок ресурса
- description: свойство, унаследованное от object, содержащее заголовок ресурса
- type: string(255)
- required: true

### note.type

- title: Тип ресурса
- description: Обязательное свойство, унаследованное от object, определяющее тип ресурса
- type: set(notes.types)
- recommended_values: request_response, tutorial, list, code, official, journal, note, reminder, task, reference,summary, decision
- required: true

### note.tags

- title: Теги ресурса
- description: Содержит список тегов ресурса
- type: set(notes.tags)
- examples: research, tutorial, reference, code, documentation, org, CID
- required: false

### note.content.first(255)

- title: Содержание ресурса (первые 255 символов)
- description: Функция first(int), унаследованная от object.printf(int), возвращающая первые int символов содержания ресурса
- type: string(255)
- required: true
