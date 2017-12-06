a='leetcoe'
b='cod'
a=list(a)
b=list(b)
i=0
j=0
count=0
while(i<len(a)):
    if a[i]==b[j]:
        i+=1
        j+=1
        count += 1
        if count==len(b):
            print(i-len(b))
            break
    else:
        count=0
        i+=1
if (i==len(a)):
    print('No')
