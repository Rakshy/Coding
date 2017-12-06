# Write a method to replace all spaces in a string with '%20: You may assume that the string has ' \
#   'sufficient space at the end to hold the additional characters, and that you are given the ' \
#   '"true" length of the string. (Note: If implementing in Java, please use a character array so ' \
#   'that you can perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith  " , 13
# Output: "Mr%20John%20Smith"

text='Mr John Smith  '
length=13
mylist=list(text)
import sys
for each in mylist:
    if length==0:
        print(''.join(mylist))
        sys.exit()
    if each==' ' and length!=0:
        mylist[mylist.index(each)]='%20'
    length-=1
