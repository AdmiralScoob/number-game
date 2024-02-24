input.onButtonPressed(Button.A, function () {
    if (currentNum < 100) {
        currentNum = currentNum + 1
        basic.showNumber(currentNum)
    }
})
input.onGesture(Gesture.LogoUp, function () {
    if (currentNum > 1) {
        currentNum = currentNum - 10
        basic.showNumber(currentNum)
        basic.pause(5000)
    }
})
input.onButtonPressed(Button.AB, function () {
    if (selectedNum != currentNum) {
        selectedNum = currentNum
    }
    if (selectedNum == answerNum) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . #
            . # . # .
            . . # . .
            `)
        streakNum = streakNum + 1
        basic.showString("Attempts:" + attemptNum)
    } else if (selectedNum != answerNum) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
        streakNum = 0
        attemptNum = attemptNum + 1
        if (selectedNum < answerNum) {
            basic.showArrow(ArrowNames.North)
        } else if (selectedNum > answerNum) {
            basic.showArrow(ArrowNames.South)
        }
    }
})
input.onButtonPressed(Button.B, function () {
    if (currentNum > 1) {
        currentNum = currentNum - 1
        basic.showNumber(currentNum)
    }
})
input.onGesture(Gesture.Shake, function () {
    answerNum = randint(1, 100)
    selectedNum = 0
    currentNum = 0
    attemptNum = 0
    basic.pause(5000)
})
input.onGesture(Gesture.LogoDown, function () {
    if (currentNum < 100) {
        currentNum = currentNum + 10
        basic.showNumber(currentNum)
        basic.pause(5000)
    }
})
let attemptNum = 0
let streakNum = 0
let currentNum = 0
let selectedNum = 0
let answerNum = 0
answerNum = randint(1, 100)
selectedNum = 0
currentNum = 0
serial.writeLine("Answer:" + answerNum)
