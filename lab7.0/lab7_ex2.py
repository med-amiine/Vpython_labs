from vpython import *
import numpy as np
from vpython import sphere

scene = canvas(width=550,height=580)
temp = sphere(pos=vec(0,0,0),raduis=0.5)
temp.visible = False
wallR = box(pos=vec(12,0,0),size=vec(1,25,25),color=color.red)
wallL = box(pos=vec(-12,0,0),size=vec(1,25,25),color=color.purple)
wallT = box(pos=vec(0,12,0),size=vec(25,1,25),color=color.cyan)
wallB = box(pos=vec(0,-12,0),size=vec(25,1,25),color=color.magenta)
wallBk = box(pos=vec(0,0,-12),size=vec(25,25,1),color=color.orange)
wallF = box(pos=vec(0,0,12),size=vec(25,25,1))
wallF.visible = False

#i.vel = vector (-0.15, -0.23, +0.27)

t = 0
dt = 0.05
L = []

for i in range(-2,2):
    for j in range(-2,2):
        L.append(sphere(pos=vec(i,j,0),raduis=0.4))

for i in L:
    x = np.random.uniform(0,1)
    y = np.random.uniform(0,1)
    z = np.random.uniform(0,1)
    i.color = vec(x, y, z)

#i.vel = vector(np.random.uniform(),np.random.uniform(),np.random.uniform())
for i in L:
    i.vel = vector(np.random.uniform(),np.random.uniform(),np.random.uniform())
scene.autoscale = False
while True:
    rate(500)
    for i in L:
        i.pos = i.pos + i.vel*dt
        if i.pos.x + 2 >= wallR.pos.x:
            temp.color = i.color
            i.color = wallR.color
            wallR.color = temp.color
            i.vel.x = -i.vel.x
        elif i.pos.x - 2 <= wallL.pos.x:
            temp.color = wallL.color
            i.vel.x = -i.vel.x
            wallL.color = i.color
            i.color = temp.color
        elif i.pos.y+ 2 >= wallT.pos.y:
            temp.color = wallT.color
            i.vel.y = -i.vel.y
            wallT.color = i.color
            i.color = temp.color
        elif i.pos.y - 2 <= wallB.pos.y:
            temp.color = wallB.color
            i.vel.y = -i.vel.y
            wallB.color = i.color
            i.color = temp.color
        elif i.pos.z <= wallBk.pos.z:
            temp.color = wallBk.color
            i.vel.z = -i.vel.z
            wallBk.color = i.color
            i.color = temp.color
        elif i.pos.z + 5 >= wallF.pos.z:
            i.vel.z = -i.vel.z
