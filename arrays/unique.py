#check if string is unique
#logic - create an array of size 128 (number of entries in ascii table) initialized to false
#        for each character in string, compute the ascii value and check if that index in the array is true
#        if true, duplicates exist

#        Complexity O(n)
#   check if string length is > 128

import sys
mylist=[False]*128
string="eno mthidya"
if len(string) > 128:
    print('duplicates found')
    sys.exit()
ip=list(string)
print(ip)
for each in ip:
    if mylist[ord(each)]==True:
        print("string has duplicates")
        sys.exit()
    else:
        mylist[ord(each)] = True
print("string is unique")

#alternate
def char_checker(text):
    if len(text) == len(set(text)):
        print('all unique')
    else:
        print('duplicates found')

#if encoding is unicode, combinations are very high, so use hash values as keys to a dictionary
def unicode(text):
    mylist=list(text)
    dict={}
    for each in mylist:
        if hash(each) not in dict:
            dict[hash(each)]=True
        else:
            print('duplicates found')
            sys.exit()
    print('all unique')
