from vpython import *

scene = canvas()

nb_balls = 10
list_balls = []
list_helix = []
vnewList = []
forceList = []

wallL = box(pos=vector(-15,0,0), size=vec(0.5,8,8), color=color.red)
wallR = box(pos=vector(30,0,0), size=vec(0.5,8,8), color=color.red)

x = -10 + nb_balls
for i in range (-4,nb_balls):
    step1 = i *2
    list_balls.append(sphere(pos=vec((i+step1),0,0),raduis=0.02))

helix1 = helix(pos=wallL.pos,axis=list_balls[0].pos-wallL.pos,raduis=0.2, coils=10,thickness=0.05, color=color.magenta)

for j in list_balls:
    list_helix.append(helix(pos=vec(j.pos),axis=(j+1).pos-i.pos,raduis=0.2, coils=10,thickness=0.05))

last = len(list_balls)
helix4 = helix(pos=list_balls[last].pos,axis=wallR.pos-list_balls[last].pos,raduis=0.2, coils=10,thickness=0.05, color=color.yellow)

t = 0.005
m = 1
vel=vec(0,0,0)


r1= vec(-5,4,0)
r2= vec(0,0,0)
r3= vec(5,-4,0)

for i in list_balls:
    i.vel = vel+i

# while i <nb_balls-1:
#     f =











