from screeninfo import get_monitors
from pynput.mouse import Controller as mouseCon, Button
from pynput.keyboard import Controller as keyCon, Key
from time import sleep as wait

mouse = mouseCon()
kb = keyCon()
marginal = 0.3
startup = 10
delay = 0.5

wait(startup)

for m in get_monitors():
    mouse.position = (m.x + int(m.width * marginal), m.y + int(m.height * marginal))
    mouse.click(Button.left)
    kb.tap(Key.f11)
    wait(delay)
    kb.tap(Key.f11)

   





