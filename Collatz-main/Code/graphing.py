import matplotlib.pyplot as plt
from graph_2 import sort
import numpy as np
from stupid import get_q
from scipy.interpolate import make_interp_spline
from scipy.ndimage.filters import gaussian_filter1d
import matplotlib as mpl

global Param
import math
Param = []



plt.figure(figsize=(10,10))

fig, ax = plt.subplots()
ax = plt.gca()
#ax.axes.xaxis.set_visible(False)
#ax.axes.yaxis.set_visible(False)
fig.set_figheight(10)
fig.set_figwidth(10)
ax.set_facecolor('black')
   # Borders


plt.ylim([21,101])
plt.xlim([-6.1, 1.5])




def printPaths(root):

    path = []
    printPathsRec(root, path, 0)
def printPathsRec(root, path, pathLen):
     
    # Base condition - if binary tree is
    # empty return
    if root is None:
        return
 
    # add current root's data into
    # path_ar list
     
    # if length of list is gre
    if(len(path) > pathLen):
        path[pathLen] = root.data
    else:
        path.append(root.data)
 
    # increment pathLen by 1
    pathLen = pathLen + 1
 
    if root.left is None and root.right is None:
         
        # leaf node then print the list
        printArray(path, pathLen)
    else:
        # try for left and right subtree
        printPathsRec(root.left, path, pathLen)
        printPathsRec(root.right, path, pathLen)
def printArray(ints, len):

    a = []
    for i in ints[0 : len]:
        a.append(i)
    graph(a)
def start_graph(root,arr):
    global Param
    Param = arr
    printPaths(root)
    plt.show()
   

def color_picker(a):

    global Param
    red = 1
    blue = .3
    for c in Param:
        if a< c:
            return(red,0,blue, 0.1)
        red -= (0.9/len(Param))
        blue +=(0.4/len(Param))
    return(red,0,blue, 0.2)
def nat_picker2(a):
    Param  = get_q(50)
    r = [0.7,0.5]
    g = [0.2,0.1]
    b = [0.4,0.6]
    

    #b = [0.6,0.2]
    #g = [0.3,0.7]
    
 
    red = r[0]
    green = g[0]
    blue = b[0]
    
    count = 0
    for c in Param:
        if a< c:
            return red,green,blue,0.07
        count+=1
        red +=  (r[1]-r[0])/a
        green +=  (g[1]-g[0])/a
        blue +=  (b[1]-b[0])/a
    return(red,blue,green,0.4)

def nat_picker3(a):
    color_list = ['#004c4c','#006666','#008080','#66b2b2','#00665c','#538585','#8eb8b8']
    color_list = ['#606c38','#283618', '#fefae0','#dda15e','#bc6c25']
    color_list = ['#cad2c5', '#84a98c','#52796f','#354f52','#2f3e46']
    color_list = ['#223843','#eff1f3','#dbd3d8','#d8b4a0','#d77a61']
    color_list = ['#102F25','#2E4D43','#718879','#C4D0CD','#DDD6D3','#B5AEAB']
    color_list = ['#291C2A','#E0C5C8','#F4E4E4','#F0E1DA']
    Param  = get_q(len(color_list))
    


    count = 0
    for c in Param:
        if a< c:
            return color_list[count]
        count+=1
    return '#00665c'

def graph(a):
    #x,y = trans(a)
    x,y = sort2(a)
    ax.set_xlim([-2,0.5])
    ax.set_ylim(-0.5,40)
    ax.plot(x,y, color = color_picker(len(a)))

def graph_a(a):
    x,y = sort(a)
    ysmoothed = gaussian_filter1d(y, sigma=1)
    xsmoothed = gaussian_filter1d(x, sigma=1)

    ax.plot(xsmoothed,ysmoothed, color = color_picker(len(x)))
    ax.plot(x,y, color = color_picker(len(x)))

def graph_b(a):
    x,y = sort2(a)
    ax.plot(x,y, color = nat_picker2(len(a)))  
def graph_c(a):
    #x,y = trans(a)
    x,y = sort2(a)
    ax.plot(x,y, color = nat_picker3(len(a)))  



def sort(a):
    seq=[0]
    val=[0]
    rad=0
    even=-.6* (math.pi / 180 )   
    odd = 1.17* (math.pi / 180 )
    ##this sets the rotation of the point and how much it shifts

    for i in range(1, len(a)):
        if a[i]%2==0:
            seq.append(seq[i-1]+math.sin(rad+even))
            rad=rad+even            
        else:
            seq.append(seq[i-1]+math.sin(rad+odd))
            rad=rad+odd
        val.append(val[i-1]+math.cos(rad))
    return val, seq

def sort2(a):
    seq=[0]
    val=[0]
    rad=0
    even=-.60* (math.pi / 180 )   
    odd = 1.17* (math.pi / 180 )
    ##this sets the rotation of the point and how much it shifts

    for i in range(1, len(a)):
        if a[i]%2==0:
            seq.append(seq[i-1]+math.sin(rad+even))
            rad=rad+even            
        else:
            seq.append(seq[i-1]+math.sin(rad+odd))
            rad=rad+odd
        val.append(val[i-1]+math.cos(rad))
    xnew = np.linspace(min(val), max(val), 200) 
    spl = make_interp_spline(val, seq, k=5)
    y_smooth = spl(xnew)
    return y_smooth,xnew