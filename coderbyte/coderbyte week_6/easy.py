def DashInsert(strParam):

  listp = list(strParam)
  c = [str(k) for k in list(range(10))[1::2]]

  for index in range(len(listp)):
    if listp[index] in c and listp[index+1] in c:
      listp[index+1:index+1] = ["-"]

  return "".join(listp)

print(DashInsert(input()))

""" 
didn't work for:

1. For input "567" the output was incorrect. The correct output is 567

2. For input "77993" the output was incorrect. The correct output is 7-7-9-9-3

3. For input "2129" the output was incorrect. The correct output is 2129

4. For input "667488958374553" the output was incorrect. The correct output is 6674889-583-745-5-3 
"""