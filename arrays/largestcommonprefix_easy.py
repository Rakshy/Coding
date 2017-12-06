def prefix():
    final = []
    for i in range(0, len(haha[0])):
        ref = haha[0][i]
        for each in haha:
            if ref == each[i]:
                pass
            else:
                final = ''.join(final)
                print(final)
                return
        final.append(ref)

def h():
    for each in hehe:
        global smallest
        if smallest in each:
            pass
        else:
            smallest=smallest[:-1]
            if smallest=='':
                print('No common prefixes')
                return
            h()
            return
    print(smallest)
    print('got it!')

# hehe=['leets','leetcode','leet','leeds','leemans','leetiole','leephone']
haha=[]
hehe=['hello','fu']
for each in hehe:
    haha.append(list(each))
# prefix()
smallest=min((word for word in hehe if word), key=len)
h()
