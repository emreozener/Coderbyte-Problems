def Palindrome(strParam):

  l_param = strParam.split(" ")
  c_param = str()
  for i in l_param:
    c_param += i

  if c_param == c_param[::-1]:
    return "true"
  else:
    return "false"

# keep this function call here 
print(Palindrome(input()))