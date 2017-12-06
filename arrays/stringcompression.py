import sys

def countit():
    global pointer1
    global pointer2
    global count
    while (ip[pointer1]):
        if pointer2 < len(ip):
            if ip[pointer1] == ip[pointer2]:
                count += 1
                pointer2 += 1
            else:
                array.append(str(ip[pointer1]) + str(count))
                count = 1
                pointer1 = pointer2
                pointer2 = pointer1 + 1
        else:
            array.append(str(ip[pointer1]) + str(count))
            return
if __name__ == '__main__':

    iporig='aabcccccaaa'
    ip=sorted(iporig)
    pointer1=0
    pointer2=1
    array=[]
    count=1
    countit()
    if ''.join(array).replace('1','')==iporig:
        print(iporig)
    else:
        print(''.join(array))




