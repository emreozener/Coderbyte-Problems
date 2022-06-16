def EvenPairs(strParam):

  #this block converts elements in l_s from str to int when possible
  param2 = list()

  for i in strParam:
    if i in [str(j) for j in list(range(0,10))]:
      param2.append(eval(i))
    else: param2.append(i)

  """following part counts number of even digits between strings. if even digits >= 2 then there
  are always 2 possible even numbers back to back."""
  count = 0

  for i in param2:
    if type(i) == int:
      if i % 2 == 0:
        count += 1
    elif type(i) != int:
      if count < 2:
        count = 0
  
  if count >= 2: return "true"
  else: return "false"

print(EvenPairs(input()))