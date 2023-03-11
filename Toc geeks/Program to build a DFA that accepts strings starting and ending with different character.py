# Python3 Program to DFA that accepts
# if it starts and end with
# same character


# vector to store state transition
state_transition = []

# end position is checked using string
# length value.
# q0 is the starting state.
# q2 and q4 are intermediate states.
# q1 and q3 are final states.
def q1(s, i):

	state_transition.append("q1")
	if (i == len(s)):
		return False

	# state transitions
	# a takes to q1, b takes to q2
	if (s[i] == 'a'):
		return q1(s, i + 1)
	else:
		return q2(s, i + 1)

def q2(s, i):

	state_transition.append("q2")
	if (i == len(s)):
		return True

	# state transitions
	# a takes to q1, b takes to q2
	if (s[i] == 'a'):
		return q1(s, i + 1)
	else:
		return q2(s, i + 1)

def q3(s, i):

	state_transition.append("q3")
	if (i == len(s)):
		return False

	# state transitions
	# a takes to q4, 1 takes to q3
	if (s[i] == 'a'):
		return q4(s, i + 1)
	else:
		return q3(s, i + 1)

def q4(s, i):

	state_transition.append("q4")
	if (i == len(s)):
		return True

	# state transitions
	# a takes to q4, b takes to q3
	if (s[i] == 'a'):
		return q4(s, i + 1)
	else:
		return q3(s, i + 1)

def q0(s, i):

	state_transition.append("q0")
	if (i == len(s)):
		return False

	# state transitions
	# a takes to q1, b takes to q3
	if (s[i] == 'a'):
		return q1(s, i + 1)
	else:
		return q3(s, i + 1)

s = "ababab"

# all state transitions are printed.
# if is acceptable, print YES.
# else NO is printed
ans = q0(s, 0)
if (ans):
	print("YES")

	# print transition state of given
	# str
	for it in state_transition:
		print(it, end = " ")

else:
	print("NO")

# This code is contributed by mohit kumar 29
