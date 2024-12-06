starting_position = []
max_x = 0
max_y = 0
loops_created = 0

def import_data():
  with open("input.txt") as file:
    lines = file.read().splitlines()
  return list(map(lambda line: list(line), lines))

def build_map_dict(position_list):
  map = {}
  global max_x
  max_x = len(position_list)
  global max_y
  max_y = len(position_list[0])
  for x in range(max_x):
    for y in range(max_y):
      contents = position_list[x][y]
      map[str([x,y])] = [contents]
      if contents == "^":
        global starting_position
        starting_position = list([x,y])
  return map

def navigate(map):
  direction = ["N", "E", "S", "W"]
  direction_index = 0
  current_position = starting_position
  while on_map(current_position) and not_visited(map[str(current_position)], direction[direction_index]):
    candidate_position = current_position
    #Find the next spot
    while current_position == candidate_position:
      candidate_position = move(direction[direction_index], current_position)
      if (on_map(candidate_position) and "#" in map[str(candidate_position)]) or candidate_position == current_position:
        candidate_position = current_position
        direction_index = (direction_index + 1) % 4
    map[str(current_position)].append(direction[direction_index])
    current_position = candidate_position
  return map

def on_map(position):
  if position[0] >= 0 and position[0] < max_x and position[1] >= 0 and position[1] < max_y:
    return True
  return False

def move(direction, position):
  if direction == "N":
    position = [position[0] - 1, position[1]]
  elif direction == "E":
    position = [position[0], position[1] + 1]
  elif direction == "S":
    position = [position[0] + 1 , position[1]]
  elif direction == "W":
    position = [position[0], position[1] - 1]
  return position
  
def count_visited(map):
  count = 0
  values = list(map.values())
  for value in values:
    if (not_visited(value, "N") and
        not_visited(value, "E") and
        not_visited(value, "S") and
        not_visited(value, "W")):
      count = count
    else:
      count +=1
  return count

def not_visited(value, direction):
  if direction in value:
    return False
  return True

def main():
  solved_map = navigate(build_map_dict(import_data()))
  print(count_visited(solved_map))

main()