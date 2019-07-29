"""
* collision detected
* __author__ = "Mohammed El Amine Idmoussi"
* Multiple balls are thrown randomly and we are detecting collision to the infinity ∞
"""

from vpython import *
import numpy as np
from vpython import sphere

scene = canvas(width=550, height=580)
wallR = box(pos=vec(12, 0, 0), size=vec(1, 25, 25), color=color.red)
wallL = box(pos=vec(-12, 0, 0), size=vec(1, 25, 25), color=color.purple)
wallT = box(pos=vec(0, 12, 0), size=vec(25, 1, 25), color=color.cyan)
wallB = box(pos=vec(0, -12, 0), size=vec(25, 1, 25), color=color.magenta)
wallBk = box(pos=vec(0, 0, -12), size=vec(25, 25, 1), color=color.orange)
wallF = box(pos=vec(0, 0, 12), size=vec(25, 25, 1))
wallF.visible = False
wallR.visible = False
wallL.visible = False
wallT.visible = False
wallB.visible = False
wallBk.visible = False

Bball = sphere(pos=vec(0, 0, 0), raduis=300, color=color.blue)
Bball.vel = vector(np.random.uniform(), np.random.uniform(), 0)
Bball.visible = False
temp = sphere(pos=vec(0, 0, 0), raduis=0.5)
temp.visible = False
t = 0
dt = 0.05
L = []
m = 1
counter = 0
for i in range(-3, 2):
    for j in range(-3, 2):
        r = np.random.uniform(1, 3)
        L.append(sphere(pos=vec(i, j, 0), raduis=r))

for i in L:
    x = np.random.uniform(0, 1)
    y = np.random.uniform(0, 1)
    z = np.random.uniform(0, 1)
    i.color = vec(x, y, z)

# i.vel = vector(np.random.uniform(),np.random.uniform(),np.random.uniform())

for i in L:
    i.vel = vector(np.random.uniform(), np.random.uniform(), 0)

scene.autoscale = False

while True:
    rate(50)
    for i in L:
        for j in L:
            rn2 = i.pos + i.vel * dt
            rn1 = j.pos + j.vel * dt
            rnb = Bball.pos + Bball.vel * dt
            i.pos = i.pos + i.vel * dt
            if mag(rn1 - rn2) < (j.radius + i.radius):
                print("collision detected")
                a = mag2(i.vel - j.vel)
                b = dot(-2 * (rn1 - rn2), i.vel - j.vel)
                c = mag2(rn1 - rn2) - (i.radius + j.radius) ** 2
                d = b ** 2 - 4 * a * c
                counter += 1
                if d > 0 or a != 0:
                    dt2 = (-b + sqrt(d)) / 2 * a
                    old_rn1 = rn1 - i.vel * dt2
                    old_rn2 = rn2 - j.vel * dt2
                    # calculation of vn1
                    pi1 = 2  # i.vel - (2 * (j.radius* m)/(i.radius * m + j.radius * m))
                    pi2 = dot(i.vel - j.vel, (old_rn1 - old_rn2) / mag(old_rn1 - old_rn2))
                    pi3 = (old_rn1 - old_rn2) / mag(old_rn1 - old_rn2)
                    vn1 = pi1 * pi2 * pi3
                    # calculation of vn2
                    pi1 = 2  # j.vel + (2 * (i.radius* m)/(i.radius * m + j.radius * m))
                    pi2 = dot(i.vel - j.vel, (old_rn1 - old_rn2) / mag(old_rn1 - old_rn2))
                    pi3 = (old_rn1 - old_rn2) / mag(old_rn1 - old_rn2)
                    vn2 = pi1 * pi2 * pi3
                    i.pos = old_rn1 + vn1 * dt2
                    j.pos = old_rn2 + vn2 * dt2
                elif i.pos.x >= wallR.pos.x:
                    i.vel.x = -i.vel.x
                elif j.pos.x >= wallR.pos.x:
                    j.vel.x = -j.vel.x
                elif i.pos.x <= wallL.pos.x:
                    i.vel.x = -i.vel.x
                elif j.pos.x <= wallL.pos.x:
                    j.vel.x = -j.vel.x
                elif i.pos.y >= wallT.pos.y:
                    i.vel.y = -i.vel.y
                elif j.pos.y >= wallT.pos.y:
                    j.vel.y = -j.vel.y
                elif i.pos.y <= wallB.pos.y:
                    i.vel.y = -i.vel.y
                elif j.pos.y <= wallB.pos.y:
                    j.vel.y = -j.vel.y
                elif i.pos.z <= wallBk.pos.z:
                    i.vel.z = -i.vel.z
                elif j.pos.z <= wallBk.pos.z:
                    j.vel.z = -i.vel.z
                elif i.pos.z + 5 >= wallF.pos.z:
                    i.vel.z = -i.vel.z
                elif j.pos.z + 5 >= wallF.pos.z:
                    j.vel.z = -j.vel.z
    t = t + dt

    # elif mag(rn1- rnb ) < (Bball.radius + i.radius):
    #     print("Big collision detected")
