"""
* solar system | earth as a center
* __author__ = "Mohammed El Amine Idmoussi"
* Simulation of solar system following physics rules {Before Galileo}
"""

from vpython import *

scene = canvas(width=550, height=580)

ballY = sphere(pos=vec(0, 0, 0), color=color.yellow, radius=11 ** 10, make_trail=True)
ballG = sphere(pos=vec(70 * 10 ** 9, 0, 0), color=color.gray(0.8), radius=10 ** 10)
ballP = sphere(pos=vec(110 * 10 ** 9, 0, 0), color=color.purple, radius=10 ** 10)
earth = sphere(pos=vec(150 * 10 ** 9, 0, 0), color=color.blue, radius=10 ** 10)
mars = sphere(pos=vec(250 * 10 ** 9, 0, 0), color=color.red, radius=10 ** 10)

M = 2 * 10 ** 30
t = 0
dt = 19 * 3600

# tra = curve(radius=0.5)
ballG.vel = vec(0, 47 * 10 ** 3, 0)
ballP.vel = vec(0, 35 * 10 ** 3, 0)
earth.vel = vec(0, 30 * 10 ** 3, 0)
mars.vel = vec(0, 24 * 10 ** 3, 0)

# G = 6.7 * (1/10**11)*(M**3)
G = 6.7 * 10 ** (-11)
L = [ballG, ballP, earth, mars]

# scene.autoscale = False

while True:
    rate(100)
    for i in L:
        a = (-G * M / mag(i.pos) ** 3)
        i.vel = i.vel + i.pos * dt * a
        i.pos = i.pos + i.vel * dt
        scene.center = earth.pos
        # tra.append(pos=i.pos,retain=500)
