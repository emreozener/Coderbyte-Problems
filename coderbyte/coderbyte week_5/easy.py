def SimpleSymbols(strParam):

  if strParam[0].isalpha() == True or strParam[-1].isalpha() == True:
    return "False" 
  else:
    for i in strParam:
      if i.isalpha() == True:
        if strParam[strParam.index(i)+1] == "+" and strParam[strParam.index(i)-1] == "+":
            return "True"
        else: return "False"
  
print(SimpleSymbols(input()))