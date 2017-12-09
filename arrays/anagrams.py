#https://leetcode.com/problems/group-anagrams/solution/

from copy import deepcopy

a=['cat','tac']
main_dict={'a':0,'b':0,'c':0,'d':0,'t':0}
reference={}
for each in a:
    dict=deepcopy(main_dict)
    for x in list(each):
        if x not in dict:
            dict[x]=1
        else:
            dict[x]+=1
    if tuple(dict.items()) not in reference:
        reference[tuple(dict.items())]=[each]
    else:
        reference[tuple(dict.items())].append(each)
print(reference)

