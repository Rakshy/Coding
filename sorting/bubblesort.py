a=[8,4,-2,-31,5,-108,-43,26,29,45]
change=True
for x in range(0,len(a)):
    if change==True:
        change=False
    else:
        print('sorted')
        break
    for i in range(0,len(a)):
        try:
            if a[i]>a[i+1]:
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
                change=True
        except:
            break
print(a)