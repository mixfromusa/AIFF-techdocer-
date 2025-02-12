

## Вопрос
Помоги выбрать инструмент управления ссылками

## Ожидаемый формат ответа
# формат ответа
Тип ответа: Массив json, содержащий информацию о наиболее подходящих инструментах
Размер ответа: 3-10 записей
Сортировка ответа: По релевантности (Для определения использовать дополнительный контекст)
# структура ответа
{
    "tool": "имя",
    "link": "ссылка",
	"license": {
		"name": "имя",
		"url": "ссылка",
		"isOpenSource": "открытый исходный код",
		"isFree": "бесплатный"
	},
	"description": "описание",
	"expectedFeatures" {
		"isTagSupport": "поддержка тегов",
		"isMultiplatform": "многоплатформенность",
		"isDuplicateDetection": "обнаружение дубликатов",
		"isRelatedLinksDetection": "обнаружение связанных ссылок"
	}
	"additonFeaturesAi": ["дополнительные интеллектуальные функции"],
	"additonFeaturesOther": ["дополнитеьлная функция"],
	"compatibility" {
		"standarts": ["стандарты"]
		"os": ["операционные системы"],
		"browsers": ["браузеры"],
		"import_export_formats": ["форматы импорта и экспорта"],
	},
	"ai_relevance": "оценка релевантности ИИ данного инструмента",
	"ai_comment": "комментарий ИИ к данному инструменту"    
}

## Дополнительный контекст

# Потребность
Приведение в порядк ссылок, накопленных в процесе различной деятельности

# Источники данных
Браузеры:
	Yandex.Browser
	Chrome
	Opera
	Edge
Расположение в браузерах:
	Закладки в иерархическом порядке
	Открытые вкладки

# Пожелания к функциям
- Возможность умного импорта ссылок в гибридном режиме, поддерживающим:
	- точное, либо очень близкое к точному определение размещения ссылки
	- временные метки для временного размещения, предполагающие определение точного размещения в дальнейшем
	- указание на ненужность хранения ссылки и причину
	- рекомендации ИИ в отношении ссылок данного типа
- Периодическая проверка некоторых ссылок на доступность
- Анализ полезности ссылок 
- Использование баз знаний интернет-ресурсов для анализа полезности ссылок
- Любые мощные возможности по приведению ссылок в порядок.

# Дополнительные сведения
Кроме закладок в браузерах и открытых вкладок, ссылки также содержаться в других инструментах, например:
- сообщения в канале "Избранное" Telegram
- заметки Memo Monica AI от Monica Team
Однако в этих источниках кроме ссылок может быть и другая информация (обычно в виде сопровождающего текста Markdown) - если их также можно будет извлечь, то это будет полезно.