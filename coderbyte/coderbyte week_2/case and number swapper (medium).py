def SwapII(strParam):

  swapped = list(strParam.swapcase())

  for i in swapped:
      if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        for k in swapped[swapped.index(i)+1::]:
          if k in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            str_inbetween = "".join(swapped[swapped.index(i)+1:swapped.index(k)])
            if str_inbetween.isalpha() == True:
              a, b = swapped.index(i), swapped.index(k)
              swapped[a], swapped[b] = swapped[b], swapped[a]
          
  return "".join(swapped)

print(SwapII(input()))
