def on_button_pressed_a():
    global currentNum
    if currentNum < 100:
        currentNum = currentNum + 1
        basic.show_number(currentNum)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global currentNum, streakNum
    if currentNum != selectedNum:
        currentNum = selectedNum
    if selectedNum == answerNum:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . #
            . # . # .
            . . # . .
            """)
        streakNum = streakNum + 1
    elif selectedNum != answerNum:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
        streakNum = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global currentNum
    if currentNum > 1:
        currentNum = currentNum - 1
        basic.show_number(currentNum)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    control.reset()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

streakNum = 0
answerNum = 0
currentNum = 0
selectedNum = 0
selectedNum = 0
currentNum = 0
answerNum = randint(1, 100)

def on_forever():
    (answerNum)
    (currentNum)
    (selectedNum)
basic.forever(on_forever)
