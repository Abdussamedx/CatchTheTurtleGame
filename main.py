import turtle
import random

#Ekran
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.setup(800, 600)
screen.title("Catch The Turtle")


#Skor
score =0

#Geri sayım süre
time_left= 30

#Puan yazısı
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0 ,260)
score_display.write(f"Puan: {score}", align="center", font=("Arial", 24, "bold"))

#Süre yazısı

timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.goto(0, 230)
timer_display.write(f"Kalan Süre: {time_left}", align="center", font=("Arial", 18, "bold"))

#Kaplumbağa

catch_turtle = turtle.Turtle()
catch_turtle.shape("turtle")
catch_turtle.color("dark green")
catch_turtle.penup()
catch_turtle.speed(0)


#Kaplumbağayı rastgele yere taşı
def move_turtle():
    if time_left > 0:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        catch_turtle.goto(x, y)
        screen.ontimer(move_turtle, 1000)

#Tıkladıkça puanı artır
def catch(x, y):
    global score
    if time_left > 0:
        score += 1
        score_display.clear()
        score_display.write(f"Puan: {score}", align="center", font=("Arial", 24, "bold"))


#Geri sayım
def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_display.clear()
        timer_display.write(f"Kalan Süre: {time_left}", align="center", font=("Arial", 18, "bold"))
        screen.ontimer(countdown, 1000)
    else:
        catch_turtle.hideturtle()
        timer_display.clear()
        timer_display.write("⏰ Oyun Bitti!", align="center", font=("Arial", 22, "bold"))


catch_turtle.onclick(catch)
move_turtle()
countdown()


turtle.mainloop()
