# binary search
def binary_search(seq, n):
	first = 0
	last = len(seq) - 1

	while True:
		if last < first:
			return False
		m = (first + last) // 2
		if seq[m] < n:
			first = m + 1
		elif seq[m] > n:
			last = m - 1
		else:
			print m
			return m
