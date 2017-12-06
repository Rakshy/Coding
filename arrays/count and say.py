#https://leetcode.com/problems/count-and-say/description/
a='21'
a=list(a)
i=0
count=1
j=1
res=''
while j<len(a):
    if a[i]==a[j]:
        count+=1
        j+=1
    else:
        res=res+str(count)+str(a[i])
        i=j
        j=i+1
        count=1
res=res+str(count)+str(a[i])
print(res)