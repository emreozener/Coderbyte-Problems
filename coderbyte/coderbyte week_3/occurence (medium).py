def SimpleMode(arr):

  #this part creates dictionary that shows how much each number occured within the array: (arr).
  counter = {}
  
  for number in arr:
    if number not in counter:
      counter[number] = 0
    counter[number] += 1

  #this part forms a list from the values of the counter dictionary. Then finds the biggest occurence.
  counter_values = list(counter.values())
  v_index = counter_values.index(max(counter_values))

  #this part returns what occured max. If max occurence is 1: it returns -1.
  if max(counter_values) > 1:
    return list(counter.keys())[v_index]
  else: return -1

print(SimpleMode(input()))