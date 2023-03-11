# Python Program to DFA that accept Strings
# which starts and end with 'a' over input(a, b)
import random

# for producing different random
# numbers every time.
r = random.Random()

# random length of String from 1 - 16
# we are taking input from input stream,
# we can take delimiter to end the String
max = 1 + r.randint(0, 14)

# generating random String and processing it
i = 0
while i < max:

	# producing random character over
	# input alphabet (a, b)
	c = chr(ord('a') + r.randint(0, 1))
	print(c, end=" ")
	i += 1

	# first character is 'a'
	if c == 'a':

		# if there is only 1 character
		# i.e. 'a'
		if i == max:
			print("YES")

		while i < max:
			c = chr(ord('a') + r.randint(0, 1))
			print(c, end=" ")
			i += 1

			# if character is 'a' and it
			# is the last character
			if c == 'a' and i == max:
				print("\nYES")

			# if character is 'b' and it
			# is the last character
			elif i == max:
				print("\nNO")
	# first character is 'b' so no matter
	# what the String is, it is not going
	# to be accepted
	else:
		while i < max:
			c = chr(ord('a') + r.randint(0, 1))
			print(c, end=" ")
			i += 1
		print("\nNO")
		
# This code is contributed by codebraxznt
