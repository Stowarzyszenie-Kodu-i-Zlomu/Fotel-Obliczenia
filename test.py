import numpy as np
import matplotlib.pyplot as plt

#dodaj punkty
p1 = [0,10,0]
p2 = [-5,-5,0]
p3 = [5,-5,0]
#wysokosci
h1 = 50
h2 = 52
h3 = 40
#grubość kolumn
thickness = 0.5

#pozycje xyz poczatkow wykresow
xpos=[p1[0],p2[0],p3[0]]
ypos=[p1[1],p2[1],p3[1]]
zpos=[p1[2],p2[2],p3[2]]

#wymiary wykresow
dx = [thickness]
dy = [thickness]
dz = [h1,h2,h3]

#to po prostu trzeba dodac by dzialalo
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#dodanie wykresow z zadanymi parametrami do obrazu
ax.bar3d(xpos,ypos,zpos,dx,dy,dz)

#dodanie opisow osi
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')


plt.show()