input.onButtonPressed(Button.A, function () {
    basic.showNumber(1023 - pins.analogReadPin(AnalogPin.P1))
})
basic.forever(function () {
	
})
