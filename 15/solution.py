import time, sys
warehouse_map = {}
starting_pos = (-1,-1)
max_height = 0
max_width = 0

def import_data(filename):
  with open(filename) as file:
    lines = file.read().splitlines()
    read_map_incomplete = True
    instructions = ""
  for i in range(len (lines)): 
    if lines[i] == "":
      global max_height
      max_height = i
      read_map_incomplete = False
    elif read_map_incomplete:
      for j in range(len(lines[i])):
        warehouse_map[(i,j)] = lines[i][j]
        if lines[i][j] == "@":
          global starting_pos
          starting_pos = (i, j)
    else:
      instructions += lines[i]
  return instructions

def import_data_wide(filename):
  with open(filename) as file:
    lines = file.read().splitlines()
    read_map_incomplete = True
    instructions = ""
  for i in range(len (lines)): 
    if lines[i] == "":
      global max_height
      max_height = i - 1
      global max_width
      max_width = (len(lines[i-1])-1)*2
      read_map_incomplete = False
    elif read_map_incomplete:
      for j in range(len(lines[i])):
        set_warehouse_map_values(i,j, lines[i][j])
        if lines[i][j] == "@":
          global starting_pos
          starting_pos = (i, j*2)
    else:
      instructions += lines[i]
  return instructions

def set_warehouse_map_values(i,j, value):
  if value == ".":
    warehouse_map[(i, j * 2)] = "."
    warehouse_map[(i, j * 2 + 1)] = "."
  elif value == "@":
    warehouse_map[(i, j * 2)] = "@"
    warehouse_map[(i, j * 2 + 1)] = "."
  elif value == "#":
    warehouse_map[(i, j * 2)] = "#"
    warehouse_map[(i, j * 2 + 1)] = "#"
  else:
    warehouse_map[(i, j * 2)] = "["
    warehouse_map[(i, j * 2 + 1)] = "]"

def follow_instructions_wide(instructions):
  cur_pos = starting_pos
  for instruction in instructions:
    if instruction == "^" and try_up_wide(cur_pos):
      move_up_wide(cur_pos)
      warehouse_map[cur_pos] = "."
      cur_pos = (cur_pos[0]-1, cur_pos[1])
    elif instruction == "v" and try_down_wide(cur_pos):
      move_down_wide(cur_pos)
      warehouse_map[cur_pos] = "."
      cur_pos = (cur_pos[0]+1, cur_pos[1])
    elif instruction == "<":
      end_move = try_left(cur_pos)
      if end_move != cur_pos:
        while cur_pos != end_move:
          warehouse_map[end_move] = warehouse_map[(end_move[0], end_move[1]+1)]
          end_move = (end_move[0], end_move[1]+1)
        warehouse_map[cur_pos] = "."
        cur_pos = (cur_pos[0], cur_pos[1]-1)
    elif instruction == ">":
      end_move = try_right(cur_pos)
      if end_move != cur_pos:
        while cur_pos != end_move:
          warehouse_map[end_move] = warehouse_map[(end_move[0], end_move[1]-1)]
          end_move = (end_move[0], end_move[1]-1)
        warehouse_map[cur_pos] = "."
        cur_pos = (cur_pos[0], cur_pos[1]+1)
    

def follow_instructions(instructions):
  cur_pos = starting_pos
  for i in range(len(instructions)):
    cur_instruction = instructions[i]
    # print(f"Move ({i}/{len(instructions)}): {cur_instruction}")
    if cur_instruction == "^":
      end_move = try_up(cur_pos)
      if end_move != cur_pos:
        while cur_pos != end_move:
          warehouse_map[end_move] = warehouse_map[(end_move[0]+1, end_move[1])]
          end_move = (end_move[0]+1, end_move[1])
        warehouse_map[cur_pos] = "."
        cur_pos = (cur_pos[0]-1, cur_pos[1])
    elif cur_instruction == "v":
      end_move = try_down(cur_pos)
      if end_move != cur_pos:
        while cur_pos != end_move:
          warehouse_map[end_move] = warehouse_map[(end_move[0]-1, end_move[1])]
          end_move = (end_move[0]-1, end_move[1])
        warehouse_map[cur_pos] = "."
        cur_pos = (cur_pos[0]+1, cur_pos[1])
    elif cur_instruction == "<":
      end_move = try_left(cur_pos)
      if end_move != cur_pos:
        while cur_pos != end_move:
          warehouse_map[end_move] = warehouse_map[(end_move[0], end_move[1]+1)]
          end_move = (end_move[0], end_move[1]+1)
        warehouse_map[cur_pos] = "."
        cur_pos = (cur_pos[0], cur_pos[1]-1)
    else:
      end_move = try_right(cur_pos)
      if end_move != cur_pos:
        while cur_pos != end_move:
          warehouse_map[end_move] = warehouse_map[(end_move[0], end_move[1]-1)]
          end_move = (end_move[0], end_move[1]-1)
        warehouse_map[cur_pos] = "."
        cur_pos = (cur_pos[0], cur_pos[1]+1)

def move_up_wide(cur_pos):
  next_pos = (cur_pos[0]-1, cur_pos[1])
  next_value = warehouse_map[next_pos]
  cur_value = warehouse_map[cur_pos]
  if next_value == "[":
    move_up_wide(next_pos)
    move_up_wide((cur_pos[0]-1, cur_pos[1]+1))
    warehouse_map[(cur_pos[0]-1, cur_pos[1]+1)] = "."
  elif next_value == "]":
    move_up_wide(next_pos)
    move_up_wide((cur_pos[0]-1, cur_pos[1]-1))
    warehouse_map[(cur_pos[0]-1), cur_pos[1]-1] = "."
  warehouse_map[next_pos] = cur_value

def move_down_wide(cur_pos):
  next_pos = (cur_pos[0]+1, cur_pos[1])
  next_value = warehouse_map[next_pos]
  cur_value = warehouse_map[cur_pos]
  if next_value == "[":
    move_down_wide(next_pos)
    move_down_wide((cur_pos[0]+1, cur_pos[1]+1))
    warehouse_map[(cur_pos[0]+1, cur_pos[1]+1)] = "."
  elif next_value == "]":
    move_down_wide(next_pos)
    move_down_wide((cur_pos[0]+1, cur_pos[1]-1))
    warehouse_map[(cur_pos[0]+1), cur_pos[1]-1] = "."
  warehouse_map[next_pos] = cur_value

def try_up_wide(cur_pos):
  next_pos = (cur_pos[0]-1, cur_pos[1])
  if warehouse_map[next_pos] == ".":
    return True
  elif warehouse_map[next_pos] == "#":
    return False
  elif warehouse_map[next_pos] == "[":
    return try_up_wide(next_pos) and try_up_wide((cur_pos[0] - 1, cur_pos[1] + 1))
  else:
    return try_up_wide(next_pos) and try_up_wide((cur_pos[0] - 1, cur_pos[1] - 1))

def try_up(cur_pos):
  next_pos = (cur_pos[0]-1, cur_pos[1])
  while next_pos in warehouse_map and \
        (warehouse_map[next_pos] == "O" or \
          warehouse_map[next_pos] == "[" or \
          warehouse_map[next_pos] == "]"):
    next_pos = (next_pos[0] - 1, next_pos[1])
  if warehouse_map[next_pos] == ".":
    return next_pos
  else:
    return cur_pos 

def try_up_wide(cur_pos):
  next_pos = (cur_pos[0]-1, cur_pos[1])
  if warehouse_map[next_pos] == ".":
    return True
  elif warehouse_map[next_pos] == "#":
    return False
  elif warehouse_map[next_pos] == "[":
    return try_up_wide(next_pos) and try_up_wide((cur_pos[0] - 1, cur_pos[1] + 1))
  else:
    return try_up_wide(next_pos) and try_up_wide((cur_pos[0] - 1, cur_pos[1] - 1))

def try_down_wide(cur_pos):
  next_pos = (cur_pos[0] + 1, cur_pos[1])
  if warehouse_map[next_pos] == ".":
    return True
  elif warehouse_map[next_pos] == "#":
    return False
  elif warehouse_map[next_pos] == "[":
    return try_down_wide(next_pos) and try_down_wide((cur_pos[0] + 1, cur_pos[1] + 1))
  else:
    return try_down_wide(next_pos) and try_down_wide((cur_pos[0] + 1, cur_pos[1] - 1))

def try_down(cur_pos):
  next_pos = (cur_pos[0]+1, cur_pos[1])
  while next_pos in warehouse_map and \
        (warehouse_map[next_pos] == "O" or \
          warehouse_map[next_pos] == "[" or \
          warehouse_map[next_pos] == "]"):
    next_pos = (next_pos[0] + 1, next_pos[1])
  if warehouse_map[next_pos] == ".":
    return next_pos
  else:
    return cur_pos

def try_left(cur_pos):
  next_pos = (cur_pos[0], cur_pos[1]-1)
  while next_pos in warehouse_map and \
        (warehouse_map[next_pos] == "O" or \
          warehouse_map[next_pos] == "[" or \
          warehouse_map[next_pos] == "]"):
    next_pos = (next_pos[0], next_pos[1]-1)
  if warehouse_map[next_pos] == ".":
    return next_pos
  else:
    return cur_pos
  
def try_right(cur_pos):
  next_pos = (cur_pos[0], cur_pos[1]+1)
  while next_pos in warehouse_map and \
        (warehouse_map[next_pos] == "O" or \
          warehouse_map[next_pos] == "[" or \
          warehouse_map[next_pos] == "]"):
    next_pos = (next_pos[0], next_pos[1]+1)
  if warehouse_map[next_pos] == ".":
    return next_pos
  else:
    return cur_pos

def calculate_sum_GPS():
  total = 0
  for key in warehouse_map:
    if warehouse_map[key] == "O" or warehouse_map[key] == "[":
      total += key[0] * 100 + key[1]
  return total

def print_map():
  # for i in range(max_height+1):
  #   sys.stdout.write("\033[F")
  key = (0,0)
  while  key in warehouse_map:
    cur_line = ""
    while key in warehouse_map:
      cur_line += warehouse_map[key]
      key = (key[0], key[1] + 1)
    print(cur_line)
    key = (key[0]+1, 0)
  print()

def main():
  follow_instructions(import_data("sample.txt"))
  print("Sample part 1: ", calculate_sum_GPS())
  print_map()
  print()

  follow_instructions_wide(import_data_wide("sample.txt"))
  print("Sample part 2: ", calculate_sum_GPS())

  print_map()
  print()

  follow_instructions(import_data("input.txt"))
  print("Part 1: ", calculate_sum_GPS())

  print_map()
  print()

  follow_instructions_wide(import_data_wide("input.txt"))
  print("Part 2: ", calculate_sum_GPS())
  print_map()

main()