a=[1,2,3,4,5,6,7,8,89]
mid=len(a)//2
start=0
end=len(a)-1
target=1
print(a)
while(start!=end):
    if target<a[0] or target>a[-1]:
        print('Not found')
        break
    if target==a[0]:
        print(0)
        break
    if mid == start:
        mid+=1
    if a[mid]==target:
        print(mid)
        break
    if a[mid]<target:
        start=mid
        mid=(start+end)//2
    else:
        end=mid
        mid = (start + end) // 2
if start==end:
    print('Not found')