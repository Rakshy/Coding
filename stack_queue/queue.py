class queue():
    def __init__(self):
        self.arr=[]
        self.size=0
    def push(self,d):
        (self.arr).insert(0,d)
        self.size+=1
    def pop(self):
        if self.size==0:
            print('queue is empty')
            return
        pp= self.arr[self.size-1]
        del self.arr[self.size-1]
        self.size-=1
        return pp
    def peek(self):
        if self.size==0:
            print('queue is empty')
            return
        return self.arr[self.size-1]
    def is_empty(self):
        if self.size>0:
            print('False')
            return False
        else:
            print('True')
            return True

if __name__ == '__main__':
    new=queue()
    new.peek()
    new.is_empty()
    new.push(5)
    new.push(9)
    new.is_empty()
    new.push(7)
    print(new.peek())
    new.pop()
    print(new.peek())



