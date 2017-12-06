from Linkedlists.single_LL import *
class kth(linkedlist):
    def find_kth(self,k):
        p1=self.root
        p2=self.root
        #move p1 to kth place
        while(k!=0):
            p1=p1.get_next()
            k-=1
        while(p1.get_next()):
            p1=p1.get_next()
            p2=p2.get_next()
        print('the kth element is '+str(p2.get_data()))

ml=kth()
ml.add(5)
ml.add(6)
ml.add(9)
ml.add(5)
ml.add(99)
ml.add(5)
ml.add(99)
ml.printlist()
ml.find_kth(3)

