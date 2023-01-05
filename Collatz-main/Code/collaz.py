from matplotlib import pyplot as plt
from datetime import datetime
import pandas as pd


count =0

pl3 = []

for b in range (1,10):
    for a in range((b*100)-99,b*100):

        y=a 
        while y!= 2:
            pl3.append(int(y))
            if y%2 == 0:
                y = y/2
            else: 
                y = y*3 +1


res = []
test_list = pl3
for i in test_list:
    if i not in res:
        res.append(i)
print(res)