from vpython import *
import numpy as np

scene = canvas(width=550,height=580)

L = []

for i in range(-3,4):
    for j in range(-3,4):
        L.append(sphere(pos=vec(i,j,0),raduis=0.4))
for i in L:
    i.vel = vector(np.random.uniform(),np.random.uniform(),np.random.uniform())

dt = 0.6

while True:
    rate(1)
    for i in L:
        x = np.random.uniform(0,1)
        y = np.random.uniform(0,1)
        z = np.random.uniform(0,1)
        i.color = vec(x, y, z)
        for i in L:
            i.pos = i.pos + i.vel*dt
