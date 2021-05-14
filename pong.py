import turtle
import os

# Creating menu
menu = turtle.Screen()
pen1 = turtle.Turtle()
pen1.hideturtle()

# Writing Start Button
pen1.goto(-80,0)

for i in range(2):
    pen1.speed(0)
    pen1.forward(160)
    pen1.left(90)
    pen1.forward(60)
    pen1.left(90)

pen1.penup()
pen1.goto(-35, 15)
pen1.write("Start", font=("Verdana", 20, "bold"))

def buttonclick(x, y):
    # Game Beggins
    if x > -79 and x < 81 and y > -1 and y < 61:
        menu.clear()
        #Draw screen
        screen = turtle.Screen()
        screen.title("My Pong")
        screen.bgcolor("black")
        screen.setup(width=800, height=600)
        screen.tracer(0)

        # draw paddle 1
        paddle_1 = turtle.Turtle()
        paddle_1.speed(0)
        paddle_1.shape("square")
        paddle_1.color("white")
        paddle_1.shapesize(stretch_wid=5, stretch_len=1)
        paddle_1.penup()
        paddle_1.goto(-350, 0)

        # draw paddle 2
        paddle_2 = turtle.Turtle()
        paddle_2.speed(0)
        paddle_2.shape("square")
        paddle_2.color("white")
        paddle_2.shapesize(stretch_wid=5, stretch_len=1)
        paddle_2.penup()
        paddle_2.goto(350, 0)

        # draw ball
        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape("square")
        ball.color("white")
        ball.penup()
        ball.goto(0, 0)
        ball.dx = 0.25
        ball.dy = 0.25

        # score
        score_1 = 0
        score_2 = 0

        # head-up display
        hud = turtle.Turtle()
        hud.speed(0)
        hud.shape("square")
        hud.color("white")
        hud.penup()
        hud.hideturtle()
        hud.goto(0, 260)
        hud.write(
            "Player 1 | 0 : 0 | Player 2",
            align="center",
            font=("Press Start 2P", 24, "normal"))

        def restartgame():
            screen = turtle.bye()
            os.system("python3 pong.py")

        def paddle_1_up():
            y = paddle_1.ycor()
            if y < 250:
                y += 45
            else:
                y = 250
            paddle_1.sety(y)

        def paddle_1_down():
            y = paddle_1.ycor()
            if y > -250:
                y += -45
            else:
                y = -250
            paddle_1.sety(y)

        def paddle_2_up():
            y = paddle_2.ycor()
            if y < 250:
                y += 45
            else:
                y = 250
            paddle_2.sety(y)

        def paddle_2_down():
            y = paddle_2.ycor()
            if y > -250:
                y += -45
            else:
                y = -250
            paddle_2.sety(y)

        # keyboard
        screen.listen()
        screen.onkeypress(paddle_1_up, "w")
        screen.onkeypress(paddle_1_down, "s")
        screen.onkeypress(paddle_2_up, "Up")
        screen.onkeypress(paddle_2_down, "Down")

        # Change maximum score as you wish
        while score_1 < 10 and score_2 < 10:
            screen.update()

            # ball movement
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            # collision with the upper wall
            if ball.ycor() > 290:
                os.system("mpg123 bounce.mp3")
                ball.sety(290)
                ball.dy *= -1

            # collision with lower wall
            if ball.ycor() < -290:
                os.system("mpg123 bounce.mp3")
                ball.sety(-290)
                ball.dy *= -1

            # collision with left wall
            if ball.xcor() < -390:
                score_2 += 1
                hud.clear()
                hud.write("Player 1 | {} : {} | Player 2".format(score_1, score_2),
                          align="center", font=("Press Start 2P", 24, "normal"))
                os.system("mpg123 258020__kodack__arcade-bleep-sound.mp3")
                ball.goto(0, 0)
                ball.dx *= -1

            # collision with right wall
            if ball.xcor() > 390:
                score_1 += 1
                hud.clear()
                hud.write("Player 1 | {} : {} | Player 2".format(score_1, score_2),
                          align="center", font=("Press Start 2P", 24, "normal"))
                os.system("mpg123 258020__kodack__arcade-bleep-sound.mp3")
                ball.goto(0, 0)
                ball.dx *= -1

            # collision with the paddle 1
            if ball.xcor() == -329 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
                ball.dx *= -1
                os.system("mpg123 bounce.mp3")

            # collision with the paddle 2
            if ball.xcor() == 329 and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
                ball.dx *= -1
                os.system("mpg123 bounce.mp3")

        # Wipes de hud, shows/tells winner and restarts game
        # at will
        if score_1 > score_2:
            hud.clear()
            hud.write(
                "Player 1 Wins! Restart(Space)",
                align="center",
                font=("Press Start 2P", 24, "normal"))
            os.system("mpg123 Player_1_Wins.mp3")
            screen.listen()
            screen.onkeypress(restartgame, "space")
        else:
            hud.clear()
            hud.write(
                "Player 2 Wins! Restart(Space)",
                align="center",
                font=("Press Start 2P", 24, "normal"))
            os.system("mpg123 Player_2_Wins.mp3")
            screen.listen()
            screen.onkeypress(restartgame, "space")
        screen.mainloop()
menu.onscreenclick(buttonclick,1, True)
menu.listen()
menu.mainloop()