import sys
from functools import reduce
from collections import defaultdict

def import_data(filename):
  with open(filename) as file:
    lines = file.read().splitlines()
    robots = []
    for line in lines:
      coords = []
      for segment in line.split(" "):
        eq_idx = segment.find("=")
        com_idx = segment.find(",")
        coords.append((int(segment[eq_idx + 1:com_idx]), int(segment[com_idx + 1:])))
      robots.append(coords)
    return robots

def write_iterations_to_file(robots, ticks, max_height, max_width):
  current_min = (-1, sys.maxsize)
  file1 = open("output.txt", "w")  # append mode
  for i in range(ticks):
    safety = find_safety_factor_after_n(robots, i, max_height, max_width)
    if safety < current_min[1]:
      print(current_min)
      current_min = (i, safety)
    file1.write(f"Position after {i} ticks\n")
    new_locations = defaultdict(int)
    for robot in robots:
      new_locations[location_after_ticks(robot, i, max_height, max_width)] = 1
    for y in range(max_height):
      for x in range(max_width):
        if new_locations[(x,y)] == 1:
          file1.write("X")
        else:
          file1.write(" ")
      file1.write("\n")
    file1.write("\n\n\n\n")
  file1.close()
  return current_min[0]

def find_safety_factor_after_n(robots, ticks, max_height, max_width):
  quadrants = [0,0,0,0]
  for robot in robots:
    new_loc = location_after_ticks(robot, ticks, max_height, max_width)
    if new_loc[0] > max_width//2:
      if new_loc[1] > max_height//2:
        quadrants[3] += 1
      elif new_loc[1] < max_height//2:
        quadrants[2] += 1
    elif new_loc[0] < max_width//2:
      if new_loc[1] > max_height//2:
        quadrants[1] += 1
      elif new_loc[1] < max_height//2:
        quadrants[0] += 1  
  return reduce(lambda x,y: x*y, quadrants)

def location_after_ticks(robot, t, max_height, max_width):
  return ((robot[0][0] + robot[1][0] * t) % max_width, (robot[0][1] + robot[1][1] * t) % max_height)

def main():
  real_data = import_data("input.txt")
  print("Part 1(sample): ", find_safety_factor_after_n(import_data("sample.txt"), 100, 7, 11))
  print("Part 1: ", find_safety_factor_after_n(real_data, 100, 103, 101))
  print("Part 2 see output file at iteration: ", write_iterations_to_file(real_data, 10000, 103, 101))
  
main()