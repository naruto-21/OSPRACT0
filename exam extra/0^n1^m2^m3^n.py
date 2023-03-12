count = []
def A(s,i):
    if i == len(s) or s[i] == "z":
        C(count)
    if s[i] == "0" or s[i] == "1":
        count.append(s[i])
        A(s,i+1)
    else:
        B(s,i+1)

def B(s,i):
    if i == len(s) or s[i] == "z":
        C(count)
    count.pop()
    if s[i] == "2" or s[i] =="3":
        B(s,i+1)

def C(count):
    if len(count)-1 == 0:
        print("Accepted")
    else:
        print("Not accepted")

#main
s = "011223z"
A(s,0)