rtidict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
itrdict={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
lvl=[1000,900,500,400,100,90,50,40,10,9,5,4,1]


def romantoint(ip):
    ip=list(ip)
    total=0
    for x in range(0,len(ip)):
        try:
            if rtidict[ip[x]]>=rtidict[ip[x+1]]:
               total+=rtidict[ip[x]]
            else:
                total-=rtidict[ip[x]]
        except:
            total+=rtidict[ip[x]]
    print(s+'---->'+str(total))

def intotoroman():
    global number
    for i in range(0,len(lvl)-1):
        if i==0 and number>=1000:
            helper(1000)
        elif number<=lvl[i] and number>=lvl[i+1]:
            helper(lvl[i+1])

def helper(hehe):
    global number
    global rom
    quotient=abs(number//hehe)
    rom=rom+(itrdict[hehe]*quotient)
    remainder=number-(quotient*hehe)
    if remainder==4:
        pass
    number=remainder
    if number>0:
        intotoroman()
    else:
        print(str(originalnumber)+'--->'+rom)

#int to roman
number=3854
originalnumber=number
rom=''
intotoroman()

#roman to int
s='MMCCCXLV'
romantoint(s)

