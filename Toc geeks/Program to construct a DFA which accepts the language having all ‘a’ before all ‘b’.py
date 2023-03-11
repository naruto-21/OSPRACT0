# Function for state zero Q0
def startStateQ0(s):
	if (s == 'a'):
		state = 1
	elif (s == 'b'):
		state = 2
	else:
		state = -1
	return state

# Function for first state Q1
def firstStateQ1(s):
	if (s == 'a'):
		state = 1
	elif (s == 'b'):
		state = 2
	else:
		state = -1
	return state

# Function for second state Q2
def secondStateQ2(s):
	if (s == 'b'):
		state = 2
	elif (s == 'a'):
		state = 3
	else:
		state = -1
	return state

# Function for third state Q3
def thirdStateQ3(s):
	state = 3
	return state

#Function to check
#if the string is accepted or not
def isAcceptedString(String):
	l = len(String)

	# dfa tells the number associated
	# with the present dfa = state
	state = 0
	for i in range(l):
		if (state == 0):
			state = startStateQ0(String[i])
		elif (state == 1):
			state = firstStateQ1(String[i])
		elif (state == 2):
			state = secondStateQ2(String[i])
		elif (state == 3):
			state = thirdStateQ3(String[i])
		else:
			return 0
	if(state == 1 or state == 2):
		return 1
	else:
		return 0

# Driver code
if __name__ == "__main__":

	String = "ba"
	if (isAcceptedString(String)):
		print("ACCEPTED")
	else:
		print("NOT ACCEPTED")
