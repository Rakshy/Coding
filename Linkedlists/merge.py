#https://leetcode.com/problems/merge-two-sorted-lists/solution/
from Linkedlists.single_LL import node,linkedlist


def merge(l1, l2,l3):
    pointer1 = l1.get_root()
    pointer2 = l2.get_root()
    if pointer1.get_data() >= pointer2.get_data():
        l3.set_root(pointer1)
        temp = pointer1.get_next()
        pointer1.set_next(pointer2)
        pointer1 = temp
    else:
        l3.set_root(pointer2)
        temp = pointer2.get_next()
        pointer2.set_next(pointer1)
        pointer2 = temp
    l3_current=l3.get_root()
    while (pointer1 and pointer2):
        # print(pointer1.get_data())
        # print(pointer2.get_data())
        if pointer1.get_data() <= pointer2.get_data():
            l3_current.set_next(pointer1)
            l3_current=l3_current.get_next()
            pointer1=pointer1.get_next()
            # l3.printlist()
        else:
            l3_current.set_next(pointer2)
            l3_current = l3_current.get_next()
            pointer2=pointer2.get_next()
            # l3.printlist()
    if pointer1:
        l3_current.set_next(pointer1)
        # l3.printlist()
        return
    else:
        l3_current.set_next(pointer2)
        # l3.printlist()
        return


l1=linkedlist()
l2=linkedlist()
l3=linkedlist()
l1.add(5)
l1.add(4)
l1.add(1)
l2.add(8)
l2.add(7)
l2.add(6)
l2.add(3)
l2.add(2)
l2.add(1)
l1.printlist()
l2.printlist()
merge(l1,l2,l3)
l3.printlist()



