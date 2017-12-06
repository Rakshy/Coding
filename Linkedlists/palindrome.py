#logic - use fast/slow runner
#initialize 2 pointers at the head, move one at 1 place per move and the other 2 places per move.
# when the 2nd pointer reaches the end, the 1st will be pointing at the center of the list.
#store values of head 1 in an array and then compare head 2 with the array as it moves

from Linkedlists.single_LL import *
class palindrome(linkedlist):
    def is_palindrome(self):
        if l2.get_size()%2==0:
            print('list is not a palindrome')
        else:
            head1=head2=self.get_root()
            arr=[]
            while(head2.get_next()):
                arr.insert(0, head1.get_data())
                head1=head1.get_next()
                head2=head2.get_next()
                head2 = head2.get_next()
            #setting the head to start comparing
            head2=head1.get_next()
            for each in arr:
                if head2.get_data()==each:
                    head2=head2.get_next()
                else:
                    print('list is not a palindrome')
                    return
            print('list is a palindrome')
if __name__ == '__main__':
    l2=palindrome()
    l2.add(1)
    l2.add(2)
    l2.add(3)
    l2.add(4)
    l2.add(3)
    l2.add(2)
    l2.add(1)
    l2.printlist()
    l2.is_palindrome()