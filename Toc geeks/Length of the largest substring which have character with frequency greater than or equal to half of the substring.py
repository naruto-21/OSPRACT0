# Python3 implementation of the above approach
import sys

# Function to return the length
# of the longest sub string
# having frequency of a character
# greater than half of the length
# of the sub string
def maxLength(s, n) :
	
	ans = -(sys.maxsize + 1);
	A, L, R = [], [], [];
	freq = [0] * (n + 5);

	# for each of the character 'a' to 'z'
	for i in range(26) :
		count = 0;
		
		# finding frequency prefix array
		# of the character
		for j in range(n) :
			if (ord(s[j]) - ord('a') == i) :
				count += 1;
				
			freq[j] = count;
		
		# Finding the r[] and l[] arrays.
		for j in range(n) :
			L.append((2 * freq[j - 1]) - j);
			R.append((2 * freq[j]) - j);
		
		max_len = -(sys.maxsize + 1);
		min_val = sys.maxsize ;

		# for each j from 0 to n
		for j in range(n) :
			min_val = min(min_val, L[j]);
			A.append(min_val);

			l = 0; r = j;

			# Finding the lower bound of i.
			while (l <= r) :
				mid = (l + r) >> 1;
				if (A[mid] <= R[j]) :
					max_len = max(max_len, j - mid + 1);
					r = mid - 1;
				
				else :
					l = mid + 1;

		# storing the maximum value of i - j + 1
		ans = max(ans, max_len);

		# clearing all the vector so that it can
		# be used for other characters.
		A.clear();
		R.clear();
		L.clear();

	return ans;

# Driver Code
if __name__ == "__main__" :

	s = "ababbbacbcbcca";
	n = len(s);

	print(maxLength(s, n));

# This code is contributed by AnkitRai01
