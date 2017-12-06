def mergesort(array):
    if len(array)==1:
        return array

    if len(array)>1:
        l=array[0:len(array)//2]
        r=array[len(array)//2:]
        left=mergesort(l)
        right=mergesort(r)
        sorted=helper(left,right)
    return sorted

def helper(left,right):
    sorted=[]
    while len(left) and len(right):
        if left[0]<=right[0]:
            sorted.append(left[0])
            del left[0]
        else:
            sorted.append(right[0])
            del right[0]
    if len(left)==0:
        sorted=sorted+right
        return sorted
    else:
        sorted = sorted + left
        return sorted

a=[38,27,43,3,9,82,10]
print(mergesort(a))
