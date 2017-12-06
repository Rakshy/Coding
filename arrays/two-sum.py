array=[2,7,11,15]
target = 9
def twosum():
    for i in range(0,len(array)):
        difference=target-array[i]
        for j in range(i+1,len(array)):
            if difference==array[j]:
                return [i,j]
print(twosum())

def twosumhash():
    dict={}
    for every in array:
        dict[every]=True
    for each in list(dict):
        dict[each]=False
        difference=9-each
        try:
            if dict[difference]==True:
                print([each,difference])
                dict[each]=True
        except:
            dict[each]=True

twosumhash()