hehe=['leets','leetcode','leet','leeds','leemans','leetiole','leephone']

def func(arr):
    if len(arr)==2:
        comb_a = arr[0]
        comb_b = arr[1]
        a = list(comb_a)
        b = list(comb_b)
        res = []
        for i in range(0, len(comb_a)):
            if comb_a[i] == comb_b[i]:
                res.append(comb_a[i])
            else:
                res = ''.join(res)
                return res
    if len(arr)>2:
        min=arr[0:(len(arr)//2)]
        max=[x for x in arr if x not in min]
        min=func(min)
        max=func(max)
    if len(arr)==1:
        return arr
    return
def helper(min):
    min=min[0]
    max=min[1]
    a=list(min)
    b=list(max)
    res=[]
    for i in range(0,len(min)):
            if min[i]==max[i]:
                res.append(min[i])
            else:
                res=''.join(res)
                return res
func(hehe)
