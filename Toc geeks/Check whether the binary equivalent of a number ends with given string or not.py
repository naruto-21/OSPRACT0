# Python3 implementation of the
# above approach

# Function returns true if
# s1 is suffix of s2
def isSuffix(s1, s2):

	n1 = len(s1)
	n2 = len(s2)
	
	if(n1 > n2):
		return False
	for i in range(n1):
	
		if (s1[n1 - i - 1] !=
			s2[n2 - i - 1]):
			return False;
	return True;

# Function to check if
# binary equivalent of a
# number ends in "111" or not
def CheckBinaryEquivalent(N, s):

	# To store the binary
	# number
	B_Number = 0;
	cnt = 0;

	while (N != 0):

		rem = N % 2;
		c = pow(10, cnt);
		B_Number += rem * c;
		N //= 2;

		# Count used to store
		# exponent value
		cnt += 1;

	bin = str(B_Number);
	return isSuffix(s, bin);

# Driver code
if __name__ == "__main__":
	
	N = 23;
	s = "111";
	
	if (CheckBinaryEquivalent(N, s)):
		print("Yes")
	else:
		print("No")

# This code is contributed by rutvik_56
