let colorIndex = 0
input.onButtonPressed(Button.A, function () {
    colorIndex = (colorIndex + 1) % 3
})
input.onButtonPressed(Button.B, function () {
    colorIndex = (colorIndex + 2) % 3
})
