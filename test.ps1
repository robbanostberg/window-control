
$wshell = New-Object -ComObject wscript.shell; # skapar ett ComObject som kan skicka tangent-tryck
Start-Sleep 120 # sekunder innan resterande script 
$FindProcess = Get-Process | Where-Object {$_.MainWindowTitle -ne ""} | Select-Object MainWindowTitle #Get-Process | Where-Object {$_.MainWindowTitle -like "*$processterm*"}
$tvs = @()
#Write-Output $FindProcess
foreach($window in $FindProcess){
    if( $window.MainWindowTitle.Contains('TV') -or $window.MainWindowTitle.Contains('Fast')){
        $tvs += $window
    }
}
#Write-Output $tvs.Count
foreach($window in $tvs){
    $wshell.AppActivate($window.MainWindowTitle.ToString())
    $wshell.SendKeys('{F11}')
    Start-Sleep 2
    $wshell.SendKeys('{F11}')
    Start-Sleep 2
    $wshell.SendKeys('{F11}')
    Start-Sleep 2
    $wshell.SendKeys('{F11}')
    Start-Sleep 2  
}

#Start-Sleep 5