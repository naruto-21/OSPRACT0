# Python3 program for the above approach
digits,sign = "0123456789", "+-"
dot, ex = ".", "eE"
dfa = [[0 for i in range(5)] for i in range(11)]

# Function to construct DFA as per the
# given conditions
def makeDFA():
	global dfa

	# If at state 0 and a digit has
	# occurred then set it to state 1
	dfa[0][0] = 1

	# Similarly for all other states
	dfa[1][0] = 1
	dfa[1][2] = 3
	dfa[1][3] = 2
	dfa[1][4] = 6

	dfa[3][0] = 4

	dfa[4][0] = 4
	dfa[4][3] = 5
	dfa[4][4] = 6

	dfa[6][0] = 8
	dfa[6][1] = 7

	dfa[7][0] = 8

	dfa[8][0] = 8
	dfa[8][3] = 9


# Function to build and connect
# the DFA states
def buildDFA():
	global dfa
	# Connect all the states to the
	# dead state
	for i in range(11):
		for j in range(5):
			dfa[i][j] = 10

	# Function call to make DFA as
	# per the given conditions
	makeDFA()

# Function call to check whether an
# integer in the form of is
# unsigned integer or not
def checkDFA(s):
	# Build the DFA
	buildDFA()

	# Stores the current state
	currentstate = 0

	# Traverse the string
	for i in range(len(s)):

		if (s[i] in digits):

			# If at a certain state a
			# digit occurs then change
			# the current state according
			# to the DFA
			currentstate = dfa[currentstate][0]

		# Or +/- sign
		elif (s[i] in sign):
			currentstate = dfa[currentstate][1]

		# Or decimal occurred
		elif (s[i] in dot):
			currentstate = dfa[currentstate][2]

		# Or any other character
		elif (s[i] in ex):
			currentstate = dfa[currentstate][4]

		# Or e/E or exponent sign
		else:
			currentstate = dfa[currentstate][3]

	# State 1, 4, 8 will give
	# the final answer
	if (currentstate == 1 or currentstate == 4 or currentstate == 8):
		print("Unsigned integer")
	else:
		print("Not an unsigned integer")

# Driver Code
if __name__ == '__main__':
	S = "1729"
	checkDFA(S)

	# This code is contributed by mohit kumar 29.
