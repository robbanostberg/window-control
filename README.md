# window-control
- Waits for 120 s after start up, counts all windows*, uses alt-tab to step through all windows and presses F11 twice.
*the counter also counts the taskbar and one other non-window entity, the amont of windows are thererfore reduced with 2 so it matches the actual amount of visible windows.

## Compiling python script using pyinstaller
- Navigate to the same directory as the python file
- ```pyinstaller --onefile Fullscreen.py```
- If all goes well, the script.exe file will be located in the /dist directory. 

## Installing Fullscreen.exe on the target computer such that it autostarts on the target computer
- Put the *.exe file on a flashdrive
- Insert the flashdrive into the target computer
- Press Windows key + R
- Write ```shell:startup```
- Press Enter (This opens the autostart folder)
- Copy the *.exe file to the autostart folder from the USB drive
- Done
You can try it out by restarting the target computer and wait to see if it works, keep in mind that it will take at least two minutes.
