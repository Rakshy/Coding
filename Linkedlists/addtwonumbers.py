from Linkedlists.single_LL import *
l=234
o=list(l)
def haha(ml,ll):
    val1 = ''
    val2 = ''
    mlnode=ml.get_root()
    llnode=ll.get_root()
    while(mlnode):
        val1=val1 + (str(mlnode.get_data()))
        mlnode=mlnode.get_next()
    while(llnode):
        val2 = val2 + str(llnode.get_data())
        llnode = llnode.get_next()
    val1 = val1[::-1]
    val2 = val2[::-1]
    sum=int(val1)+int(val2)
    sumlist=[int(d) for d in str(sum)]
    sumlist=sumlist[::-1]
    return sumlist

if __name__ == '__main__':
    ml=linkedlist()
    ml.add(3)
    ml.add(4)
    ml.add(2)

    ll = linkedlist()
    ll.add(4)
    ll.add(6)
    ll.add(5)

    ml.printlist()
    ll.printlist()
    haha(ml,ll)