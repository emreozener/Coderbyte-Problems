def CoinDeterminer(num):
  #determines smallest number of coins possible to form a sum for given number. coins consist of 1,5,7,9 

  count = 0

  count += num // 11
  new_num = num % 11

  count += new_num // 9
  new_num = new_num % 9

  count += new_num // 7
  new_num = new_num % 7

  count += new_num // 5
  new_num = new_num % 5

  count += new_num // 1

  """
  could also ne written as: 

  count = 0

  count += num // 11
  new_num = % 11

  for i in [1,5,7,9][::-1]:
     count += num // i
    new_num = new_num % i
  
  """

  #bottom part did not exist in the prior code
  count_2 = 0

  count_2 += num // 9
  new_num_2 = num % 9

  for i in [1,5,7][::-1]:
    count_2 += num // i
    new_num_2 = new_num_2 % i

  count_3 = 0

  count_3 += num // 7
  new_num_3 = num % 7

  for i in [1,5][::-1]:
    count_3 += num // i
    new_num_3 = new_num_3 % i

  count_4 = 0

  count_4 += num // 5
  new_num_4 = num // 5

  count_4 += new_num_4

  return min([count, count_2, count_3, count_4])
  return [count, count_2, count_3, count_4]


print(CoinDeterminer(input()))

#should be checked. did not work for certain cases. num = 25,37,14