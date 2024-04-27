import turtle
import keyboard
import subprocess



eldarLOx = turtle.Turtle()


while True:
    if keyboard.is_pressed("w"):
        eldarLOx.forward(10)

    if keyboard.is_pressed("a"):
        eldarLOx.left(10)

    if keyboard.is_pressed("d"):
        eldarLOx.right(10)
    
    if keyboard.is_pressed("s"):
        eldarLOx.back(10)
    
    if keyboard.is_pressed("esc"):
        break
    if keyboard.is_pressed("ctrl"):
        eldarLOx.write("Zapomnite ELDA LOX")

    if keyboard.on_press:
        eldarLOx.