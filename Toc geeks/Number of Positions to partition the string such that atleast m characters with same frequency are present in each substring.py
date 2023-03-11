# Python3 implementation of the approach
from collections import defaultdict

# Function to return the number of ways
# to partition the given so that the
# given condition is satisfied
def countWays(string, m):

	# Hashset to store unique
	# characters in the given string
	Set = set()
	for i in range(0, len(string)):
		Set.add(string[i])

	# To store the number of ways
	# to partition the string
	result = 0

	for i in range(1, len(string)):

		# Hashmaps to store frequency of
		# characters of both the partitions
		first_map = defaultdict(lambda:0)
		second_map = defaultdict(lambda:0)

		# Iterate in the first partition
		for j in range(0, i):

			first_map[string[j]] += 1
		
		# Iterate in the second partition
		for k in range(i, len(string)):

			second_map[string[k]] += 1
		
		# To store the count of characters that have
		# equal frequencies in both the partitions
		total_count = 0

		for ch in Set:

			# first_count and second_count keeps track
			# of the frequencies of each character
			first_count, second_count = 0, 0

			# Frequency of the character
			# in the first partition
			if ch in first_map:
				first_count = first_map[ch]

			# Frequency of the character
			# in the second partition
			if ch in second_map:
				second_count = second_map[ch]

			# Check if frequency is same in both the partitions
			if first_count == second_count and first_count != 0:
				total_count += 1
		
		# Check if the condition is satisfied
		# for the current partition
		if total_count >= m:
			result += 1
	
	return result

# Driver code
if __name__ == "__main__":

	string = "aabbccaa"
	m = 2
	print(countWays(string, m))
	
# This code is contributed by Rituraj Jain
