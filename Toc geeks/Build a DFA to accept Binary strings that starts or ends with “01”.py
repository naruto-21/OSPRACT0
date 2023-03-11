# Python3 program to check if
# a string either starts or
# ends with 01

# Function for transition
# state A
def checkstateA(n):

	# State transition to
	# B if the character is
	# 0
	if(n[0]=='0'):
		stateB(n[1:])

	# State transition to
	# D if the character is
	# 1
	else:
		stateD(n[1:])

# Function for transition
# state B		
def stateB(n):

	# Check if the string has
	# ended
	if (len(n)== 0):
		print("string not accepted")
	else:
	
		# State transition to C
		# if the character is 1
		if(n[0]=='1'):
			stateC(n[1:])

		# State transition to D
		# if the character is 0
		else:
			stateD(n[1:])
		
# Function for transition
# state C
def stateC(n):
	print("String accepted")

# Function for transition
# state D
def stateD(n):
	if (len(n)== 0):
		print("string not accepted")
	else:

		# State transition to D
		# if the character is 1
		if (n[0]=='1'):
			stateD(n[1:])

		# State transition to E
		# if the character is 0
		else:
			stateE(n[1:])

# Function for transition
# state E
def stateE(n):
	if (len(n)== 0):
		print("string not accepted")
	else:

		# State transition to E
		# if the character is 0
		if(n[0]=='0'):
			stateE(n[1:])

		# State transition to F
		# if the character is 1
		else:
			stateF(n[1:])

# Function for transition
# state F
def stateF(n):
	if(len(n)== 0):
		print("string accepred")
	else:

		# State transition to D
		# if the character is 1
		if(n[0]=='1'):
			stateD(n[1:])

		# State transition to E
		# if the character is 0
		else:
			stateE(n[1:])
	
# Driver code
if __name__ == "__main__":
	n = "0100101"
	checkstateA(n)
