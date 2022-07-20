def TwoSum(arr):

	l_sums = list()
	one_sum = list()

	for i in arr:
		for k in arr[arr.index(i)+1:]: #was "for k in arr[arr.index(i):]:" and it takes half of arr[0] 2 times if it exists
			if i + k == arr[0]:
				one_sum = list()
				one_sum.append(str(i))
				one_sum.append(str(k))
				u = ",".join(one_sum)

				l_sums.append(u)

	if l_sums != []:
		b = " ".join(l_sums)
		return b
	else:
		return -1

TwoSum(input())

#I don't understand why return b doesn't work.

"""
1. For input [8, -5, 4, 2, 7, -6, 4] the output was incorrect. The correct output is 4,4

2. For input [8, 1, 2, 3, 4, 5, 7] the output was incorrect. The correct output is 1,7 3,5

3. For input [4, 5, 2, 1] the output was incorrect. The correct output is -1

1 and 3 solved
"""

"""
line 7 still wrong. takes last element twice if it is the half of arr[0].
as in: For input [8, -5, 4, 2, 7, -6, 4].
"""