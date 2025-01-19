import turtle,random
choice=input("Type 'draw' for drawing, 'rps' for rock paper scissors or 'game' for the game: ").lower()
if choice=='draw':
    print('Use arrow keys to move, space to lift/put-down your pen, and r to reset the board!!!')
    pencil=turtle.Turtle()
    screen=turtle.Screen()
    x=0
    def left():pencil.left(30)
    def right():pencil.right(30)
    def up():pencil.forward(15)
    def down():pencil.backward(15)
    def space():
        global x
        pencil.penup() if x%2==0 else pencil.pendown()
        x+=1
    def reset():screen.reset()
    screen.listen()
    screen.onkey(left,'Left')
    screen.onkey(right,'Right')
    screen.onkey(up,'Up')
    screen.onkey(down,'Down')
    screen.onkey(space,'space')
    screen.onkey(reset,'r')
    turtle.done()

elif choice=='game':
    screen=turtle.Screen()
    player=turtle.Turtle()
    screen.setup(600,600)
    try:
        screen.bgpic("space.gif")
        turtle.register_shape("player.gif")
        turtle.register_shape("fire.gif")
        turtle.register_shape("enemy.gif")
    except:print("Make sure files are in the same folder.")

    player.shape("player.gif")
    player.setheading(90)
    player.penup()
    player.goto(0,-250)
    player_speed=20
    bullet=turtle.Turtle()
    bullet.shape("fire.gif")
    bullet.setheading(90)
    bullet.penup()
    bullet.goto(0,-240)
    show_bullet=False
    bullet_speed=100
    def left():player.setx(player.xcor()-player_speed)
    def right():player.setx(player.xcor()+player_speed)
    def up():player.sety(player.ycor()+player_speed)
    def down():player.sety(player.ycor()-player_speed)
    def shoot():
        global show_bullet
        bullet.goto(player.xcor(),player.ycor()+20)
        show_bullet=True
    def bullet_move():
        if show_bullet:bullet.sety(bullet.ycor()+bullet_speed)
    screen.listen()
    screen.onkey(left,'Left')
    screen.onkey(right,'Right')
    screen.onkey(up,'Up')
    screen.onkey(down,'Down')
    screen.onkey(shoot,'space')
    enemy=turtle.Turtle()
    enemy.shape("enemy.gif")
    enemy.penup()
    x=random.randint(-280,280)
    enemy.goto(x,180)
    score=0
    while True:
        if show_bullet:bullet_move()
        enemy.sety(enemy.ycor()-1)
        if enemy.ycor()<-300:enemy.goto(random.randint(-280,280),180)
        if bullet.ycor()>300:show_bullet=False;bullet.goto(0,-240)
        if enemy.distance(bullet)<40:
            score+=1
            print(f"Score:{score}")
            enemy.goto(random.randint(-280,280),180)
        if score>=10:print("You win!");break
    turtle.done()
elif choice=='rps':
    com=random.choice(['Rock','Paper','Scissors'])
    user=input('Choose, rock, paper, or scissors!!!').lower()
    if com=='Rock' and user=='scissors':
        print('Ha I win I chose rock and you chose scissors')
    elif com=='Scissors' and user=='rock':
        print('No I lost, I chose scissors when you chose rock')
    elif com=='Paper' and user=='rock':
        print('Ha I win I chose paper and you chose rock')
    elif com=='Rock' and user=='paper':
        print('No I lost I chose rock and you chose paper')
    elif com=='Scissors' and user=='paper':
        print('Ha I win I chose scissors and you chose paper')
    elif com=='paper' and user=='scissors':
        print('No I lost I chose paper and you chose scissors')
    else:
        print(f'It is a draw we both chose {com}')