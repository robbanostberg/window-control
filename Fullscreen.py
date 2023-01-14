from screeninfo import get_monitors
from pynput.mouse import Controller as mouseCon, Button
from pynput.keyboard import Controller as keyCon, Key
from time import sleep as wait

mouse = mouseCon()  # Skapar musobjekt
kb = keyCon()  # Skapar tangentbordsobjekt
marginal = 0.2  # Avstånd från kanten av skärmen
startup = 120  # Väntetid från start till exekvering
delay = 0.5  # Paus mellan tryck

print("Waiting for " + str(startup) + " seconds before executing F11 presses to send FAST TV windows into fullscreen mode")  # Berättar vad som pågår för de som ser skärmen
wait(startup)  # Väntar så de andra programmen hinner starta

for m in get_monitors():  # Tar reda på antalet skärmar och gör följande för varje skärm:
    mouse.position = (m.x + int(m.width * marginal), m.y + int(m.height * marginal))  # Placerar musen 20% in uppifrån och vänsterifrån på skärmen
    mouse.click(Button.left)  # Klickar en gång med musen för att aktivera programfönstret
    wait(delay)
    kb.tap(Key.f11)  # Trycker F11 två gånger
    wait(delay)
    kb.tap(Key.f11)

   





