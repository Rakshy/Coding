from Linkedlists.single_LL import node,linkedlist

class ll(linkedlist):
    def rdups(self):
        this_node=self.root
        prev_node=None
        dict={}
        while this_node:
            if this_node.get_data() not in dict:
                dict[this_node.get_data()]=0
                prev_node=this_node
                this_node=this_node.get_next()
            else:
                prev_node.set_next(this_node.get_next())
                this_node=this_node.get_next()



ml=ll()
ml.add(5)
ml.add(6)
ml.add(9)
ml.add(5)
ml.add(99)
ml.add(5)
ml.add(99)
ml.printlist()
ml.rdups()
ml.printlist()
ml.find(66)
