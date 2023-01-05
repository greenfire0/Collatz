from nade import Node
#from turtle_graphing import  printPaths
from graphing import start_graph
import pandas as pd
root = Node(4)
root.insert([16,8,4,2,1])
def get_quantile(df,parts):
    
    arrau = []
    for a in range(1,parts+1):
        arrau.append(df.quantile(q = (a/parts)).iloc[0])
    return arrau

def create_collatz(a,c):
    hold = []


    for b in range (a,c):
        pl3 = []
        y=b
        while y!= 4:
            pl3.append(int(y)) 
            if y%2 == 0:
                y = y/2
            else: 
                y = y*3 +1
        hold.append(pl3)
    return hold




arr = []
for a in create_collatz(1,2000):

    arr.append(len(a))
    root.insert(a)
start_graph(root,get_quantile(pd.DataFrame(arr),parts=50))

##work with colors

#root.display()    #printPaths(root) #root.traverse()
