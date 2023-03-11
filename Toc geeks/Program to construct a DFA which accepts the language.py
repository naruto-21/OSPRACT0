Program to construct a DFA which accepts the language L = {aN | N ≥ 1}


# Python3 program for the above approach

# Function to check whether the string
# S satisfy the given DFA or not
def isAcceptedDFA(s, N):

	# Stores the count of characters
	count = 0

	# Iterate over the range [0, N]
	for i in range(N):

		# Count and check every
		# element for 'a'
		if (s[i] == 'a'):
			count += 1

	# If string matches with DFA
	if (count == N and count != 0):
		print ("Accepted")

	# If not matches
	else :
		print ("Not Accepted")

# Driver Code
if __name__ == '__main__':
	S = "aaaaa"

	# Function Call
	isAcceptedDFA(S, len(S))

# This code is contributed by mohit kumar 29







