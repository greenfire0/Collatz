import numpy as np
import matplotlib.pyplot as plt


def color_picker():
    return np.random.choice(['#FF5E02','red', 'blue','#6400FF','#E10060','#02D1FF'])


def transforms(x):
    seq=[0]
    val=[0]
    rad=0
    even=-.54* (np.pi / 180 )   
    odd = 1.2* (np.pi / 180 )
    ##this sets the rotation of the point and how much it shifts

    for i in range(1, len(x)):
        if x[i]%2==0:
            seq.append(seq[i-1]+np.sin(rad+even))
            rad=rad+even            
        else:
            seq.append(seq[i-1]+np.sin(rad+odd))
            rad=rad+odd
        val.append(val[i-1]+np.cos(rad))
    ##this applies the value to the sequence
    ##this math leads to nice patterns for some reason
    return val,seq

plt.figure(figsize=(10,10))
fig, ax = plt.subplots()
fig.set_figheight(10)
fig.set_figwidth(10)


def collatz(a):
        pl3 = []
        y=a
        while y!= 1:
            pl3.append(int(y)) 
            if y%2 == 0:
                y = y/2
            else: 
                y = y*3 +1
        pl3.append(1)
        return [ele for ele in reversed(pl3)]
    

runs=2000
seen = {}
sequence_lengths=[]


for i in range(1, runs):
    length = collatz(i)    
    sequence_lengths.append(length)
    x,y = transforms(np.array(length))
    ##picks random colors
    ax.plot(x,y, alpha=0.15, color=color_picker());     
plt.show()