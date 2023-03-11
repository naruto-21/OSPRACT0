# Python program for the above approach

import threading

count = [0] * 4
str = "prrrogramisprrrogramming"
sub = "rr"

def str_seq_count(value):
	global count
	l1 = len(str)
	l2 = len(sub)
	for i in range(value, l1, 4):
		flag = 0
		k = i
		for j in range(l2):
			if sub[j] == str[k]:
				k += 1
			else:
				flag = 1
				break
		if flag == 0:
			count[value] += 1

if __name__ == '__main__':
	total_count = 0
	x = [i for i in range(4)]
	print("Enter the main string: ", str)
	print("Enter the sequence to search: ", sub)

	threads = []
	for i in range(4):
		t = threading.Thread(target=str_seq_count, args=(x[i],))
		threads.append(t)
		t.start()
	for t in threads:
		t.join()

	total_count = sum(count)
	print("Frequency of substring: ", total_count)

# This code is contributed by codebraxnzt
