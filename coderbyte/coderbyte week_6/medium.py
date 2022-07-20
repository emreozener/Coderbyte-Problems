import itertools

def PermutationStep(num):
  #returns the next number greater than num using the same digits

  a = [int(i) for i in list(str(num))] #integer input changed to list of numbers
  permuts = list(itertools.permutations(a)) #list of permutations possible from given num
  permuts = list(set(permuts)) #removes duplicates

  #following block to change permutations (x, y, z) to "xyz"
  permuts_ = list() 
  for i in permuts:
    permuts_.append("".join(str(k) for k in i))

  permuts_ = [int(i) for i in permuts_] #to change str elements to int

  b = sorted(permuts_) #sorts permuts_ list 
  num_index = b.index(num)

  return b[num_index+1]

print(PermutationStep(input()))