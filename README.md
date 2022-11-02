# window-control - What it does
- Waits for 120 s after start up
- Identifies all windows with either 'TV' or 'Fast' in the name
- Activates each window  and presses F11 four times with 2s in between

## Compiling python script using PS2EXE
- Open powershell as administrator and run ```Win-PS2EXE```
- Point the source to the 'test.ps1' file (full address, i.e. 'C:\[...]\test.ps1'
- Point the output to any directory where you want the output, then add the name of the exe file (i.e. 'C:\[...]\fullscreen.exe')
- Deselect the 'Compile a graphics windows program' check box
- Press 'Compile'

## Installing Fullscreen.exe on the target computer such that it autostarts on the target computer
- Put the *.exe file on a flashdrive
- Insert the flashdrive into the target computer
- Press Windows key + R
- Write ```shell:startup```
- Press Enter (This opens the autostart folder)
- Copy the *.exe file to the autostart folder from the USB drive
- Done
You can try it out by restarting the target computer and wait to see if it works, keep in mind that it will take at least two minutes.
