s=612216
y=s
res=1221%10
s=round(s/10)
while(s/res!=1):
    temp=s%10
    s=round(s/10)
    res=(10*res)+temp
    if s<10:
        print('Not a palindrome')
        break
print('Is a palindrome')
