# Python3 program to find maximum
# occurred of a string

# function to return maximum occurred
# substring of a string
def MaxFreq(s):
	
	# size of string
	n = len(s)
	
	m = dict()
	
	for i in range(n):
		string = ''
		for j in range(i, n):
			string += s[j]
			if string in m.keys():
				m[string] += 1
			else:
				m[string] = 1
				
	# to store maximum frequency
	maxi = 0
	
	# To store string which has
	# maximum frequency
	maxi_str = ''
	
	for i in m:
		if m[i] > maxi:
			maxi = m[i]
			maxi_str = i
		elif m[i] == maxi:
			ss = i
			if len(ss) > len(maxi_str):
				maxi_str = ss
				
	# return substring which has maximum freq
	return maxi_str
	
# Driver code
string = "ababecdecd"

print(MaxFreq(string))
		
# This code is contributed by Mohit kumar 29	
