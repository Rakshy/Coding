# Given a string, write a function to check if it is a permutation of a palindrome.

#Logic : to be a permutation, an even string should have - even number of all characters
#                                Odd string should have - 1 single character and even other characters
# check if white space is also considered as a character
# Time complexity O(2N) = O(N)
ip='tact coa'
import sys
my_list=list(ip)
dict={}
for each in my_list:
    if each!=' ':
        if each in dict:
            dict[each]+=1
            dict[each]=dict[each]%2
        else:
            dict[each]=1
stop_flag=False
for every in dict:
    if dict[every]==1:
        if stop_flag==False:
            stop_flag=True
        else:
            print('Not a permutation of a palindrome')
            sys.exit()
print('It is a permutation')



