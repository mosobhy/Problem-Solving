def find_one_location(a):   # a stands for the array input
  loc = []
  for i in range(1, 6):     # i have started the count from 1, because he said to me to this
    for j in range(1, 6):
      if a[i-1][j-1] == 1:
        loc.extend([i, j])
  return loc

def get_number_of_moves(one_loc):
  moves = 0
  while True:
    if one_loc[0] == 3 and one_loc[1] == 3:
      break

    else:
      if one_loc[0] < 3:
        one_loc[0] += 1
        moves += 1

      elif one_loc[0] > 3:
        one_loc[0] -= 1
        moves += 1

      if one_loc[1] < 3:
        one_loc[1] += 1
        moves += 1

      elif one_loc[1] > 3:
        one_loc[1] -= 1
        moves += 1

  return moves

if __name__ == '__main__':

  # getting a two dimensional array from the user
  a=[]
  for i in range(0,5):
    a.append([int(j) for j in input().split()])

  # pass it to get the one location
  location = find_one_location(a)

  # get teh nubmer of moves to beautify the matrix
  moves = get_number_of_moves(location)
  print(moves)
