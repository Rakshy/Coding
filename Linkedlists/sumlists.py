from Linkedlists.single_LL import *
class sumlists(linkedlist):
    def sum(self,head2):
        head1=self.get_root()
        head2=l2.get_root()
        carry=0
        final=[]
        while(head1 or head2):
            ans=0
            if not head1:
                ans=carry+head2.get_data()
                head2=head2.get_next()
            elif not head2:
                ans = carry + head1.get_data()
                head1 = head1.get_next()
            else:
                ans=carry + head1.get_data()+head2.get_data()
                head1 = head1.get_next()
                head2 = head2.get_next()
            if ans>9:
                ans=ans%10
                carry=1
            else:
                carry=0
            final.insert(0,ans)
        new=sumlists()
        for each in final:
            new.add(int(each))
        print('final list is')
        new.printlist()
    def sum_inverted(self,l2):
        final = []
        size1=l1.get_size()
        size2=l2.get_size()
        if size1>size2:
            while(size1>size2):
                l2.add(0)
                size2+=1
        elif size2>size1:
            while(size2>size1):
                l1.add(0)
                size1+=1
        arr=[]
        head1 = self.get_root()
        head2 = l2.get_root()
        carry=0
        index=0
        while(head1):
            ans=head1.get_data()+head2.get_data()
            if ans>=10:
                ans=ans%10
                carry=1
                arr.append(ans)
                if carry==1:
                    if index>0:
                        tmpindex=index-1
                        while(tmpindex>=0):
                            if arr[tmpindex]+1<10:
                                arr[tmpindex]+=1
                                break
                            else:
                                arr[tmpindex]=0
                                tmpindex=tmpindex-1
                    elif index==0:
                        arr.insert(0,1)
                        index+=1
                    carry=0
            else:
                arr.append(ans)
            index+=1
            head1 = head1.get_next()
            head2 = head2.get_next()
        new = sumlists()
        arr=reversed(arr)
        for each in arr:
            new.add(int(each))
        print('final list is')
        new.printlist()




if __name__ == '__main__':
    l1=sumlists()
    l2=sumlists()
    l1.add(9)
    l1.add(9)
    l1.add(9)
    l1.add(9)
    l1.add(9)
    l1.add(9)
    l2.add(9)
    l2.add(9)
    l2.add(9)
    l2.add(9)
    l2.add(9)
    l2.add(9)
    l1.printlist()
    l2.printlist()
    l1.sum_inverted(l2)











