# Python3 program for the above approach

# Function to check whether the given
# is accepted by DFA or not
def checkValidDFA(s):
	
	# Stores initial state of DFA
	initial_state = 0

	# Stores final state of DFA
	final_state = 0

	# Stores previous state of DFA
	previous_state = 0

	# Iterate through the string
	for i in range(len(s)):
		
		# Checking for all combinations
		if ((s[i] == '0' and previous_state == 0) or
			(s[i] == '1' and previous_state == 3)):
			final_state = 1
		elif ((s[i] == '0' and previous_state == 3) or
			(s[i] == '1' and previous_state == 0)):
			final_state = 2
		elif ((s[i] == '0' and previous_state == 1) or
			(s[i] == '1' and previous_state == 2)):
			final_state = 0
		elif ((s[i] == '0' and previous_state == 2) or
			(s[i] == '1' and previous_state == 1)):
			final_state = 3

		# Update the previous_state
		previous_state = final_state

	# If final state is reached
	if (final_state == 3):
		print("Accepted")
		
	# Otherwise
	else:
		print("Not Accepted")

# Driver Code
if __name__ == '__main__':
	
	# Given string
	s = "010011"

	# Function Call
	checkValidDFA(s)

# This code is contributed by mohit kumar 29
