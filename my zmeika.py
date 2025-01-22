import turtle
import random


delay = 0.1
score = 0


x = random.randint(-400, 400)
y = random.randint(-300, 300)


score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-350, 250)
score_display.write(f"Счет: {score}", font=("Arial", 16, "normal"))


window = turtle.Screen()
window.title("управление черепашка")
window.screensize(canvwidth=800, canvheight=600)


#создаём черепашка
t = turtle.Turtle()
t.shape("turtle")
t.speed(1000)


#яблоко
apple = turtle.Turtle()
apple.shape("circle")
apple.color("red")
apple.penup()
apple.speed(0)
apple.goto(x, y)


def go_apple():
    x = random.randint(-400, 400)
    y = random.randint(-300, 300)
    apple.penup()
    apple.goto(x, y)
    apple.down()
    apple.speed(-1)
    check_poss()



def move_forward():
    t.forward(10)
    check_poss()
def move_backward():
    t.backward(10)
    check_poss()

def move_left():
    t.left(90)
    check_poss()
def move_right():
    t.right(90)
    check_poss()

def clear_screen():
    t.clear()
def reset_position():
    t.penup()
    t.home()
    t.pendown()

def check_poss():
    if t.distance(apple) < 20:
        go_apple()
        t.up()
        t.goto(0, 0)
        t.down()
        clear_screen()
        update_score()

def update_score():
    global score
    score += 1
    score_display.clear()
    score_display.write(f"Счет: {score}", font=("Arial", 16, "normal"))


window.listen()
window.onkeypress(move_forward,"w")
window.onkeypress(move_backward,"s")
window.onkeypress(move_left,"a")
window.onkeypress(move_right,"d")
window.onkeypress(clear_screen,"c")
window.onkeypress(reset_position,"r")

window.mainloop()