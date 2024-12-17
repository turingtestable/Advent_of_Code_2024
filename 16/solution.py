import sys, heapq, copy
from collections import defaultdict

starting_pos = (-1,-1)
ending_pos = (-1,-1)
minimum_cost = sys.maxsize
directions = [(1,0), (0,1), (-1,0), (0,-1)]
max_i = 0
max_j = 0

def import_data(filename):
  with open(filename) as file:
    maze_map = list(file.read().splitlines())
    maze_dict = {}
    global max_i
    max_i = len(maze_map)
    global max_j
    max_j = len(maze_map[0])
    for i in range(max_i):
      for j in range(max_j):
        maze_dict[(i,j)] = maze_map[i][j]
        if maze_dict[(i,j)] == "S":
          global starting_pos
          starting_pos = (i,j)
        elif maze_dict[(i,j)] == "E":
          global ending_pos
          ending_pos = (i,j)
    return maze_dict

def djikstra(maze):
  distance_dict = defaultdict(lambda: (sys.maxsize))
  distance_dict[starting_pos] = 0
  unvisited = set(maze.keys())
  current = starting_pos
  predecessors = defaultdict(list)
  predecessors[current].append(current)
  heap = []
  direction = (0,1)
  loop_counter = 0 
  while len(unvisited) > 0:
    loop_counter += 1
    unvisited_neighbors = []
    for dir in directions:
      pos = (add(dir, current), dir)
      step_cost = 0
      if pos[1] == direction:
        step_cost = 1
      elif pos[1] == (-direction[0], -direction[1]):
        step_cost = 2001
      else:
        step_cost = 1001
      
      if distance_dict[current] + step_cost <= distance_dict[pos[0]]:
        new_cost = distance_dict[current] + step_cost
        if new_cost == distance_dict[pos[0]]:
          predecessors[pos[0]].append(current)
        elif new_cost < distance_dict[pos[0]]:
          predecessors[pos[0]] = [current]
          distance_dict[pos[0]] = new_cost
      heapq.heappush(heap, (new_cost, pos[0], pos[1]))
    unvisited.remove(current)
    next_pos = heapq.heappop(heap)
    while next_pos[1] not in unvisited or maze[next_pos[1]] == "#":
      if next_pos[1] in unvisited and maze[next_pos[1]] == "#":
        unvisited.remove(next_pos[1])
      if len(heap) == 0:
        print("Early Part 1: ", distance_dict[ending_pos])
        return predecessors
      next_pos = heapq.heappop(heap)
    current = next_pos[1]
    direction = next_pos[2]
  print("Part 1: ", distance_dict[ending_pos])
  return predecessors 

def navigate(predecessors, new_maze, current):
  if current != starting_pos:
    for predecessor in predecessors[current]:
      new_maze[current] = "O"
      navigate(predecessors, new_maze, predecessor)
  else:
    new_maze[current] = "O"

def add(tuple1, tuple2):
  return tuple(map(sum, zip(tuple1, tuple2)))

def print_map(maze):
  for i in range(max_i):
    line = ""
    for j in range(max_j):
      line += maze[(i,j)]
    print(line)


def main():
  maze = import_data("sample.txt")
  new_maze = copy.deepcopy(maze)
  navigate(djikstra(maze), new_maze, ending_pos)
  print("Part 2: ", list(new_maze.values()).count("O"))
  print_map(new_maze)
  maze = import_data("sample2.txt")
  new_maze = copy.deepcopy(maze)
  navigate(djikstra(maze), new_maze, ending_pos)
  print("Part 2: ", list(new_maze.values()).count("O"))
  print_map(new_maze)
  maze = import_data("input.txt")
  new_maze = copy.deepcopy(maze)
  navigate(djikstra(maze), new_maze, ending_pos)
  print_map(new_maze)
  #print("Part 2: ", list(new_maze.values()).count("0") )

main()