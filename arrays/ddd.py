a=[[5, 16],[0, 30], [15, 20]]
a=sorted(a)
count=1
for i in range(0,len(a)-1):
    if a[i][1]>a[i+1][0]:
        count+=1
    else:
        pass
print(count)