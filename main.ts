/** This code only gets executed when "time left?" is yes. When you press A the variable "time left" changes from "no" to "yes" and it keeps the value "yes" for two minutes. */
/** Changing the variable "time left?" into "yes" starts the game, because only when this variable is yes, the code in the forever loop will be executed. */
/** The players need to get the ball to the target that's connected with pin 1 first, because that one is made "active". The arrow on the display shows them which side this is. */
/** 

When the players have played for two minutes, they can't score points anymore, because the code in the forever loop isn't executed anymore when the variable "time left" is changed to "no". 

A cross will be displayed on the screen of the micro:bit to tell the players that the game is over.


 */
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    Score = 0
    time_left = "yes"
    pin_thats_active = 1
    music.startMelody(music.builtInMelody(Melodies.PowerUp), MelodyOptions.Once)
    basic.pause(250)
    basic.showLeds(`
        . . # . .
                . . . # .
                # # # # #
                . . . # .
                . . # . .
    `)
    basic.pause(120000)
    time_left = "no"
    basic.showIcon(IconNames.No)
    music.startMelody(music.builtInMelody(Melodies.PowerDown), MelodyOptions.Once)
    basic.pause(2000)
    for (let index = 0; index < 4; index++) {
        basic.showNumber(Score)
    }
    basic.showIcon(IconNames.No)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showNumber(Score)
})
/** The game starts when one of the players presses button A on the micro:bit. */
let pin_thats_active = 0
let time_left = ""
let Score = 0
Score = 0
basic.showIcon(IconNames.Yes)
basic.pause(500)
basic.showString("Press A!")
/** The pink block detects whether the electrical circuit is closed at a target by the conductive ball. */
/** You only get a point when the ball is at the right target. You don't get a point if you hit the wrong one. That pin is made inactive using the variable "pin that's active". Active is 1, inactive is 0. */
/** This arrow tells the player to which side of the maze the ball needs to go. */
basic.forever(function on_forever() {
    
    if (time_left == "yes") {
        if (input.pinIsPressed(TouchPin.P1)) {
            if (pin_thats_active == 1) {
                basic.showIcon(IconNames.Happy)
                music.startMelody(music.builtInMelody(Melodies.JumpDown), MelodyOptions.Once)
                basic.pause(1000)
                Score += 1
                basic.showNumber(Score)
                pin_thats_active = 2
                basic.pause(1500)
                basic.showLeds(`
                    . . # . .
                                        . # . . .
                                        # # # # #
                                        . # . . .
                                        . . # . .
                `)
            }
            
        }
        
        if (input.pinIsPressed(TouchPin.P2)) {
            if (pin_thats_active == 2) {
                basic.showIcon(IconNames.Happy)
                music.startMelody(music.builtInMelody(Melodies.JumpUp), MelodyOptions.Once)
                basic.pause(1000)
                Score += 1
                basic.showNumber(Score)
                pin_thats_active = 1
                basic.pause(1500)
                basic.showLeds(`
                    . . # . .
                                        . . . # .
                                        # # # # #
                                        . . . # .
                                        . . # . .
                `)
            }
            
        }
        
    }
    
})
