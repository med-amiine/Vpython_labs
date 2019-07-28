from vpython import *
import numpy as np

scene = canvas(width=550,height=580)

ball = sphere(pos=vec(0,0,0),raduis=0.8,color=color.white)

wallR = box(pos=vec(5.7,0,0),size=vec(0.5,11,11),color=color.red)
wallL = box(pos=vec(-5.7,0,0),size=vec(0.5,11,11),color=color.purple)
wallT = box(pos=vec(0,5.7,0),size=vec(11,0.5,11),color=color.cyan)
wallB = box(pos=vec(0,-5.7,0),size=vec(11,0.5,11),color=color.magenta)
wallBk = box(pos=vec(0,0,-5.7),size=vec(11,11,0.5),color=color.orange)
wallF = box(pos=vec(0,0,5.7),size=vec(11,11,0.5),color=color.black)
wallF.visible = False

ball.vel = vector(np.random.uniform(),np.random.uniform(),np.random.uniform())
#ball.vel = vector (-0.15, -0.23, +0.27)

t = 0
dt = 0.006

#scene.autoscale = False

while True:
    rate(3000)
    ball.pos = ball.pos + ball.vel*dt
    if ball.pos.x+ 1 >= wallR.pos.x:
        ball.vel.x = -ball.vel.x
        ball.color = wallR.color
    elif ball.pos.x - 1  <= wallL.pos.x:
        ball.vel.x = -ball.vel.x
        ball.color = wallL.color
    elif ball.pos.y+ 1 >= wallT.pos.y:
        ball.vel.y = -ball.vel.y
        ball.color = wallT.color
    elif ball.pos.y - 1 <= wallB.pos.y:
        ball.vel.y = -ball.vel.y
        ball.color = wallB.color
    elif ball.pos.z <= wallBk.pos.z:
        ball.vel.z = -ball.vel.z
        ball.color = wallBk.color
    elif ball.pos.z >= wallF.pos.z:
        ball.vel.z = -ball.vel.z


t =t+dt
