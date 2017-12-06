'''Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.'''
'''
Solutions:
1. Add another field to the node keeping track of the minimum at the time of insertion. when min function is called,
check the min field of the top most element
Disadvantage, a lot of space is wasted.
2. keep track of the mins in another stack'''

'''2nd solution implementation'''
from stack_queue.stack import *
class new_stack(stack):
    def __init__(self):
        self.arr=[]
        self.minarr=[]
        self.size=0
        self.minarr_size=0
    def push(self,d):
        if self.minarr_size==0:
            (self.minarr).append(d)
            self.minarr_size+=1
        else:
            for x in range(0,self.minarr_size):
                if self.minarr[x]==d:
                    self.minarr.insert(x,d)
                    break
                elif self.minarr[x]<d:
                    if len(self.minarr)==x+1:
                        self.minarr.append(d)
                        self.minarr_size+=1
                        break
                    else:
                        pass
                else:
                    (self.minarr).insert(x,d)
                    self.minarr_size+=1
        (self.arr).append(d)
        self.size+=1

    def pop(self):
        if self.size==0:
            print('stack is empty')
            return
        pp= self.arr[self.size-1]
        del self.arr[self.size-1]
        self.size-=1
        self.minarr.remove(pp)
        self.minarr_size-=1
        return pp

    def show_min(self):
        print(self.minarr[0])
    def print(self):
        print(self.arr)
        print(self.minarr)
        return

if __name__ == '__main__':
    main=new_stack()
    main.push(1)
    main.print()
    main.push(3)
    main.print()
    main.push(5)
    main.print()
    main.push(1)
    main.print()
    main.pop()
    main.print()
    main.pop()
    main.print()
