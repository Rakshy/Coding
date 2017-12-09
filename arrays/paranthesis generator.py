
def generateparanthesis(n):
    li=['{}']
    for i in range(0,n-1):
        temp=[]
        for item in li:
            s1=item+'{}'
            s2='{}'+item
            s3='{'+item+'}'
            temp.append(s1)
            temp.append(s2)
            temp.append(s3)
        li=[item for item in temp] #Deep copy
        del li[0]
    return li

print(generateparanthesis(2))