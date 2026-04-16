def on_button_pressed_a():
    global colorIndex
    colorIndex = (colorIndex + 1) % 3
    doSomething()
input.on_button_pressed(Button.A, on_button_pressed_a)

def doSomething():
    basic.show_number(colorIndex)
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 0)
    pins.digital_write_pin(list2[colorIndex], 1)

def on_button_pressed_b():
    global colorIndex
    colorIndex = (colorIndex + 2) % 3
    doSomething()
input.on_button_pressed(Button.B, on_button_pressed_b)

colorIndex = 0
list2: List[number] = []
list2[0] = DigitalPin.P0
list2[2] = DigitalPin.P2
list2[1] = DigitalPin.P1