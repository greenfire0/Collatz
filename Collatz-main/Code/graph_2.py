global Param

def graph_a(a,Para):
    global Param
    Param = Para
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10,10))
    fig, ax = plt.subplots()
    fig.set_figheight(10)
    fig.set_figwidth(10)
    x,y = sort(a)
    ax.plot(x,y)

def color_picker(a):
    global Param
    red = 1
    blue = 0
    for c in Param:
        if a< c:
            return(red,0,blue, 0.25)
        red -= (1/len(Param))
        blue +=(1/len(Param))
    return(0,0,1, 0.5)

def sort(a):
    count =0
    array = [0]
    arr2 = [0]
    for num in a:
        
        if num%2 == 0:
            array.append(array[count-1]+1)
        else:
            array.append(array[count-1]-1)
        count+=1
        arr2.append(count)
    return(array,arr2)
        
