import copy, time
from collections import defaultdict

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
  path = defaultdict(list)
  while on_map(current_position) and not_visited(map[str(current_position)], direction[direction_index]):
    candidate_position = current_position
    #Find the next spot
    while current_position == candidate_position:
      candidate_position = move(direction[direction_index], current_position)
      if (on_map(candidate_position) and "#" in map[str(candidate_position)]) or candidate_position == current_position:
        candidate_position = current_position
        direction_index = (direction_index + 1) % 4
    if not_visited(path[str(current_position)], direction[direction_index]):
      path[str(current_position)].append(direction[direction_index])
    else:
      break
    current_position = candidate_position
  if on_map(current_position):
    global loops_created
    loops_created += 1
    print("Loop Detected: ", loops_created)
  return path

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

def visited(value):
  if len(value) > 0:
    return True
  return False

def try_all_obstructions(map, path):
  count = 0
  for x in range(max_x):
    for y in range(max_y):
      if map[str([x,y])] != "^" and map[str([x,y])] != "#" and visited(path[str([x,y])]):
        count+=1
        print(count)
        map[str([x,y])] = ["#"]
        navigate(map)
        map[str([x,y])] = ["."]

def main():
  map = build_map_dict(import_data())
  path = navigate(map)
  print("Part 1:", len(path.keys()))
  try_all_obstructions(map, path)
  print("Part 2:", loops_created)
  

main()