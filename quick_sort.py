with open('QuickSort.txt') as f:
	IntArray = f.readlines()
IntArray = map(long, IntArray)

def PartitionFirst(A,l,r):
	p = A[l]
	i = l+1
	for j in range(l+1,r):
		if A[j] < p:
			A[i], A[j] = A[j], A[i]
			i += 1
	A[l], A[i-1] = A[i-1], A[l]
	return i-1

def PartitionLast(A,l,r):
	p = A[r-1]
	i = l+1
	A[r-1], A[l] = A[l], p
	for j in range(l+1,r):
		if A[j] < p:
			A[i], A[j] = A[j], A[i]
			i += 1
	A[l], A[i-1] = A[i-1], A[l]
	return i-1

def median(x,y,z):
	if (x-y)*(z-x) >= 0:
		return x
	elif (y-x)*(z-y) >= 0:
		return y
	else:
		return z

def PartitionMedian(A,l,r):
	left = A[l]
	right = A[r-1]
	length = r-l
	if length%2==0:
		middle = A[l+length/2-1]
	else:
		middle = A[l+length/2]

	p = median(left,right,middle)
	pindex = A.index(p)
	A[pindex], A[l] = A[l], p
	i = l+1
	for j in range(l+1,r):
		if A[j] < p:
			A[i], A[j] = A[j], A[i]
			i += 1
	A[l], A[i-1] = A[i-1], A[l]
	return i-1

def QuickSortFirst(A,l,r):
	global first
	if l < r:
		newpindex = PartitionFirst(A,l,r)
		first += (r-l-1)
		QuickSortFirst(A,l,newpindex)
		QuickSortFirst(A,newpindex+1,r)

def QuickSortLast(A,l,r):
	global last
	if l < r:
		newpindex = PartitionLast(A,l,r)
		last += (r-l-1)
		QuickSortLast(A,l,newpindex)
		QuickSortLast(A,newpindex+1,r)

def QuickSortMedian(A,l,r):
	global med
	if l < r:
		newpindex = PartitionMedian(A,l,r)
		med += (r-l-1)
		QuickSortMedian(A,l,newpindex)
		QuickSortMedian(A,newpindex+1,r)

first = 0
last = 0
med = 0

# QuickSortFirst(IntArray,0,len(IntArray))
# print first
# QuickSortLast(IntArray,0,len(IntArray))
# print last
# QuickSortMedian(IntArray,0,len(IntArray))	
# print med
