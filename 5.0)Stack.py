#Our stack
class Stack():
    def __init__(self, arr=[]):
        self.mainArr= arr
        self.size = len(arr)

    def push(self, element):
        self.mainArr.append(element)
        self.size +=1

    def pop(self, ret=False):
        if(self.size==0):
            print("Underflow")
            return False
        element=self.mainArr[-1]
        del self.mainArr[-1]
        self.size-=1
        if(ret==True):
            return element

    def topElement(self):
        if(self.size==0):
            return False
        return self.mainArr[-1]

#Function to check if a string has balanced paranthesis
def isBalParenthesis(string):
    s = Stack()
    opening = ["(","{","["]
    closing = [")","}","]"]
    for i in range(len(string)):
        if(string[i] in opening):
            s.push(string[i])
        else:
            if(s.topElement()==False):
                return False
            index1 = opening.index(s.topElement())
            index2 = closing.index(string[i])
            if(index1==index2):
                s.pop()
            else:
                return False
    if(s.size==0):
        return True
    else:
        return False

#Stock span problem
#We maintain a stack that only stores greater elements and pops all smaller elements.
#This funtion is not called in the driver code 
def StockSpanProblem(arr):
    s = Stack()
    spanArr=[1]
    s.push(0)
    for i in range(1,len(arr)):
        while(s.size!=0 and arr[s.topElement()]<=arr[i]):
            s.pop()
        if(s.size==0):
            spanArr.append(i+1)
        else:
            spanArr.append(i-s.topElement())
        s.push(i)
    return spanArr

#A variation of stock span problem.
#It return span between next as well as previous element(where the element is minimum in the span)
#This function is not called in driver code.
def spanDict(arr):
    n=len(arr)
    stack=[]
    Ans = defaultdict()
    for i in range(n):
        while stack and arr[stack[-1]]>=arr[i]:
            key=stack.pop()
            Ans[arr[key]] = i-stack[-1]-1 if stack else i
        stack.append(i)
    while stack:
        key=stack.pop()
        Ans[arr[key]] = n-stack[-1]-1 if stack else n
    return Ans

#The function takes in three stacks and returns the sum that occurs in all these stacks.
#The problem goes like this: Given three stacks(initially as arrays), we are allowed to pop any numer of elements from any stack that, in the end
#we get the sum of all elements of each stack to be equal, we have to do so in order to maximize this sum.
#The function is not called in driver code.
def equalStacks(h1, h2, h3):
    #If any of them is empty return 0.
    if(h1==[] or h2==[] or h3==[]):
        return 0
    #Reverse so that list behaves as a stack.
    h1 = list(reversed(h1))
    h2 = list(reversed(h2))
    h3 = list(reversed(h3))
    #Make prefix arrays
    prefixArr1=set()
    prefixArr2=set()
    prefixArr3=set()
    psum=0
    for i in range(0,len(h1)):
        psum+=h1[i]
        prefixArr1.add(psum)
    psum=0
    for i in range(0,len(h2)):
        psum+=h2[i]
        prefixArr2.add(psum)
    psum=0
    for i in range(0,len(h3)):
        psum+=h3[i]
        prefixArr3.add(psum)
    
    #Their intersection represents total number of common sums, we choose maximum of them.
    ans =(prefixArr1.intersection(prefixArr2)).intersection(prefixArr3)
    if(len(ans)==0):
        return 0
    return max(ans)
    
#Stack Game function(explained tin the docs of stack).
#This is a Dynamic programming approach where x replaces the general memoization and we don't pop from A or B as well.
#The function is not called in driver code.
def StackGame(a, b, x):
    i = 0
    while i < len(a) and x >= a[i]:
        x -= a[i]
        i += 1
    
    ans = i
    j = 0
    for p in b:
        if(i==0 and x<0):
            break
        
        j += 1
        x -= p
        
        while x < 0 and i > 0:
            i -= 1
            x += a[i]
        
        if x >= 0:
            ans = max(ans, j + i)

    return(ans)
    
#Driver Code
string = input()
print("The given string has balanced paranthesis: ",isBalParenthesis(string))
