with open('integerArray.txt') as f:
	IntArray = f.readlines()
IntArray = map(long, IntArray)

def MergeCount(A,B):
	count = 0
	M = []
	while A and B:
		if A[0] <= B[0]:
			M.append(A.pop(0))
		else:
			count += len(A)
			M.append(B.pop(0))
	M += A + B
	return M, count

def SortCount(A):
	l = len(A)
	if l==1:
		return A, 0
	else:
		left = A[:l//2]
		right = A[l//2:]
		X, x = SortCount(left)
		Y, y = SortCount(right)
		Z, z = MergeCount(X,Y)
		print x+y+z
		return Z, x+y+z

#TestArray = [1, 2, 4, 5, 0, 7,]
#SortCount(TestArray)
SortCount(IntArray)