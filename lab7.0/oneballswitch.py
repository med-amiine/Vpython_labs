from vpython import *
import numpy as np

scene = canvas(width=550,height=580)

ball = sphere(pos=vec(0,0,0),raduis=0.8,color=color.white)
temp = sphere(pos=vec(0,0,0),raduis=0.8)
temp.visible = False

wallR = box(pos=vec(5.7,0,0),size=vec(0.5,11,11),color=color.red)
wallL = box(pos=vec(-5.7,0,0),size=vec(0.5,11,11),color=color.purple)
wallT = box(pos=vec(0,5.7,0),size=vec(11,0.5,11),color=color.cyan)
wallB = box(pos=vec(0,-5.7,0),size=vec(11,0.5,11),color=color.magenta)
wallBk = box(pos=vec(0,0,-5.7),size=vec(11,11,0.5),color=color.orange)
wallF = box(pos=vec(0,0,5.7),size=vec(11,11,0.5))
wallF.visible = False

ball.vel = vector(np.random.uniform(),np.random.uniform(),np.random.uniform())
#ball.vel = vector (-0.15, -0.23, +0.27)

t = 0
dt = 0.06
#scene.autoscale = False
R = L = B = BK = T =  0
while True:
    rate(100)
    ball.pos = ball.pos + ball.vel*dt
    if ball.pos.x+ 1 >= wallR.pos.x:
        temp.color = ball.color
        ball.color = wallR.color
        wallR.color = temp.color
        ball.vel.x = -ball.vel.x
        R = R + 1
    elif ball.pos.x - 1  <= wallL.pos.x:
        temp.color = wallL.color
        ball.vel.x = -ball.vel.x
        wallL.color = ball.color
        ball.color = temp.color
        L = L+1
    elif ball.pos.y+ 1 >= wallT.pos.y:
        temp.color = wallT.color
        ball.vel.y = -ball.vel.y
        wallT.color = ball.color
        ball.color = temp.color
        T = T + 1
    elif ball.pos.y - 1 <= wallB.pos.y:
        temp.color = wallB.color
        ball.vel.y = -ball.vel.y
        wallB.color = ball.color
        ball.color = temp.color
        B = B+1
    elif ball.pos.z + 1 <= wallBk.pos.z:
        temp.color = wallBk.color
        ball.vel.z = -ball.vel.z
        wallBk.color = ball.color
        ball.color = temp.color
        BK = BK + 1
    elif ball.pos.z + 1 >= wallF.pos.z:
        ball.vel.z = -ball.vel.z
    if R == 30:
        print("stop")
        break
    t =t+dt

print("Right :",R)
print("Left :",L)
print("Bottom :",B)
print("Top :",T)
print("Background :",BK)
print(t)
