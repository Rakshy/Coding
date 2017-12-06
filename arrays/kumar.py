array = [1,7,2,1,3,5]
for i in range(0,len(array)):
    if (i==0 and array[1]<array[0]):
        temp = array[0]
        array[0] = array[1]
        array[1] = temp
    elif (i != 0 and i % 2 == 0):
        if(array[i]>array[i-1]):
            temp = array[i]
            array[i] = array[i-1]
            array[i-1] = temp
        elif (i%2==1 and i!=(len(array)-1)):
            if(array[i]<array[i+1]):
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] =temp

print(array)
