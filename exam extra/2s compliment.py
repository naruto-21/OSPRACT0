list = []
str= ""
def A(s, i):
    if i == 0:
        return
    if s[i - 1] == "0":
        list.insert(0,0)
        A(s, i - 1)
    else:
        list.insert(0,1)
        B(s, i - 1)

def B(s, i):
    if i == 0:
        return
    if s[i - 1] == "0":
        list.insert(0,1)
        B(s, i - 1)
    else:
        list.insert(0,0)
        B(s, i - 1)

s = "0100100"
A(s, len(s))
print(list)
for x in list:
    print(x,end="")
