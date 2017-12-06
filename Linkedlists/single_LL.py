class node(object):
    def __init__(self,d,n=None):
        self.data=d
        self.next=n
    def get_next(self):
        return self.next
    def set_next(self,n):
        self.next=n
    def get_data(self):
        return self.data
    def set_data(self,d):
        self.data=d

class linkedlist():
    def __init__(self):
        self.root=None
        self.size=0
    def set_root(self,d):
        self.root=d
    def get_root(self):
        return self.root
    def get_size(self):
        return self.size
    def add(self,d):
        new_node=node(d,self.root)
        self.root=new_node
        self.size+=1
    def remove(self,d):
        this_node=self.root
        prev_node=None
        while this_node:
            if this_node.get_data()==d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size-=1
                return True #data removed
            else:
                prev_node=this_node
                this_node=this_node.get_next()
        return False
    def find(self,d):
        this_node=self.root
        while this_node:
            if this_node.get_data()==d:
                print('True')
                return
            else:
                this_node=this_node.get_next()
        print('false')
        return
    def printlist(self):
        this_node=self.root
        while this_node:
            print(str(this_node.get_data())+'->',end='')
            this_node=this_node.get_next()
        print('None')

# if __name__ == '__main__':
#     ml=linkedlist()
#     ml.add(4)
#     ml.add(5)
#     ml.add(8)
#     ml.find(5)
#     ml.printlist()
#     ml.remove(5)
#     ml.printlist()