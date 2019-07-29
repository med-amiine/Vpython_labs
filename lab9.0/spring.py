"""
* spring
* __author__ = "Mohammed El Amine Idmoussi"
* Simulation of spring movements
"""

from vpython import *

scene = canvas()

ball1 = sphere(pos=vec(-5, 0, 0), raduis=0.2, color=color.blue)
ball2 = sphere(pos=vec(0, 0, 0), raduis=0.2, color=color.purple)
ball3 = sphere(pos=vec(5, 0, 0), raduis=0.2, color=color.white)

wallL = box(pos=vector(-10, 0, 0), size=vec(0.5, 8, 8), color=color.red)
wallR = box(pos=vector(10, 0, 0), size=vec(0.5, 8, 8), color=color.red)

helix1 = helix(pos=wallL.pos, axis=ball1.pos - wallL.pos, raduis=0.2, coils=10, thickness=0.05, color=color.magenta)
helix2 = helix(pos=ball1.pos, axis=ball2.pos - ball1.pos, raduis=0.2, coils=10, thickness=0.05, color=color.green)
helix3 = helix(pos=ball2.pos, axis=ball3.pos - ball2.pos, raduis=0.2, coils=10, thickness=0.05, color=color.orange)
helix4 = helix(pos=ball3.pos, axis=wallR.pos - ball3.pos, raduis=0.2, coils=10, thickness=0.05, color=color.yellow)

t = 0.005
m = 1
vel1 = vec(0, 0, 0)
vel2 = vec(0, 0, 0)
vel3 = vec(0, 0, 0)

r1 = vec(-5, 4, 0)
r2 = vec(0, 0, 0)
r3 = vec(5, -4, 0)

ball1.vel = vel1
ball2.vel = vel2
ball3.vel = vel3

while True:
    rate(1000)
    F1 = wallL.pos + r2 - 2 * r1
    F2 = r1 + r3 - 2 * r2
    F3 = r2 + wallR.pos - 2 * r3

    v1_new = vel1 + (F1 / m) * t
    v2_new = vel2 + (F2 / m) * t
    v3_new = vel3 + (F3 / m) * t

    r1_new = r1 + v1_new * t
    r2_new = r2 + v2_new * t
    r3_new = r3 + v3_new * t

    ball1.pos = r1_new
    ball1.vel = v1_new

    helix1.axis = ball1.pos - wallL.pos

    ball2.pos = r2_new
    ball2.vel = v2_new

    ball3.pos = r3_new
    ball3.vel = v3_new

    # helix1.axis = ball1.pos-wallL.pos

    helix2.pos = ball1.pos
    helix2.axis = ball2.pos - ball1.pos

    helix3.pos = ball2.pos
    helix3.axis = ball3.pos - ball2.pos

    helix4.pos = ball3.pos
    helix4.axis = wallR.pos - ball3.pos

    vel1 = v1_new
    vel2 = v2_new
    vel3 = v3_new

    r1 = r1_new
    r2 = r2_new
    r3 = r3_new
