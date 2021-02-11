from math import sin, cos, tan, pi, acos, atan
import matplotlib.pyplot as plt
l1 =1
l2=1

xa=0.5
ya=0.0

xb=1.5
yb=0.8

def fk(q1,q2):
    x1=l1 * cos(q1)
    y1=l1* sin(q1)
    x2= x1 +l2 *cos(q1 + q2)
    y2 = y1 + l2 * sin(q1 +q2)
    return (x1, y1, x2, y2)

def draw_robot(q1, q2):
    x1, y1, x2, y2 =fk(q1, q2)
    plt.axis('equal')
    plt.plot([0,x1,x2], [0,y1,y2], 'o-')
    #plt.show()

def ik(x, y, l1, l2):
    q2= acos(( (x**2)+(y**2)-(l1**2)-(l2**2) )/ (2*l1*l2) )
    q1 = atan(y/x) - atan((l2 *sin(q2))/(l1+l2*cos(q2)))
    return (q1, q2)

def interpolate(a,b,i,N=10):
    return( ((b-a)/(N))*i+a)

q1a ,q2a =ik(xa, ya, l1, l2)
draw_robot(q1a,q2a)

q1b ,q2b =ik(xb, yb, l1, l2)
draw_robot(q1b,q2b)

for i in range(0,10):
    q1= interpolate(q1a, q1b, i, 10)
    q2= interpolate(q2a, q2b, i, 10)
    draw_robot(q1,q2)
plt.show()

for i in range(0, 10):
    x=interpolate(xa, xb,i, 10)
    y=interpolate(ya, yb,i, 10)
    q1 ,q2 =ik(x, y, l1, l2)
    draw_robot(q1,q2)
