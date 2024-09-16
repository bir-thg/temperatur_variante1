input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    if (input.temperature() > 25) {
        basic.setLedColor(basic.rgb(255, 0, 0))
    } else if (input.temperature() < 15) {
        basic.setLedColor(basic.rgb(0, 0, 255))
    } else {
        basic.setLedColor(basic.rgb(0, 255, 0))
    }
    basic.pause(1000)
    basic.showString("" + input.temperature())
    basic.pause(1000)
    basic.showLeds(`
        . . . # .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
basic.showIcon(IconNames.Yes)
basic.forever(function () {
	
})
