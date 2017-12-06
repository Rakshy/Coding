from Linkedlists.single_LL import *
class loop_detection(linkedlist):
    def find_loop(self):
        slow=(self.get_root()).get_next()
        fast=((self.get_root()).get_next()).get_next()
        while(slow.get_next() and fast.get_next() and (fast.get_next()).get_next()):
            if(slow!=fast):
                slow=slow.get_next()
                fast = (fast.get_next()).get_next()
            else:
                print('loop detected')
                slow=self.get_root()
                while(slow!=fast):
                    slow=slow.get_next()
                    fast=fast.get_next()
                print('head of the loop is ',end='')
                print(slow.get_data())
                return 
        print('loop does not exist')
        return 
if __name__ == '__main__':
    l2=loop_detection()
    l2.add(11)
    l2.add(10)
    l2.add(9)
    l2.add(8)
    l2.add(7)
    l2.add(6)
    l2.add(5)
    l2.add(4)
    l2.add(3)
    l2.add(2)
    l2.add(1)
    jj=l2.get_root()
    while(jj):
        last=jj
        if jj.get_data()==4:
            link=jj
            jj=jj.get_next()
        else:
            jj=jj.get_next()
    last.set_next(link)
    l2.find_loop()
                    
        
        