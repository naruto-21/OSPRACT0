<script>

# python3 implementation of the above approach

# Function to find min operations
def minOperations(A, B) :

	# dp[i][j] = length of longest
	# (contiguous) suffix of A[0..i]
	# that is a subsequence of B[0..j]
	dp = [[ 0 for _ in range(1001)] for _ in range(1001) ]

	# r = maximum value over all
	# dp[i][j] computed so far
	r = 0

	for i in range(0, len(A) + 1) :
		for j in range(0, len(B) + 1) :

			dp[i][j] = 0

			if (i and j) :

				# any suffix of A[0..i]
				# which is a subsequence of B[0..j]
				# is also a subsequence of B[0..j-1]...
				dp[i][j] = dp[i][j - 1]

				# or, if last character matches (i.e.
				# A[i-1] == B[j-1]), and then the rest
				# of the suffix is a suffix of
				# A[0..i-1] and a subsequence of B[j-1]
				if (A[i - 1] == B[j - 1]) :

					dp[i][j] = max(
						dp[i][j],
						1 + dp[i - 1][j - 1])
					r = max(r, dp[i][j])
				

	# r = the length of the
	# longest (contiguous) substring
	# of A that is a subsequence of B
	return len(A) - r


# Driver code
if __name__ == "__main__" :

	A = "edacb"
	B = "abcde"
	print(minOperations(A, B))
	
	# This code is contributed by rakeshsahni
