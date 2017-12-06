from Linkedlists.single_LL import *
class intersection(linkedlist):
    def find_intersection(self,l2):
        h1=self.get_root()
        h2=l2.get_root()
        size1=0
        size2=0
        last_h1=None
        last_h2=None
        while(h1):
            size1+=1
            last_h1=h1
            h1=h1.get_next()
        while (h2):
            size2 += 1
            last_h2 = h2
            h2 = h2.get_next()
        if last_h1==last_h2:
            print('intersection exists')
            if size1>size2:
                diff=size1-size2
                h1=self.get_root()
                h2=l2.get_root()
                while(diff>0):
                    h1=h1.get_next()
                    diff-=1
            if size2>size1:
                diff=size2-size1
                h1=self.get_root()
                h2=l2.get_root()
                while(diff>0):
                    h2=h2.get_next()
                    diff-=1
            while(h1 and h2):
                if h1!=h2:
                    h1=h1.get_next()
                    h2=h2.get_next()
                else:
                    print('the intersection is',end=' ')
                    print(h1.get_data())
                    break

if __name__ == '__main__':
    l1=intersection()
    l2=intersection()
    l3=intersection()
    l3.add(1)
    l3.add(2)
    l3.add(7)
    l1.add(9)
    l1.add(5)
    l1.add(1)
    l1.add(3)
    l2.add(6)
    l2.add(4)
    p1=l1.get_root()
    p2=l2.get_root()
    while(p1.get_next()):
        p1=p1.get_next()
    while (p2.get_next()):
        p2 = p2.get_next()
    p1.set_next(l3.get_root())
    p2.set_next(l3.get_root())
    l1.printlist()
    l2.printlist()
    l1.find_intersection(l2)
    