stack=[]
def A(s,i):
    print(" A",end="-> ")
    if i==len(s):
        print("Not Accepted")
        return
    stack.append(s[i])
    if s[i+1]=='$':
        B(s,i+1)
    else:
        A(s,i+1)
        
def B(s,i):
    print(" B",end="-> ")
    if i==len(s):
        print("Not Accepted")
        return
    l=len(stack)
    if stack[l-1]==s[i]:
        stack.pop()
    if s[i+1]=="z":
        C(s,i+1)   
    else:
        B(s,i+1)
        
def C(s,i):
    print(" C",end="-> ")
    if len(stack)==0:
        print("Accepted")
    else:
        print("not accepted")
        
s='abac$cabaz'
A(s,0)

