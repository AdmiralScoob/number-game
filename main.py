def on_button_pressed_a():
    global currentNum
    if currentNum < 100:
        currentNum = currentNum + 1
        basic.show_number(currentNum)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    global currentNum
    if currentNum > 10:
        currentNum = currentNum - 10
        basic.show_number(currentNum)
        basic.pause(5000)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_button_pressed_ab():
    global selectedNum, streakNum, attemptNum
    if selectedNum != currentNum:
        selectedNum = currentNum
    if selectedNum == answerNum:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . #
            . # . # .
            . . # . .
            """)
        streakNum = streakNum + 1
        basic.show_string("Attempts:" + ("" + str(attemptNum)))
    elif selectedNum != answerNum:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
        streakNum = 0
        attemptNum = attemptNum + 1
        if selectedNum < answerNum:
            basic.show_arrow(ArrowNames.NORTH)
        elif selectedNum > answerNum:
            basic.show_arrow(ArrowNames.SOUTH)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global currentNum
    if currentNum > 1:
        currentNum = currentNum - 1
        basic.show_number(currentNum)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global answerNum, selectedNum, currentNum, attemptNum
    answerNum = randint(1, 100)
    selectedNum = 0
    currentNum = 0
    attemptNum = 0
    basic.pause(5000)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_logo_down():
    global currentNum
    if currentNum <= 90:
        currentNum = currentNum + 10
        basic.show_number(currentNum)
        basic.pause(5000)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

attemptNum = 0
streakNum = 0
currentNum = 0
selectedNum = 0
answerNum = 0
answerNum = randint(1, 100)
selectedNum = 0
currentNum = 0
serial.write_line("Answer:" + ("" + str(answerNum)))