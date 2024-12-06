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
  map = defaultdict(list)
  global max_x
  max_x = len(position_list)
  global max_y
  max_y = len(position_list[0])
  for x in range(max_x):
    for y in range(max_y):
      contents = position_list[x][y]
      map[str([x,y])].append(contents)
      if contents == "^":
        global starting_position
        starting_position = list([x,y])
  return map

def navigate(map):
  direction = ["N", "E", "S", "W"]
  direction_index = 0
  current_position = starting_position
  path = defaultdict(list)
  while on_map(current_position) and not visited(path[str(current_position)], direction[direction_index]):
    candidate_position = current_position
    #Find the next spot
    while current_position == candidate_position:
      #Try to move
      candidate_position = move(direction[direction_index], current_position)
      #If obstructed turn to the right
      if ("#" in map[str(candidate_position)]):
        candidate_position = current_position
        direction_index = (direction_index + 1) % 4
    #Check for loop
    if not visited(path[str(current_position)], direction[direction_index]):
      path[str(current_position)].append(direction[direction_index])
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

def visited(value, direction):
  if direction in value:
    return True
  return False

def try_all_obstructions(map, path):
  for candidate in path.keys():
    if map[candidate] != "^":
      map[candidate] = ["#"]
      navigate(map)
      map[candidate] = ["."]

def main():
  map = build_map_dict(import_data())
  path = navigate(map)
  try_all_obstructions(map, path)
  print("Part 1:", len(path.keys()))
  print("Part 2:", loops_created)
  

main()