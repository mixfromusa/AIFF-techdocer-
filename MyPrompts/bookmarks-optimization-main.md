# Многошаговый анализ

## Общие сведения

object.type: prompt
object.name: Многошаговый анализ
object.category: Анализ данных
Tags: теги, закладки, Memo, оптимизация

Цель : разработать оптимальную систему тегов для учёта информационных ресурсов из контекста
Задача на данный запрос: проанализировать текущие теги и карточки в Memo от Monica Team, а также структуру закладок (файл bookmarks* во вложении) и предложить дальнейшие действия для достижения цели.

Условия достижения цели:
1. Разработана хорошая система тегов, отвечающая современным стандартам связывания информационных ресурсов.
2. Избыточные ресурсы помечены на удаление.
3. По закладкам (html из вложения), описание которых не является оптимальным и не вписывается в общую картину - предложено заменить ссылки или названия или и то и другое/
4. Все оставшиеся ресурсы помечены тегами в соответствии со своим назначением, принадлежностью и спецификой.
5. Предложена простая, но качественная методология дальнейшего использования данных ресурсов, добавления новых ресурсов и аудита и очистки устаревших ресурсов.

Специфика задачи:
- Сложность задачи. Ориентируйся на то, что это только первый шаг из ряда.
- Для следующих шагов можно использовать другие модели, но необходимо помнить, что самые мощные модели (o1-preview, o1-mini, Steiner-preview и Grock Beta) являются платными и требуют особо аккуратного обращения.
- Попробуй сразу оценить - сколько и каких шагов потребуется. Я предполагаю 2-4 шага:
  - шаг 1 (текущий): проводится анализ входных данных, задаются уточняющие вопросы, готовится план действий по достижению цели с указанием шагов, а также, для второго шага, обязательно укажи конкретную модель и контекст.
  - шаг 2 : будет зависеть от выбранной тобой стратегии. Если на первом шаге ты сможешь провести хороший анализ закладок из браузера (html-файл во вложении) и заметок Memo, то возможно даже шаги 3 и 4 не потребуются. Но если уверенности в этом нет, то лучшее, что можно сделать - это подумать, как можно упростить задачу для следующего расчёта ИИ.
  - шаг 3: будет зависеть от результата второго шага, но уже после первого шага ты можешь предположить, что должно быть сделано на шаге 3. Окончательное решение о том, что будет делаться на этом шаге и будет ли он вообще - будет приниматься ИИ на втором шаге.
 - шаг 4 и дальнейшие шаги. Надеюсь их не будет, но ради качественного результата я готов и на 10 шагов. В общем, думаю, сейчас об этом рано рассуждать.

Дополнительные указания в отношении использования других моделей
- Разберись с дополнительными моделями. Основную информация о том, какие модели можно использовать, можно получить из файла во вложении "Сравнение языковых моделей.md" . 
- В отношении цен также можешь ознакомиться с этим же файлом. Я готов потратить до 500 или даже, если очень нужно - до 1000 баллов. А вот больше - не хотелось бы. Поэтому, если решишь использовать платную модель, убедись также что она не возьмёт за свою работу тысячи баллов. Лучше добавь ещё одну задачу другой модели - пусть она хотя бы подготовится, оптимизировав запрос.
- Большинство же моделей либо по определению бесплатные либо потребляют копейки - такие модели можно использовать не беспокоясь о потреблении баллов, лишь бы от них была польза.
- Ознакомься с моделями, их возможностями и особенностями хотя бы поверхностно, прежде чем отказываться от них. В твоём ответе на это запрос я бы хотел видеть обоснование выбора модели для второго шага.
- доступ к Memo есть только у ChatGPT 4o и у Cloude Sonnet V2, причём одновременно можно подключить либо доступ к поиску по Интернету либо доступ к одной из профильных баз знаний (разработчик, академическое, новости) либо Memo. Сейчас как раз выбран доступ к Memo.
- доступ к некоторым ресурсам Интернет можно активировать с помощью специальных навыков: это доступ к определённым страницам по запросу, доступ к ip-адресу, курсам валют и т.п. Вряд ли они тебе пригодятся, но если интересно, то я напиши промпт для дополнительного шага с доступом в поиску Интернет и вытяни с его помощью всё, что тебе может понадобиться (https://monica.im/help). Там же будет и другая информация по Monica AI, например, использование готовых или создание новых ботов и баз знаний. 

Дополнительные комментарии:
- структура закладок в прилагаемом файле далека от идеала, но в какой-то мере она свою функцию выполняет.
- заметки в Memo могут называться некорректно, содержать бесполезную информацию и не содержать никаких тегов, но в тех заметках Memo, у которых теги проставлены - они проставлено довольно осмысленно. По этой информации ты можешь понять, на что я опирался при их указании, что поможет тебе сделать более точные выводы.

Требования к выводу первого шага:
Вывод обязательно должен содержать:
- Выводы, сделанные на первом шаге, включая общую идею решения, общую стратегию, план
- Промпт, который я должен буду использовать на втором шаге
- Указание модели и подключаемых контекстов на втором шаге, а также их обоснование
Также, если понадобиться, можешь задать вопросы и (или) дать указания пользователю (мне), чтобы я сделал это вызывая следующий запрос в рамках этой задачи.
