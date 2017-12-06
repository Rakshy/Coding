from Linkedlists.single_LL import node,linkedlist
class removenth(linkedlist):
    def __init__(self):
        linkedlist.__init__(self)
        self.count=1
    def remove(self,n):
        this=self.get_root()
        prev=None
        while(this):
            if n==1:
                try:
                    self.set_root(this.get_next())
                    this.set_next(None)
                    return
                except:
                    self.set_root(None)
                    return
            if self.count<n:
                prev=this
                this=this.get_next()
                self.count+=1
            elif self.count==n:
                prev.set_next(this.get_next())
                this.set_next(None)
                self.printlist()
                return




ml=removenth()
ml.add(5)
ml.add(6)
ml.add(9)
ml.add(5)
ml.add(99)
ml.add(5)
ml.add(99)
ml.printlist()
ml.remove(3)
ml.remove(1)
ml.printlist()