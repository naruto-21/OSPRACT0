def q0(s,i):
    print("q0->",end=" ")
    if i==len(s):
        print("YES")
        return
    if s[i]=="R":
        q0(s,i+1)
    elif s[i]=="A":
        q1(s,i+1)
    else :
        q2(s,i+1)
def q1(s,i):
    print("q1->",end=" ")
    if i==len(s):
        print("NO")
        return
    if s[i]=="R":
        q2(s,i+1)
    elif s[i]=="A":
        q1(s,i+1)
    else:
        q3(s,i+1)
def q2(s,i):
    print("q2->",end=" ")
    if i==len(s):
        print("NO")
        return
    if s[i]=="R":
        q3(s,i+1)
    elif s[i]=="A":
        q3(s,i+1)
    else:
        q2(s,i+1)
def q3(s,i):
    print("q3->",end=" ")
    if i==len(s):
        print("NO")
        return
    if s[i]=="R" or s[i]=="A" or s[i]=="G":
        q3(s,i+1)
        
#main
s="RAAGG"
q0(s,0)
