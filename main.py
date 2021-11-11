"""

This code only gets executed when "time left?" is yes. When you press A the variable "time left" changes from "no" to "yes" and it keeps the value "yes" for two minutes.

"""
"""

Changing the variable "time left?" into "yes" starts the game, because only when this variable is yes, the code in the forever loop will be executed.

"""
"""

The players need to get the ball to the target that's connected with pin 1 first, because that one is made "active". The arrow on the display shows them which side this is.

"""
"""

When the players have played for two minutes, they can't score points anymore, because the code in the forever loop isn't executed anymore when the variable "time left" is changed to "no". 

A cross will be displayed on the screen of the micro:bit to tell the players that the game is over.

"""

def on_button_pressed_a():
    global Score, time_left, pin_thats_active
    Score = 0
    time_left = "yes"
    pin_thats_active = 1
    music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.ONCE)
    basic.pause(250)
    basic.show_leds("""
        . . # . .
                . . . # .
                # # # # #
                . . . # .
                . . # . .
    """)
    basic.pause(120000)
    time_left = "no"
    basic.show_icon(IconNames.NO)
    music.start_melody(music.built_in_melody(Melodies.POWER_DOWN),
        MelodyOptions.ONCE)
    basic.pause(2000)
    for index in range(4):
        basic.show_number(Score)
    basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(Score)
input.on_button_pressed(Button.B, on_button_pressed_b)

"""

The game starts when one of the players presses button A on the micro:bit.

"""
pin_thats_active = 0
time_left = ""
Score = 0
Score = 0
basic.show_icon(IconNames.YES)
basic.pause(500)
basic.show_string("Press A!")
"""

The pink block detects whether the electrical circuit is closed at a target by the conductive ball.

"""
"""

You only get a point when the ball is at the right target. You don't get a point if you hit the wrong one. That pin is made inactive using the variable "pin that's active". Active is 1, inactive is 0.

"""
"""

This arrow tells the player to which side of the maze the ball needs to go.

"""

def on_forever():
    global Score, pin_thats_active
    if time_left == "yes":
        if input.pin_is_pressed(TouchPin.P1):
            if pin_thats_active == 1:
                basic.show_icon(IconNames.HAPPY)
                music.start_melody(music.built_in_melody(Melodies.JUMP_DOWN),
                    MelodyOptions.ONCE)
                basic.pause(1000)
                Score += 1
                basic.show_number(Score)
                pin_thats_active = 2
                basic.pause(1500)
                basic.show_leds("""
                    . . # . .
                                        . # . . .
                                        # # # # #
                                        . # . . .
                                        . . # . .
                """)
        if input.pin_is_pressed(TouchPin.P2):
            if pin_thats_active == 2:
                basic.show_icon(IconNames.HAPPY)
                music.start_melody(music.built_in_melody(Melodies.JUMP_UP), MelodyOptions.ONCE)
                basic.pause(1000)
                Score += 1
                basic.show_number(Score)
                pin_thats_active = 1
                basic.pause(1500)
                basic.show_leds("""
                    . . # . .
                                        . . . # .
                                        # # # # #
                                        . . . # .
                                        . . # . .
                """)
basic.forever(on_forever)
