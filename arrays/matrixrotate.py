# Rotate Matrix: Given an image represented by an NxN matrix,
# where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees.
# Logic - https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python

ip=[[1,2,3],[4,5,6],[7,8,9]]
for each in ip:
    print(each)
# clock=zip(*reversed(ip))
# array=[]
# array2=[]
# anticlock=reversed(list(zip(*ip)))
# for each in clock:
#     array.append(list(each))
# print(array)
# for each in anticlock:
#     array2.append(list(each))
# print(array2)
print('-----------')


for value in zip(*ip[::-1]):
    print(value)