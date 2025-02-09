#!/bin/bash

# Проверка наличия параметра
if [ $# -eq 0 ]; then
    echo "Error: Message text is required"
    echo "Usage: $0 \"your message\""
    exit 1
fi

MESSAGE="$1"
RESPONSEALL="0"

if [ $# -eq 2 ]; then
   RESPONSEALL="$2"
fi

# Отправка запроса к API (замените URL и данные на ваши)
response=$(curl -s -v -X POST "https://openapi.monica.im/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-aBJ4Rq5BF1yc-Aa98xdiLgCFTgvh7pPTk8AcUbxEaw3u-PEfQ" \
  -d "{
  	\"model\":\"gpt-4o\",
	\"messages\":[{
		\"role\":\"user\",
		\"content\":[{
			\"type\":\"text\",
			\"text\": \"$MESSAGE\"
		]}
	]}"
}"
)


# Отладочный вывод
echo "Response: $response"

# Проверяем, что JSON не пустой
if [ -z "$response" ]; then
    echo "Error: Empty response from API"
    exit 1
fi

if [ "$RESPONSEALL" = 'ra' ]; then
	echo "$response" 
else
 # Используем jq для обработки ответа
    echo "$response" | jq -r '
    .choices[] | 
    "choices[\(.index)]\n\(.message.content)"
    '
fi