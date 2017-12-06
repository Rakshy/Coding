
#http://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/

par='[()]{}{[()()]()}'
dict={'(':')','[':']','{':'}'}
a=list(par)
stack=[]

def heeh(a):
    for each in a:
        if each in dict:
            stack.append(each)
        else:
            if len(stack)==0:
                print('Not valid')
                return False
            else:
                hehe=stack.pop()
                if dict[hehe]==each:
                    pass
                else:
                    print('Not valid')
                    return False
    print('Valid')
heeh(a)
