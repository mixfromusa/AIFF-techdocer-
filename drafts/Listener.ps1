#Run this code in admin mode

#todo: поменять на Basic Authentication
Start-HTTPListener - $Port = 2105, $Url = "192.168.2.11", $Auth =  [System.Net.AuthenticationSchemes]::BasicAuthentication
Write-Host "HTTP Listener started"

$cred = Get-Credential -UserName "admin" -Message "Enter password for admin user"
Write-Host "Credentials created"

Invoke-RestMethod -Uri "http://192.168.2.11:2105" -Credential $cred