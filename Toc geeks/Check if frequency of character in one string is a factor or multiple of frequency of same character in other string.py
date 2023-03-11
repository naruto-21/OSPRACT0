# Python3 implementation of above approach
from collections import defaultdict

# Function that checks if the frequency of
# character are a factor or multiple of each other
def multipleOrFactor(s1, s2):

	# map store frequency of each character
	m1 = defaultdict(lambda:0)
	m2 = defaultdict(lambda:0)
	for i in range(0, len(s1)):
		m1[s1[i]] += 1

	for i in range(0, len(s2)):
		m2[s2[i]] += 1

	for it in m1:

		# if any frequency is 0, then continue
		# as condition is satisfied
		if it not in m2:
			continue

		# if factor or multiple, then condition satisfied
		if (m2[it] % m1[it] == 0 or
			m1[it] % m2[it] == 0):
			continue

		# if condition not satisfied
		else:
			return False
			
	return True

# Driver code
if __name__ == "__main__":

	s1 = "geeksforgeeks"
	s2 = "geeks"

	if multipleOrFactor(s1, s2): print("YES")
	else: print("NO")

# This code is contributed by Rituraj Jain
