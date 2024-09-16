def on_button_b():
    if input.temperature() > 25:
        basic.set_led_color(basic.rgb(255, 0, 0))
    elif input.temperature() < 15:
        basic.set_led_color(basic.rgb(0, 0, 255))
    else:
        basic.set_led_color(basic.rgb(0, 255, 0))
    basic.pause(1000)
    basic.show_string("" + str(input.temperature()))
    basic.pause(1000)
    basic.show_leds("""
        . . . # .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

basic.show_icon(IconNames.YES)

def on_forever():
    pass
basic.forever(on_forever)
