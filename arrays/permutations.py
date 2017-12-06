# check if two strings are permutations of each other
import sys
text_1='ball'
text_2='lalb'
#check if length is equal
if len(text_1)!=len(text_2):
    print('no permutations exist')
    sys.exit()
#method 1 - sort and compare
text_1=sorted(list(text_1))
text_2=sorted(list(text_2))
if text_1==text_2:
    print("strings are permutations")
else:
    print('no permutations exist')
# time complexity n log n - beacuse the sorted function takes n log n 