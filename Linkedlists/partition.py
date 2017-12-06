from Linkedlists.single_LL import *
class partition(linkedlist):
    def partitionit(self,x):
        lowerlist=partition()
        higherlist=partition()
        this_node=self.root
        while(this_node):
            if this_node.get_data()<x:
                current_node=this_node
                this_node=this_node.get_next()
                current_node.set_next(None)
                lowerlist.add(current_node)
            else:
                current_node = this_node
                this_node = this_node.get_next()
                current_node.set_next(None)
                higherlist.add(current_node)
        this_node=lowerlist.get_root()
        while (this_node):
            if not this_node.get_next():
                this_node=this_node.get_next()
            else:
                break
        this_node.set_next(higherlist.get_root())
        return lowerlist

if __name__ == '__main__':
    ml=partition()
    ml.add(1)
    ml.add(2)
    ml.add(10)
    ml.add(5)
    ml.add(8)
    ml.add(5)
    ml.add(3)
    ml.printlist()
    newls=ml.partitionit(5)
    newls.printlist()