# Установка кодировки
#[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
#$PSDefaultParameterValues['*:Encoding'] = 'utf8'

# Заголовки
$headers = @{
    "Content-Type" = "application/json charset=utf"
    "Authorization" = "Bearer sk-aBJ4Rq5Bqg9JFDVGb6TDaUH2fx-8PlfJlrqVbs9aVR5VtUvog-nF1yc-Aa98xdiLgCFTgvh7pPTk8AcUbxEaw3u-PEfQ"
    #  "Accept" = "application/json"
    #  "User-Agent" = "PowerShell/7.0"  # Добавляем User-Agent
    #  "Monica-Version" = "2024-01-01"  # Добавляем версию API если требуется
}

# Тело запроса
$body = @{
    model = "gpt-4o"  
    messages = @(
        @{
            role = "user"
            content = "This is test message, answer it randomize number from 1 to 100"
        }
    )
}

# Преобразование в JSON
$jsonBody = $body | ConvertTo-Json -Depth 10

# Отправка запроса и обработка ответа с корректной кодировкой
try {
    $response = Invoke-RestMethod -Uri "https://openapi.monica.im/v1/chat/completions" `
                                -Method POST `
                                -Headers $headers `
                                -Body $jsonBody 

    # Прямой доступ к содержимому ответа
    $content = $response.choices[0].message.content
    
    Write-Host "Ответ ассистента:" $content
    
} catch {
    Write-Host "Ошибка:" $_.Exception.Message
    Write-Host "Статус код:" $_.Exception.Response.StatusCode.value__
    # Получение дополнительной информации об ошибке
    $errorResponse = $_.ErrorDetails.Message
    if ($errorResponse) {
        Write-Host "Детали ошибки:" $errorResponse
    }
    
    # Вывод отправленного JSON для проверки
    # Write-Host "Отправленный JSON:" $jsonBody
}
