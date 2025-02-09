[![Main branch AaC Workflow](https://github.com/DevOps-MBSE/AaC/actions/workflows/main-branch.yml/badge.svg)](https://github.com/DevOps-MBSE/AaC/actions/workflows/main-branch.yml)
[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/from-referrer/)

# Note to Contributors

Из -за определенных неконтролируемых обстоятельств, связанных с окружающей средой, в которой
Архитектура-код разрабатывается и финансируется, мы не можем принять какие-либо новые внешние
Вклад в это время.Мы отклоним любые запросы на притяжение из неизвестных источников.
Хотя это прискорбно, мы все еще принимаем обратную связь и идеи, которые улучшат
форма и функция продукта AAC во всех его формах.Приносим извинения за это неудобства.

В будущем мы намерены принять взносы из внешних источников
согласно нашим стандартам и кодексу поведения.Мы стремимся достичь цели
хранилище с открытым исходным кодом и надеется, что потенциальные участники все равно будут следовать нашим
Прогресс и присоединяйтесь к нам в будущем.


# Architecture-as-Code (AaC)

AAC-это совершенно другой взгляд на модель системного проектирования (MBSE), который позволяет
Системный модельер для определения системы в простом YAML.Этот подход позволяет инженерам
Примените строгое управление конфигурацией к их базовым показателям (в отличие от других подходов «коробки и линий»).
Наша команда провела много лет, создавая, строительство, тестирование и доставку сложных систем.В
В то время мы видели огромное количество усилий и денег, вложенных в моделирование системы.К сожалению,
Почти всегда тот случай, когда модель системы либо никогда не используется строительством команд и
Предоставление продукта, или он добавляет сложность к рабочим процессу этой команды и становится препятствием.А
Создатели AAC потратили много лет, работая над тем, чтобы принять и адаптировать принципы DevOps внутри
Наши профессиональные рабочие места.Мы видели удивительную эффективность, которая может быть достигнута путем сбивания
«стена путаницы» между разработчиками и операциями и оптимизация вокруг системного мышления, потока,
и постоянное улучшение посредством обучения и экспериментов.Мы считаем, что критический переломный момент
Это позволило этому произойти создание инфраструктуры как код и принятие новых практик
Как жители, которые используют автоматическое обеспечение качества, автоматическое развертывание и непрерывный мониторинг.
Наша цель состоит в том, чтобы сбить «стену путаницы», которая существует между системной техникой и
Разработка, оптимизация общего потока стоимости доставки системы от концепции/требований до
Операции с полной отслеживаемостью и управлением конфигурацией повсюду.Мы верим, что можем
Откройте для себя новые способы определения, доставки и развития сложных систем, используя архитектуру как код.

AAC-это самоопределяющее решение.В основе приложения AAC лежит определение самого AAC.
Эта модель проверяет себя на правильность.Основные типы данных целенаправленно просты и могут быть
Расширен пользователем.

AAC разработан с учетом расширяемости.Встроенная функциональность намеренно сводит к минимуму.
AAC использует плагин-систему для расширения базовых возможностей.Чтобы еще больше упростить это, AAC включает
Встроенная команда для создания новых плагинов из модели AAC.Есть несколько внутренних примеров этого
В папке плагинов репозитория и дополнительная информация ниже.

## Using AaC to Model Your System

AAC написан на Python, чтобы помочь сделать его более доступным для случайных пользователей и легко расширяется для
Пользователи питания.

** Вам понадобится Python 3.9 или позже, чтобы запустить AAC. **

Для установки AAC на Linux или Windows:
```bash
pip install aac
```

Чтобы использовать AAC, вы сначала определите модель вашей системы в YAML.Обратитесь к документации для получения более подробной информации.
Простая модель для эхосервиса представлена ​​здесь для справки.Вырезать и вставить приведенную модель в
Файл с именем echoservice.yaml.
*Примечание: это использует небольшой трюк YAML, чтобы объединить содержимое двух файлов YAML в один файл.**
```yaml
schema:
  name: Message
  fields:
  - name: body
    type: string
  - name: sender
    type: string
---
model:
  name: EchoService
  description: This is a message mirror.
  behavior:
    - name: echo
      type: REQUEST_RESPONSE
      description: This is the one thing it does.
      input:
        - name: inbound
          type: Message
      output:
        - name: outbound
          type: Message
      acceptance:
        - scenario: onReceive
          given:
           - The EchoService is running.
          when:
            - The user sends a message to EchoService.
          then:
            - The user receives the same message from EchoService.
```

Теперь вы можете запустить AAC против своей модели.
```bash
aac check EchoService.yaml
```

AAC имеет некоторые основные «типы корней» для вас.Вы можете увидеть типы корней «схемы» и «Модель», используемые в приведенном выше примере.
Типы основных корней AAC:
- Схема: позволяет моделировать структуры данных, используемые в вашей системе в качестве пользовательских типов.
- enum: позволяет вам моделировать перечисленные значения (типы с разрешенными только конкретными значениями).
- Модель: позволяет вам моделировать компоненты вашей системы и их интерфейсы.Они могут быть абстрактными или конкретными.
- Usecase: позволяет вам моделировать поведение и взаимодействие между вашими моделями.
- Плагин: позволяет легко расширить сам DSL AAC и создавать адаптированные команды AAC для ваших потребностей.

Хотя при моделировании вашей системы вы можете использовать трюк YAML, было бы лучше сохранять вещи больше
структурированный и организованный.Чтобы помочь с этим AAC, позволяет определить каждый элемент, который вы моделируете в отдельном файле и
Затем импортируйте его по мере необходимости.Для этого просто поместите ** импорт ** в корне из файла модели.

Вот пример эхосервиса, разбитого на два файла:
*Message.yaml*
```yaml
schema:
  name: Message
  fields:
    - name: body
      type: string
    - name: sender
      type: string
```
*EchoService.yaml*
```yaml
import:
  files:
    - ./Message.yaml
---
model:
  name: EchoService
  description: This is a message mirror.
  behavior:
    - name: echo
      type: REQUEST_RESPONSE
      description: This is the one thing it does.
      input:
        - name: inbound
          type: Message
      output:
        - name: outbound
          type: Message
      acceptance:
        - scenario: onReceive
          given:
           - The EchoService is running.
          when:
            - The user sends a message to EchoService.
          then:
            - The user receives the same message from EchoService.
```

Ok, so that's interesting, but what can you do with the AaC model once you've built it?
AaC is designed and built on years of experimentation, experience, and learning.  But this version
is a brand new implementation rewritten entirely in Python in an attempt to make AaC more user friendly
to both the casual user and the power user. Right now AaC doesn't have a lot of additional features.
But new plugins are being created to deliver more functionality.  Over time there will be plugins
available to use the AaC model to auto-generate content for reviews, documentation, and even system
development and deployment.

## User Documentation
Users who would like more detailed documentation on leveraging AaC can find it in our Github pages [User Guide Documentation](https://arch-as-code.org/project_documentation/user_guide/index.html)

## Developer Documentation
Contributors, developers, or just generally interested parties who would like to understand the more technical underpinnings of AaC are welcome to read the project and developer documentation found in our Github pages [Developer Guide Documentation](https://arch-as-code.org/project_documentation/dev_guide/index.html)


We're also actively working on other functionality so keep an eye out for new updates.

## pyproject.toml vs setup.py

Previously, this project was built with dependency information kept in a setup.py script.
However, the preferred method is to use pyproject.toml to set the project-level options.
Required modules are kept in the dependency sections of the pyproject.toml, and then the
pip-compile command is used to add hashes to the requirements.txt file for enhanced security
(see additional instructions below).

To coincide with these changes, some changes to tox.ini and the addition of a MANIFEST.ini file were also necessary.

These lines were added to tox.ini:
```
   isolated_build = True
   skipsdist = True
```

A MANIFEST file with these lines was added:
```
   graft src
   graft tests
   include tox.ini
   include src/aac/aac.aac
```

## TO BUILD FROM TERMINAL

```
cd python
pip install -e .
```

## TO TEST FROM TERMINAL

```
cd python
pip install -e .
python -m unittest
```

## Generate a requirements.txt file populated with hashes

```
pip install pip-tools
pip-compile --generate-hashes pyproject.toml
```
