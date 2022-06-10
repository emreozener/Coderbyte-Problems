def RomanNumeralReduction(strParam):
  
  #This part converts the roman number to integer
  num = int()
  for i in strParam:
    if i == "I": num += 1
    elif i == "V": num += 5
    elif i == "X": num += 10
    elif i == "L": num += 50
    elif i == "C": num += 100
    elif i == "D": num += 500
    elif i == "M": num += 1000
 
  roman_num = str()
#A letter can't occur more than 3 times in a row in a roman number.

  M = ["", "M", "MM", "MMM"] #thousands
  C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] #hundreds
  X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"] #tens
  I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VII", "IX"] #ones

  thousands = M[num // 1000]
  hundreds = C[(num % 1000) // 100]
  tens = X[(num % 100) // 10]
  ones = I[(num % 10) // 1]

  roman_num = (thousands + hundreds + tens + ones)

  return roman_num

print(RomanNumeralReduction(input()))
