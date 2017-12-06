# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.
# Example
# pale, ple -) true
# pales, pale - ) true
# pale, bale -) true
# pale, bae -) false
def count():
    for each in ip1:
        if each in dict:
            dict[each]+=1
        else:
            dict[each]=1
    for every in ip2:
        if every in dict:
            dict[every]-=1
        else:
            dict[every]=1
def check(ttt):
    stop_flag = 0
    for hehe in dict:
        if stop_flag > ttt:
            print("beyond 1 edit")
            sys.exit()
        else:
            if dict[hehe] != 0:
                stop_flag += abs(dict[hehe])
    if stop_flag > ttt:
        print("beyond 1 edit")
        sys.exit()
    else:
        print('1 or less than 1 edit away')

def ins():
    count()
    check(1)
def replace():
    count()
    check(2)



if __name__ == '__main__':

    ip1='pale'
    ip2='bae'
    ip1=list(ip1)
    ip2=list(ip2)
    dict={}
    import sys
    if len(ip1)+1==len(ip2) or len(ip1) -1 == len(ip2):
        ins()
    elif len(ip1)==len(ip2):
        replace()
    else:
        print("beyond 1 edit")



