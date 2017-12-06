from stack_queue.stack import *
import math
class three_stack():
    def __init__(self,s):
        self.init_size=s
        self.arr=[None]*s
        r=math.floor(s/3)
        self.s1_begin=0
        self.s1_current=0
        self.s1_end=r-1
        self.s1_size=0
        self.s2_begin=r
        self.s2_current = r
        self.s2_end=r+(r-1)
        self.s2_size=0
        self.s3_end=r+r
        self.s3_begin=(len(self.arr))-1
        self.s3_current = (len(self.arr)) - 1
        self.s3_size=0
        self.s1_flag=False
        self.s2_flag = False
        self.s3_flag = False
        print('s1_begin '+str(self.s1_begin))
        print('s1_end '+str(self.s1_end))
        print('s2_begin ' + str(self.s2_begin))
        print('s2_end ' + str(self.s2_end))
        print('s3_begin ' + str(self.s3_begin))
        print('s3_end ' + str(self.s3_end))

    def reallocate(self,allocation_for_s1,allocation_for_s2,allocation_for_s3):
        haha = [None] * self.init_size
        for i in range(self.s1_begin, self.s1_end + 1):
            if self.arr[i]!=None:
                haha[i] = self.arr[i]
                tmp_s1_current = i
            else:
                tmp_s1_current = i
                break

        i += allocation_for_s1
        tmp_s1_end = i
        i += 1
        tmp_s2_begin = i+1
        for j in range(self.s2_begin, self.s2_end + 1):
            if self.arr[j] != None:
                haha[i] = self.arr[j]
                tmp_s2_current = i
                i+=1

            else:

                break

        i+=allocation_for_s2
        tmp_s2_end = i
        # i += 1
        tmp_s3_end = i+1
        i+=allocation_for_s3
        for k in range(self.s3_begin,self.s3_end-1,-1):
            if self.arr[k] != None:
                haha[k] = self.arr[k]
                tmp_s3_current = k

            else:
                break

        self.arr = haha
        self.s1_end = tmp_s1_end
        self.s2_begin = tmp_s2_begin
        self.s2_end = tmp_s2_end
        self.s3_end = tmp_s3_end
        self.s1_current=tmp_s1_current
        self.s2_current=tmp_s2_current
        self.s3_current=tmp_s3_current
        # self.printstack()

    def freeup(self,calling_stack):
        total_free_space = (self.s2_begin-self.s1_current-1)+(self.s3_current+1-self.s2_current-1-1)
        if total_free_space==0:
            print('ERROR: No space in array')
            return False
        if total_free_space>=3:
            allocation_for_s1=math.ceil(total_free_space/3)
            allocation_for_s2=math.ceil((total_free_space-allocation_for_s1)/2)
            allocation_for_s3=total_free_space-allocation_for_s1-allocation_for_s2
            self.reallocate(allocation_for_s1, allocation_for_s2, allocation_for_s3)
        else:
            if calling_stack=='s1':
                allocation_for_s1=total_free_space
                allocation_for_s2=0
                allocation_for_s3=0
                self.reallocate(allocation_for_s1,allocation_for_s2,allocation_for_s3)
            if calling_stack=='s2':
                allocation_for_s1=0
                allocation_for_s2=total_free_space
                allocation_for_s3=0
                self.reallocate(allocation_for_s1, allocation_for_s2, allocation_for_s3)
            if calling_stack == 's3':
                allocation_for_s1 = 0
                allocation_for_s2 = 0
                allocation_for_s3 = total_free_space
                self.reallocate(allocation_for_s1, allocation_for_s2, allocation_for_s3)
        return True



    def add(self,stack,d):
        if stack==1:
            if self.s1_flag==False:
                self.arr[self.s1_current] = d
                self.s1_size += 1
                self.s1_flag=True


            else:
                if self.s1_current+1<=self.s1_end:
                    self.s1_current += 1
                    self.arr[self.s1_current]=d

                    self.s1_size+=1
                else:
                    print('reallocating')
                    if self.freeup('s1')==True:
                        self.add(1,d)
            return

        if stack==2:
            if self.s2_flag==False:
                self.arr[self.s2_current] = d
                self.s2_size += 1
                self.s2_flag=True

            else:
                if self.s2_current+1<=self.s2_end:
                    self.s2_current += 1
                    self.arr[self.s2_current] = d

                    self.s2_size += 1
                else:
                    print('reallocating')
                    if self.freeup('s2')==True:
                        self.add(2, d)
            return

        if stack == 3:
            if self.s3_flag==False:
                self.arr[self.s3_current] = d
                self.s3_size += 1
                self.s3_flag=True

            else:
                if self.s3_current-1 >= self.s3_end:
                    self.s3_current -= 1
                    self.arr[self.s3_current] = d

                    self.s1_size += 1
                else:
                    print('reallocating')
                    if self.freeup('s3')==True:
                        self.add(3, d)
            return

    def printstack(self):
        print(self.arr)

if __name__ == '__main__':
    # ss=input('enter size of stack\n')
    # n=three_stack(int(ss))
    # print('stack created')
    # while(True):
    #     try:
    #         a,b = input("Enter two numbers here: \n").split()
    #         n.add(int(a), int(b))
    #         n.printstack()
    #     except ValueError:
    #         print('try again')
    n=three_stack(10)
    n.add(1,1)
    n.printstack()
    n.add(2,2)
    n.printstack()
    n.add(3,3)
    n.printstack()
    n.add(2,2)
    n.printstack()
    n.add(2, 2)
    n.printstack()
    n.add(2, 2)
    n.printstack()
    n.add(2, 2)
    n.printstack()
    n.add(2, 2)
    n.printstack()
    n.add(2, 2)
    n.printstack()
    n.add(2, 2)
    n.printstack()
    n.add(2, 2)
    n.printstack()
    n.add(2, 2)
    n.printstack()