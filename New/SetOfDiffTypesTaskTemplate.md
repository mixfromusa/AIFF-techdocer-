# Set of Different Types Tasks Template

## meta

- Type: tasksListSpecialTemplate

## Symbols, Keywords, Rules and Recommendations

### Default rules
- Any text in square brackets [] is a placeholder for a specific keyword, construct, variable, directive or other specific meaning.

### Special symbols and constructions

- Symbols: "#", "-", and other base markdown symbols used for formatting
- Symbol: $ = (DOLLAR_SYMBOL) = Unicode(0x24) = ANY - prefix indicating generalization (e.g. $type = any type)
- Symbols: $symbols = anySetofSimbols(SetofSimnols(typeOf(format, style))) that point to a determined style or format - used for details rules in concrete format of document
- Construction: [$text] - points to a keyword or variable, valid for a current expression (usually that word, phrase, string, sentence, codeLine, math expression, or same short text)
- Construction: [$text:] - points that the $text effect will be continued until it is closed with the appropriate tag.
- Construction: [/$text] - close tag of the $text, finishes its effect. 


- *Result and delegation requirements* - curcive typically inserts with template and not editing or formating
 
- [description] - description of the task type
- [example] = forExample() = (examples:) = (напр.) = ... and similar - example of content for such task
- [typical] - typical target for such task
- [requirement] - requirement for such task
- [recommendation] - recommendation for such tasks
- [-$keyword] - any keyword with prefix "-" means that the task is not about this keyword
- [up] = "-" - повешенный приоритет
- [down] = "-" пониженный приоритет
- [min] - минимально
- [few] - незначительно
- [balanced] - сбалансированною, используется по умолчанию
- [lot] - значительно
- [max] - максимально

[recommendation] - you may create a spectial sets of symbols, taskTypes and tasks - better relevant to concrete task.

### Main

*Выполняется обязательно,*
*может быть частично делегирована*

[description:]
Главная задача. Должна быть выполнена обязательно. Обладает наибольшим приоритетом и, как правило, задаёт основную линию контекста.


[example:]
- Найди наиболее корректные и подходящие название (и определение) для типа записи журнала NameOf(TypeOf(JournalRecord).

Предложи хорошие короткие, но сохраняющие смысл варианты.
Также важны:
- простота,
- точность,
- понятность,
- возможность корректной записи во фразу из только существительных слов.

[typical:]


### Additional

*Выполняется по возможности*

Какие инсайты (интересные выводы, феномены, свойства, взаимосвязи, закономерности, тенденции и т.д.) можно получить проводя такой анализ?

### Extra

*Выполняется только если выполнены главная и дополнительная задачи, иначе - частично или полностью делегируется*

Предложи концепт, стратегию и конкретные инструкции (минимум на следующий шаг и, если необходимо - на несколько шагов вперёд, приводящих к развитию прогресса с получением инструкций последующих шагов (рекурсивно, но с гарантированной остановкой) по организации исследования вопросов правил классификации, именований и типизации, с использованием режима TheBattleOfTheBots (описание режима во вложении).

### Super

*Выполняется при наличии свободных ресурсов и энтузиазма либо делегируется*

Предложи, как можно получить более качественные и точные результаты любого из затронутых процессов, подходов и решений.

### Creative

*Выполняется произвольным образом, фокус на креативности, делегируется любым доступным способом, в т.ч. - только что придуманным*

### Random

*Выполняется (и/или/частично/иначе) делегируется случайным образом*

Предложи случайное решение или делегирую случайно.

### Crazy

*Выполняется или не выполняется, а может даже, делегируется - как заблагорассудиться*

Предложи что-то совершенно безумное, но в рамках темы.

## Possible Target Type Objects Возможные примеры объектов данного типа:
JournalRecord
FieldsRecord
TableRecord
TableColumn
CodeStroke (very maybe)
MathSequence (very maybe)
FixedTimestampEvent
TaskList (maybe)
ComplexNumbers (maybe)

## Examples (need better)

Не очень хорошие варианты для примера:

- множество пар однотипных объектов
- множество пар объектов, связанных определённым образом
- set of series of objects of the same type
- Композиция однотипных объектов, расположенных в хронологической последовательности в рамках определённого процесса. A composition of objects of the same type arranged in chronological order within a certain process.
- Временной ряд однотипных объектов
- Временной ряд записей
- Композиция записей