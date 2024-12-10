from collections import defaultdict

max_i = 0
max_j = 0
starting_pos_list = []

def import_data():
  with open("input.txt") as file:
    lines = file.read().splitlines()
    return list(map(lambda line: list(line), lines))

def build_map_dict(lines):
  map = defaultdict(list)
  global max_i
  max_i = len(lines)
  global max_j
  max_j = len(lines[0])
  for i in range(max_i):
    for j in range(max_j):
      contents = lines[i][j]
      map[(i,j)].append(int(contents))
      if contents == "0":
        global starting_pos_list
        starting_pos_list.append((i,j))
  return map

def sum_trailhead(map):
  trailhead_value = 0
  trailhead_rating = 0 
  for starting_pos in starting_pos_list:
    trailhead_value += len(navigate_trail(map, starting_pos, -1))
    trailhead_rating += navigate_ratings(map, starting_pos, -1)
  print("Part 1: ", trailhead_value)
  return trailhead_rating


def navigate_trail(map, cur_pos, last_pos_value):
  trail_sum = 0
  value_list = map[cur_pos]
  if len(value_list) == 0 or value_list[0] != 1 + last_pos_value:
    return set()
  value = value_list[0]
  if value == 9:
    return {cur_pos}
  else:
    return navigate_trail(map, (cur_pos[0]-1, cur_pos[1]), value) | \
      navigate_trail(map, (cur_pos[0]+1, cur_pos[1]), value) | \
      navigate_trail(map, (cur_pos[0], cur_pos[1]-1), value) | \
      navigate_trail(map, (cur_pos[0], cur_pos[1]+1), value)

def navigate_ratings(map, cur_pos, last_pos_value):
  trail_sum = 0
  value_list = map[cur_pos]
  if len(value_list) == 0 or value_list[0] != 1 + last_pos_value:
    return 0
  value = value_list[0]
  if value == 9:
    return 1
  else:
    return navigate_ratings(map, (cur_pos[0]-1, cur_pos[1]), value) + \
      navigate_ratings(map, (cur_pos[0]+1, cur_pos[1]), value) + \
      navigate_ratings(map, (cur_pos[0], cur_pos[1]-1), value) + \
      navigate_ratings(map, (cur_pos[0], cur_pos[1]+1), value)

def main():
  map_dict = build_map_dict(import_data())
  print("Part 2: ", sum_trailhead(map_dict))

main()