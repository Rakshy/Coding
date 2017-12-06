
def init(problem):
    global soln
    global buffer
    hello=[]
    for p in range(0,len(problem)):
        hello.append(p)
    while(len(hello)>1):
        for each in hello:
            if isinstance(each,list):
                x=each[0]
                y=each[1]
            else:
                x=each
                y=each
            if x - 1 >= 0 and y + 1 < len(problem) and problem[x - 1] == problem[y + 1]:
                index=hello.index(each)
                hello[index]=[x-1,y+1]
                # buffer.append([x - 1, y + 1])
            else:
                hello.remove(each)



a='banana'
problem=list(a)
soln=[]
buffer=[]
init(problem)
# longestpalindrome(problem)
