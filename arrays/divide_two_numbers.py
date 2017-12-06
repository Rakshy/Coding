dividend=27
divisor=3
count=1
if dividend >divisor:
    count=1
    while (dividend >= divisor):
        if dividend == divisor:
            break
        else:
            dividend -= divisor
            count += 1
    print(count)

else:
    print(count)

print(bin(27))
print(bin(27<<2))