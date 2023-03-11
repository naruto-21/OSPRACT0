# Python program to find
# if a given corner string
# is present at corners.

def isCornerPresent(str, corner) :

	n = len(str)
	cl = len(corner)

	# If length of corner
	# string is more, it
	# cannot be present
	# at corners.
	if (n < cl) :
		return False

	# Return true if corner
	# string is present at
	# both corners of given
	# string.
	return ((str[: cl] == corner) and
			(str[n - cl :] == corner))

# Driver Code
str = "geeksforgeeks"
corner = "geeks"
if (isCornerPresent(str, corner)) :
	print ("Yes")
else :
	print ("No")

# This code is contributed by
# Manish Shaw(manishshaw1)
