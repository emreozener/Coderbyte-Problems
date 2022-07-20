def ChessboardTraveling(strParam):

  # Evaluates the number of possible ways to travel from a space on a chess board to another space on the chess board by only going up and right.
  x = int(strParam[1])
  y = int(strParam[3])
  a = int(strParam[6])
  b = int(strParam[8])

  # The number of possible ways to travel to a space is the sum of possible ways to travel the space below and left.

  m = (b-y)+1 #rows of the matrix
  n = (a-x)+1 #columns of the matrix

  # the mxn matrix, the row m and the first column consist of element a = 1. 
  # since they can only be traveled to by one possible way.
  # elements in this matrix correspond to the number of ways possible to travel to a space.

  row = [1]
  for _ in range(n-1):
    row.append(0)

  matrix = []
  for _ in range(m-1):
    matrix.append(row)
  matrix.append([1 for _ in range(n)])

  # rows are inversed for easier calculation:

  mi = matrix[::-1]

  # matrix is flattened for easier calculation:

  flattened = list()

  """ this part sums up the values of the elements below and left of an element (before inversion) 
  that correspond to spaces on the board. The sum is the value of that element. """

  for c in mi:
    for i in c:
      flattened.append(i)

  for i in flattened:
    if i == 0:
      flattened[flattened.index(i)] = flattened[flattened.index(i)-1] + flattened[flattened.index(i)-n]

  # Returns the last value of element, hence the number of routes to go to a space.
  return flattened[-1]

while True == True:
  print(ChessboardTraveling(input()))

