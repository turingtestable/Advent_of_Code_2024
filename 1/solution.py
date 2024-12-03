from collections import Counter

def importData():
  with open("input.txt") as file:
    lines_array = file.read().splitlines()
  col_1,col_2 = [],[]
  for line in lines_array:
    line_arr = line.split()
    col_1.append(int(line_arr[0]))
    col_2.append(int(line_arr[1]))

  col_1.sort()
  col_2.sort()
  return [col_1, col_2]

def calc_distance(columns, pos):
  return abs(columns[0][pos]-columns[1][pos])

def sum_distance(columns):
  total_distance = 0
  position = 0 
  while position < len(columns[0]):
    total_distance += calc_distance(columns, position)
    position += 1
  return total_distance

def similarity_score(columns):
  similarity_score = 0
  frequencies = Counter(columns[1])
  for entry in columns[0]:
    if entry in frequencies:
      similarity_score += entry * frequencies[entry]
  return similarity_score



def main():
  columns = importData()
  print("part 1:")
  print(sum_distance(columns))
  print("part 2:")
  print(similarity_score(columns))

main()

