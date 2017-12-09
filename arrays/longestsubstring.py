#https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/

class Solution():
    # global array
    # global longest
    # global long_length
    # global total
    longest=0
    long_length=0
    total=[]
    def __init__(self,arr):
        self.array=arr
        self.longest=0
        self.long_length=0
        self.total=[]
        self.visited=[]
        self.start=0
        self.end=0

    def loadmarkers(self,x):
        self.start=x
        try:
            while(self.array[self.start]==self.array[self.start+1]):
                self.start+=1
        except:
            return False
        self.end=self.start+1
        self.visited.append(self.array[self.start])
        self.visited.append(self.array[self.end])
        return True

    def findlongest(self):
        while(self.end<len(self.array)-1):
            self.end+=1
            if self.array[self.end] in self.visited:
                if self.end-self.start>self.long_length:
                    self.long_length=self.end-self.start
                    substring = self.array[self.start:self.start + self.long_length]
                    self.total=substring

                    if self.loadmarkers(self.end)==False:
                        print(len(self.total))
                        return
                else:
                    if self.loadmarkers(self.end)==False:
                        print(self.total)
                        return
            else:
                self.visited.append(self.array[self.end])



inp='abcabcbb'
arr=list(inp)
a=Solution(arr)
a.loadmarkers(0)
a.findlongest()


