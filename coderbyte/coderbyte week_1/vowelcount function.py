def VowelCount(strParam):
  vowels = str()
  for i in strParam:
    if i in "aeiouAEIOU": vowels += i
  return len(vowels)

print(VowelCount(input()))
