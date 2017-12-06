list1=[0,3,5]
list2=[1,6,7]
list3=[2,8,10]
big=[list1]+[list2]+[list3]
import numpy as np
t=np.transpose(big)
print(t)
hehe=[]
import heapq as hh
for each in t[0]:
    hh.heappush(hehe,each)
print(hehe)