
def longestpalindrome(problem):
    global soln
    global buffer
    explore = True
    x=0
    y=0
    if len(soln)==0:
        while(x<len(problem)-1):
                if x-1>=0 and problem[x-1]==problem[x+1]:
                    soln.append([x-1,x+1])
                    x+=1
                else:
                    x+=1
    else:
        while(explore==True):
            for each in soln:
                x=each[0]
                y=each[1]
                if x - 1 >= 0 and y+1<len(problem) and problem[x - 1] == problem[y + 1]:
                    buffer.append([x - 1, y + 1])
                if len(soln)==1:
                    explore=False
                    print(''.join(problem[x:y+1]))
                    return
            soln=buffer
            buffer=[]


a='banana'
problem=list(a)
soln=[]
buffer=[]
longestpalindrome(problem)
longestpalindrome(problem)
