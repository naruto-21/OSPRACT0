def stateq0(n):
	#if length found 0
	#print not accepted
	if (len(n)==0):
		print("string accepted")
	else:
		
		#if at index 0
		#'0' found call
		#function stateq0
		if(n[0]=='0'):
			stateq0(n[1:])
			
		#else if '1' found
		#call function q1.
		elif (n[0]=='1'):
			stateq1(n[1:])

def stateq1(n):
	#if length found 0
	#print not accepted
	if (len(n)==0):
		print("string not accepted")
	else:
		
		#if at index 0
		#'0' found call
		#function stateq0
		if(n[0]=='0'):
			stateq0(n[1:])
			
		#else if '1' found
		#call function q1.
		elif (n[0]=='1'):
			stateq1(n[1:])		
		

#take number from user
n=int(input())
#converting number to binary
n = bin(n).replace("0b", "")

#call stateA
#to check the input
stateq0(n)
