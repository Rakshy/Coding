a=-123
res=''
if bin(a)[0]=='-':
    res=res+'-'
    a=a*-1
while a>9:
    res=res+str(a%10)
    a=a//10
res=res+str(a)
print(res)