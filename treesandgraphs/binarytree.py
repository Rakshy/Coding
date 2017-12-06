'''implement a binary tree'''
class node():
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None
    def get_data(self):
        return self.data
    def set_data(self,d):
        self.data=d
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    def set_left(self,n):
        self.left=n
    def set_right(self,n):
        self.right=n
class binarytree():
    def __init__(self):
        self.size=0
        self.root=None
    def get_root(self):
        return self.root
    def add(self,d):
        new=node(d)
        if self.size==0:
            self.root=new
            self.size+=1
        else:
            this=self.root
            while (this):
                if d>this.get_data():
                    if (this.get_right()):
                        this=this.get_right()
                    else:
                        this.set_right(new)
                        self.size+=1
                        return
                elif d<this.get_data():
                    if (this.get_left()):
                        this=this.get_left()
                    else:
                        this.set_left(new)
                        self.size+=1
                        return
                else:
                    print('duplicate value')
                    return

    '''for remove logic: http://www.algolist.net/Data_structures/Binary_search_tree/Removal'''
    def remove(self,d):
        prev=None
        this=self.root
        while(this):
            if d<this.get_data():
                if this.get_left():
                    prev=this
                    this=this.get_left()
                else:
                    print('not found')
                    return
            elif d>this.get_data():
                if this.get_right():
                    prev=this
                    this=this.get_right()
                else:
                    print('not found')
                    return
            elif d==this.get_data():
                # no children
                if not(this.get_left() and this.get_right()):
                    if prev.get_left()==this:
                        prev.set_left(None)
                        self.size-=1
                        del this
                        return
                    else:
                        prev.set_right(None)
                        self.size-=1
                        del this
                        return
                #both children
                elif this.get_left() and this.get_right():
                    current=this
                    while(this.get_left() and this.get_right()):
                        if this.get_left():
                            prev=this
                            this=this.get_left()
                        else:
                            prev=this
                            this.get_right()
                    current.set_data(this.get_data())
                    if prev.get_left()==this:
                        prev.set_left(None)
                        self.size-=1
                        del this
                        return
                    else:
                        prev.set_right(None)
                        self.size-=1
                        del this
                        return
                #if 1 child
                else:
                    if this.get_left():
                        if prev.get_left()==this:
                            prev.set_left(this.get_left())
                            self.size-=1
                            del this
                            return
                        else:
                            prev.set_right(this.get_right())
                            self.size -= 1
                            del this
                            return

def inorder(tree):
    this=tree.get_root()
    ino(this)
def ino(this):
    if this==None:
        return

    ino(this.left)

    print(this.data)
    ino(this.right)


if __name__ == '__main__':
    b=binarytree()
    b.add(1)
    b.add(0)
    b.add(3)
    b.add(2)
    b.add(5)
    b.add(7)
    inorder(b)
    b.remove(3)
    inorder(b)