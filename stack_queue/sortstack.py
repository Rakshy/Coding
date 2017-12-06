'''Sort Stack: Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy the elements into any other
data structure (such as an array).The stack supports the following operations: push, pop, peek, and isEmpty.'''

'''
Logic : use recursion for this. 1st pop all the elements to temp variables till end is reached.
if size=0(i.e empty) or if the top most >= the current (which means current is in the correct order i.e descending),
push the temp onto the stack.
if not, pop to top most till a match is found and then reinsert the tmps on top of it.'''
from stack_queue.stack import *

class sort_stack(stack):
    def sort(self):
        if (self.size!=0):
            tmp = self.pop()
            self.sort()
            self.sortedinsert(tmp)

    def sortedinsert(self,d):
        if self.size==0 or self.peek()>=d:
            self.push(d)
        else:
            tmp=self.pop()
            self.sortedinsert(d)
            self.push(tmp)
            return

if __name__ == '__main__':
    hehe=sort_stack()
    hehe.push(2)
    hehe.push(5)
    hehe.push(7)
    hehe.push(44)
    hehe.push(23)
    hehe.push(77)
    hehe.push(12)
    hehe.push(25)
    hehe.push(65)
    hehe.push(55)
    hehe.print()
    hehe.sort()
    hehe.print()