$wshell = New-Object -ComObject wscript.shell; # skapar ett ComObject som kan skicka tangent-tryck
Start-Sleep 100 # sekunder innan resterande script 
$FindProcess = Get-Process | Where-Object {$_.MainWindowTitle -like "*$processterm*"}
$windows = Get-Process -ID $FindProcess.ID | Select-Object * # skapar en array med alla programfönster

foreach($window in $windows){ # går igenom alla fönster, aktiverar dem samt skickar två F11-tryckningar
    $wshell.AppActivate($window.Name)
    Start-Sleep 0.5
    $wshell.SendKeys('{F11}')
    Start-Sleep 0.5
    $wshell.SendKeys('{F11}')
}