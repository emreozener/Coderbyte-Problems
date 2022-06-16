def FindIntersection(strArr):

  s1 = strArr[0]
  s2 = strArr[1]
  l1 = [int(i) for i in s1.split(",")]
  l2 = [int(i) for i in s2.split(",")]

  opt = str()

  for i in l1:
    if i in l2:
      opt += str(i) + ","
  
  opt = opt[:-1]

  if set(l1).intersection(l2) != set():
    return opt
  elif set(l1).intersection(l2) == set():
    return "false"

print(FindIntersection(input()))