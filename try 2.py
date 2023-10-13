

###########startup



import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



fig = plt.figure(figsize=(10, 10))
axes = fig.add_subplot(111, projection="3d")
randomcolors = ["blue","red","green","orange","purple","violet","pink"]



dt = 10**15 #timestep increment in seconds
n = 0 #timestep number
ne = 200 #timestep number end
G = 6.6743*(10**-11) #G in base units
E = 1000000 #softening constant



N = 5 #number of bodies
R = 100000000000000000000 #sphere volume radius
V = 47000 #max start velocity m/s
Mmin = 13000000000000000000000 #min weight
M = 1900000000000000000000000000 #max weight



planets = {} 
force_x = np.zeros((N,N))
force_y = np.zeros((N,N))
force_z = np.zeros((N,N))



def inter(r1,r2,m1,m2):
    return (-G*m1*m2*((r1-r2)/(((r1-r2)**2)+E**2)**1.5))



def KE(vx,vy,vz,m):
    return (0.5*m*((vx**2+vy**2+vz**2)**0.5))
    
#def PE():
    
class bodies:
    def __init__(self,x,y,z,vx,vy,vz,m,color):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.m = m
        self.color = color

        
        
for i in range (0,N):
    x = random.randrange(-R,R,2*R/N)
    y = random.randrange(-R,R,2*R/N)
    z = random.randrange(-R,R,2*R/N)
    vx = random.randint(-V,V)
    vy = random.randint(-V,V)
    vz = random.randint(-V,V)
    m = random.randint(Mmin,M)
    color = random.choice(randomcolors)
    planets[i] = bodies(x,y,z,vx,vy,vz,m,color)
    axes.scatter(planets[i].x, planets[i].x, planets[i].z, c=planets[i].color, marker='o') 
  
  

    
#################active after
    
    
for timer in range(0,ne):
    
    for i in range(0,N):
        j=0
        while j < i:
            force_x[j][i] = inter(planets[i].x,planets[j].x,planets[i].m,planets[j].m)
            force_x[i][j] = -force_x[j][i]
            j+=1
    for i in range(0,N):
        j=0
        while j < i:
            force_y[j][i] = inter(planets[i].y,planets[j].y,planets[i].m,planets[j].m)
            force_y[i][j] = -force_y[j][i]
            j+=1
    for i in range(0,N):
        j=0
        while j < i:
            force_z[j][i] = inter(planets[i].z,planets[j].z,planets[i].m,planets[j].m)
            force_z[i][j] = -force_z[j][i]
            j+=1
        
        
        
    for i in range(0,N):
        planets[i].x += -planets[i].vx*dt
        planets[i].y += -planets[i].vy*dt
        planets[i].z += -planets[i].vz*dt

    
    
    for i in range(0,N):
        planets[i].vx += sum(force_x[i])*dt/(planets[i].m)
        planets[i].vy += sum(force_y[i])*dt/(planets[i].m)
        planets[i].vz += sum(force_z[i])*dt/(planets[i].m)
    
    for i in range(0,N):
        axes.scatter(planets[i].x, planets[i].x, planets[i].z, c=planets[i].color, marker='o') 
        
        
        
