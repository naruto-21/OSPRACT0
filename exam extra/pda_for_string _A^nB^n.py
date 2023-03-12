stack=[]
def q0(s,i=0):
    print("=>Qo ",end='')
    if i==len(s):
        print(f"{s} is not in AnBn|n>0 form")
        return
    if s[i]=='a':
        stack.append('a')
    if s[i+1]=='$':
        q1(s,i+1)
    else:
        q0(s,i+1)
def q1(s,i):
    print("=>Q1 ",end='')
    if s[i]=='b':
        try:
            stack.pop()
        except IndexError as e:
            print("\nAn Error occured while poping.\nThere must be less 'a' than 'b'.")
            return
    if s[i+1]=='#':
        q2(s)
    else:
        q1(s,i+1)
def q2(s):
    print("=>Q2 ",end='')
    if len(stack)==0:
        print(f"\n{s} is in AnBn|n>0 form")
    else:
        print(f"\n{s} is not in AnBn|n>0 form")
#main program
#word='aa$bbb#'
word='aaa$bb#'
#word='aaaaaaaaaa$bbbbbbbbbb#'
print(f"Transition states of string [{word}] for a PDA[L=AnBn|n>0] are:")
q0(word)
