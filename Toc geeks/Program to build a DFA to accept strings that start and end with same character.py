# Python3 Program for DFA that accepts string
# if it starts and ends with same character

# Function for the state Q1
def q1(s, i):

	# Condition to check end of string
	if (i == len(s)):
		print("Yes");
		return;
	
	# State transitions
	# 'a' takes to q1, and
	# 'b' takes to q2
	if (s[i] == 'a'):
		q1(s, i + 1);
	else:
		q2(s, i + 1);

# Function for the state Q2
def q2(s, i):
	
	# Condition to check end of string
	if (i == len(s)):
		print("No");
		return;
	
	# State transitions
	# 'a' takes to q1, and
	# 'b' takes to q2
	if (s[i] == 'a'):
		q1(s, i + 1);
	else:
		q2(s, i + 1);

# Function for the state Q3
def q3(s, i):
	
	# Condition to check end of string
	if (i == len(s)):
		print("Yes");
		return;
	
	# State transitions
	# 'a' takes to q4, and
	# 'b' takes to q3
	if (s[i] == 'a'):
		q4(s, i + 1);
	else:
		q3(s, i + 1);

# Function for the state Q4
def q4(s, i):
	
	# Condition to check end of string
	if (i == s.length()):
		print("No");
		return;
	
	# State transitions
	# 'a' takes to q4, and
	# 'b' takes to q3
	if (s[i] == 'a'):
		q4(s, i + 1);
	else:
		q3(s, i + 1);

# Function for the state Q0
def q0(s, i):

	# Condition to check end of string
	if (i == len(s)):
		print("No");
		return;
	
	# State transitions
	# 'a' takes to q1, and
	# 'b' takes to q3
	if (s[i] == 'a'):
		q1(s, i + 1);
	else:
		q3(s, i + 1);

# Driver Code
if __name__ == '__main__':
	s = "abbaabb";

	# Since q0 is the starting state
	# Send the string to q0
	q0(s, 0);
	
# This code is contributed by Rajput-Ji
