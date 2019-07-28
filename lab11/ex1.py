from vpython import *
import numpy as np
import math as m

scene = canvas(width=550,height=700)

pi = m.pi
t=0
f1= pi
t1= pi -0.1

f2= pi
t2= pi -0.1

dt = 0.001

L = 4



v1F = 0
v1T = 0
a1F = 0
a1T = 0

v2F = 0
v2T = 0
a2F = 0
a2T = 0

G1=9.8
G2=9.800000000001

ballA = sphere(pos=vec(L*sin(f1),-L*cos(f1),0), radius = 0.2, color=color.white)
ballB = sphere(pos=vec(L*(sin(f1)+sin(t2)) , -L*(cos(f1)+cos(t1)),0),radius = 0.2, color=color.white)

ballX = sphere(pos = vec(L*sin(f2),-L*cos(f2),0), radius = 0.2, color=color.blue)
ballY = sphere(pos = vec(L*(sin(f2)+sin(t2)) , -L*(cos(f2)+cos(t2)),0), radius = 0.2, color=color.blue)

cylA = cylinder(pos = vec(0,0,0), axis = ballA.pos,length = L, radius = 0.02,color = color.magenta)
cylB = cylinder(pos = vec(ballA.pos.x,ballA.pos.y,0), axis = ballB.pos,length = L,radius = 0.02,color = color.magenta)

cylX = cylinder(pos = vec(0,0,0), axis = ballX.pos,length = L, radius = 0.02,color = color.yellow)
cylY = cylinder(pos = vec(ballX.pos.x,ballX.pos.y,0), axis = ballY.pos,length = L,radius = 0.02,color = color.yellow)

while(True):

    rate(4000)
    p1 = (1 + (sin(f1-t1)**2))
    a1F =  ((-G1/L)*(2*sin(f1)-sin(t1)*cos(f1-t1)) - 0.5*(v1F**2)*sin(2*f1 - 2*t1) - (v1T**2)*sin(f1-t1))/p1
    p2 = (1 + (sin(f1-t1)**2))
    a1T = ((-G1/L)*(2*sin(t1)-2*sin(f1)*cos(f1-t1)) + 0.5*(v1T**2)*sin(2*f1 - 2*t1) + 2*(v1F**2)*sin(f1-t1))/p2


    v1F= v1F + a1F*dt
    v1T= v1T + a1T*dt

    f1 = f1 + v1F*dt
    t1 = t1 + v1T*dt

    ballA.pos = vec(L*sin(f1),-L*cos(f1),0)
    ballB.pos = vec(ballA.pos.x + L*sin(t1),ballA.pos.y - L*cos(t1),0)

    cylA.axis = ballA.pos
    cylB.pos = vec(ballA.pos.x,ballA.pos.y,0)
    cylB.axis = ballB.pos-ballA.pos

    p3=(1 + (sin(f2-t2)**2))
    a2F =  ((-G2/L)*(2*sin(f2)-sin(t2)*cos(f2-t2)) - 0.5*(v2F**2)*sin(2*f2 - 2*t2) - (v2T**2)*sin(f2-t2))/p3
    p4 = (1 + (sin(f2-t2)**2))
    a2T = ((-G2/L)*(2*sin(t2)-2*sin(f2)*cos(f2-t2)) + 0.5*(v2T**2)*sin(2*f2 - 2*t2) + 2*(v2F**2)*sin(f2-t2))/p4


    v2F= v2F + a2F*dt
    v2T= v2T + a2T*dt

    f2 = f2 + v2F*dt
    t2 = t2 + v2T*dt

    ballX.pos = vector(L*sin(f2),-L*cos(f2),0)
    ballY.pos = vector(ballX.pos.x + L*sin(t2),ballX.pos.y - L*cos(t2),0)

    cylX.axis = ballX.pos
    cylY.pos = vector(ballX.pos.x,ballX.pos.y,0)
    cylY.axis = ballY.pos-ballX.pos

