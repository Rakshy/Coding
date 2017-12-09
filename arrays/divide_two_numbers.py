dividend=27
divisor=3

#https://www.sigmainfy.com/blog/leetcode-divide-two-integers.html

# count=1
# if dividend >divisor:
#     count=1
#     while (dividend >= divisor):
#         if dividend == divisor:
#             break
#         else:
#             dividend -= divisor
#             count += 1
#     print(count)
#
# else:
#     print(count)
#
# print(bin(27))
# print(bin(27<<2))

# a=[1,2,3,4,5]
# a[0],a[2]=a[2],a[0]
# print(a)

def power(x,y):
    if( y == 0):
        return 1
    temp = power(x, y//2)
    if (y%2 == 0):
        return temp*temp
    else:
        return x*temp*temp

print(power(2,10))