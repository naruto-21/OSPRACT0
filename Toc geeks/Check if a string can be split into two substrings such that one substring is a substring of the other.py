# Python3 program to implement
# the above approach

# Function to check if a can be
# divided into two substrings such that
# one subis subof the other
def splitString(S, N):
	
	# Store the last character of S
	c = S[N - 1]

	f = 0

	# Traverse the characters at indices [0, N-2]
	for i in range(N - 1):
		
		# Check if the current character is
		# equal to the last character
		if (S[i] == c):
			
			# If true, set f = 1
			f = 1
			
			# Break out of the loop
			break

	if (f):
		print("Yes")
	else:
		print("No")

# Driver Code
if __name__ == '__main__':
	
	# Given string, S
	S = "abcdab"

	# Store the size of S
	N = len(S)

	# Function Call
	splitString(S, N)
	
# This code is contributed by mohit kumar 29
