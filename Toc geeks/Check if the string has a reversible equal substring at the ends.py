# python program for the above approach

# Function to print longest substring
# that appears at beginning of string
# and also at end in reverse order
def commonSubstring(s):

	n = len(s)
	i = 0
	j = n - 1

	# Stores the resultant string
	ans = ""
	while (j >= 0):

		# // If the characters are same
		if (s[i] == s[j]):
			ans += s[i]
			i = i + 1
			j = j - 1

		# Otherwise, break
		else:
			break

	# If the string can't be formed
	if (len(ans) == 0):
		print("False")

	# Otherwise print resultant string
	else:
		print("True")
		print(ans)

# Driver Code
if __name__ == "__main__":

	S = "abca"
	commonSubstring(S)
	
	# This code is contributed by rakeshsahni
