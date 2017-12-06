a=[1,1,2,2,2,2,4,6,7,9,9,9,10]
i=0
j=1
while (j<len(a)):
    if a[i]==a[j]:
        del a[j]
    else:
        i=j
        j+=1
print(a)

words='lcetcode'

blacklist='cod'
print(words)
print(blacklist)
words=list(words)
blacklist=list(blacklist)
print(set(words)&set(blacklist))