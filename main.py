def on_button_pressed_a():
    basic.show_number(1023 - pins.analog_read_pin(AnalogPin.P1))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
