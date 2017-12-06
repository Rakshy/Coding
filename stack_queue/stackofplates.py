'''Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds
some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should
be composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push () and SetOfStacks. pop() should behave identically to a single stack
(that is, pop ( ) should return the same values as it would if there were just a single stack).

FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific sub- stack.'''

'''Logic : create a new field called limit and when push is called check if size>limit. if yes, create
a new substack and push. Also, create a substack flag to check if there is a substack or not.
 when popping, 1st check if the substack is true, if yes, then send the pop command to the substack
 after popping, check if size of substack is 0. if yes, delete the substack and set the substack flag to False'''

from stack_queue.stack import *

class new_stack(stack):
    def __init__(self):
        self.arr = []
        self.size = 0
        self.substack=False
        self.limit=1
    def push(self,d):
        if self.size>self.limit:
            if self.substack==True:
                self.nstack.push(d)
                return
            else:
                self.nstack=new_stack()
                self.substack=True
                self.nstack.push(d)
            return
        else:
            (self.arr).append(d)
            self.size+=1

    def get_size(self):
        return self.size

    def pop(self):
        if self.substack==True:
            (self.nstack).pop()
            if self.nstack.get_size()==0:
                del self.nstack
                self.substack = False
        else:
            if self.size==0:
                print('stack is empty')
                return
            pp= self.arr[self.size-1]
            del self.arr[self.size-1]
            self.size -= 1
            return pp

    def print(self):
        print(self.arr)
        if self.substack==True:
            print('------->')
            self.nstack.print()
if __name__ == '__main__':
    main=new_stack()
    main.push(1)
    main.print()
    main.push(2)
    main.print()
    main.push(3)
    main.print()
    main.push(4)
    main.print()
    main.push(5)
    main.print()
    main.pop()
    main.print()
    main.pop()
    main.print()
    main.pop()
    main.print()