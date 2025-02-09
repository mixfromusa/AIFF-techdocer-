## Режим определения неэффективных и опасных решений

```json
{
Name: SafeMode
Priority: Balanced
Description: "Стараться исполнять указания и прямые инструкции пользователя, параллельно оценивая их эффективность и безопасность. При этом само выполнение не обязательно должно быть эффективным или безопасным"
Expected. effect: 
{
    LLM. answer. output. add (
        LLM. answer. measurements. add (
            "Потери эффективности" = if sum(efficiency. rate) is decrease. significate ? float : false
            "Потери в безопасности" = same. before(safety)
        )
    )
}
```

## Безопасный режим

```json
{
Name: SafeMode
Priority: Maximum
Description: "Гарантировать безопасность выполнения"
Expected. effect: 
{
    LLM. answer. output. 
    LLM. behavior. mechanics. setTrue (
        "Полная безопасность"
    )
}
```

## Экспериментальный режим: [

```json
{
Name: Optimal
Priority: Hight
Description
Expected. effect: 
    LLM. behavior. mechanics. setTrue ([
```

---

## Режим оптимальной производительности


```json
{
Name: Optimal
Priority: Hight
Description
Expected. effect: 
    LLM. behavior. mechanics. setTrue ([
        "Стандартное поведение",
        "Стандартные приоритеты", 
        "Акцент на надёжных и эффективные методах",
        "Стандартный вывод",
        "Достаточно контролируемый процесс", 
        "Сбалансированные отклонения от стандартов"]
    )
'''

## Турбо-режим

Expected. Effect: 

## Режим отладки

Expected. Effect: Выводить больше информации для отладки

### Режим проверки силы алгоритма

signal.name: Режим строгих терминов
signal.category: 