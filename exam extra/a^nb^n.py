count = []

def A(s,i):
    print("A-->",end="")
    if i == len(s):
        B(count)
    if s[i] == "a":
        count.append("a")
        A(s,i+1)
    elif s[i] == "b":
        try:
            count.pop()
        except IndexError as e:
            print("\nAn Error occured while poping.\nThere must be less 'a' than 'b'.")
            return
        A(s,i+1)
    elif s[i] == "z":
        B(count)
def B(count):
    if len(count) == 0:
        print("Accepted")
    else:
        print("Not Accepted")

#main 
s = input("Enter the string: ")
A(s,0)