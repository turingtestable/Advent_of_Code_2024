def import_data():
  with open("input.txt") as file:
    lines = file.read().splitlines()
  return list(map(lambda line: list(line), lines))

def count_x_mas(lines):
  count = 0
  for x in range(len(lines)):
    for y in range(len(lines[x])):
      if lines[x][y] == "A":
        count += find_x_mas(x, y, lines)
  return count

def find_x_mas(x, y, lines):
  if x - 1 >= 0 and y - 1 >= 0 and x + 1 < len(lines) and y + 1 <(len(lines[x])):
    stroke_1 = str(lines[x-1][y-1]) + str(lines[x+1][y+1])
    stroke_2 = str(lines[x-1][y+1]) + str(lines[x+1][y-1])
    if (stroke_1 == "MS" or stroke_1 == "SM") and (stroke_2 == "MS" or stroke_2 == "SM"):
      return 1
  return 0  

def count_xmas(lines):
  count = 0
  for x in range(len(lines)):
    for y in range(len(lines[x])):
      if lines[x][y] == "X":
        count += find_xmas(x, y, lines)
  return count

def find_xmas(x, y, lines):
  count = 0
  mas = "MAS"
  if x - 3 >= 0:
    #NW
    if y - 3 >= 0 and mas == lines[x-1][y-1] + lines[x-2][y-2] + lines[x-3][y-3]:
      count +=1
    #NE
    if y + 3 < len(lines[x]) and mas == lines[x-1][y+1] + lines[x-2][y+2] + lines[x-3][y+3]:
      count += 1
    #N
    if mas == lines[x-1][y] + lines[x-2][y] + lines[x-3][y]:
      count += 1
  if x + 3 < len(lines):
    #SW
    if y - 3 >= 0 and mas == lines[x+1][y-1] + lines[x+2][y-2] + lines[x+3][y-3]:
      count +=1
    #SE
    if y + 3 < len(lines[x]) and mas == lines[x+1][y+1] + lines[x+2][y+2] + lines[x+3][y+3]:
      count += 1
    #S
    if mas == lines[x+1][y] + lines[x+2][y] + lines[x+3][y]:
      count += 1
  #W
  if y - 3 >= 0 and mas == lines[x][y-1] + lines[x][y-2] + lines[x][y-3]:
    count +=1
  #E
  if y + 3 < len(lines[x]):
    if mas == lines[x][y+1] + lines[x][y+2] + lines[x][y+3]:
      count += 1
  return count


def main():
  print("XMAS count:")
  print(count_xmas(import_data()))
  print("X-MAS count:")
  print(count_x_mas(import_data()))

main()