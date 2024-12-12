import math
from collections import defaultdict

max_i = 0
max_j = 0
visited = set()

def import_data(filename):
  with open(filename) as file:
    lines = file.read().splitlines()
  letter_dict = {}
  global max_i
  global max_j
  max_i = len(lines)
  max_j = len(lines[0])
  for i in range(len(lines)):
    for c in range(len(lines[i])):
      letter_dict[(i,c)]=lines[i][c]
  return letter_dict

def sum_regions(crop_dict):
  total_price = 0
  discount_total_price = 0 
  regions = define_regions(crop_dict)
  for region in regions:
    total_price += calculate_fence_price(region, crop_dict)
    discount_total_price += calculate_discount_price(region, crop_dict)
  print("Part 1: ", total_price)
  return discount_total_price

def calculate_discount_price(region, crop_dict):
  num_sides = 0
  edge_dict = defaultdict(set)
  area = len(region)
  for loc in region:
    #Left Edge
    above = (loc[0] - 1, loc[1])
    left = (loc[0], loc[1] - 1)
    below = (loc[0] + 1, loc[1])
    right = (loc[0], loc[1] + 1)
    if above not in crop_dict or crop_dict[loc] != crop_dict[above]:
      edge_dict["A"].add(loc)
    if left not in crop_dict or crop_dict[loc] != crop_dict[left]:
      edge_dict["L"].add(loc)
    if below not in crop_dict or crop_dict[loc] != crop_dict[below]:
      edge_dict["B"].add(loc)
    if right not in crop_dict or crop_dict[loc] != crop_dict[right]:
      edge_dict["R"].add(loc)
  for loc in edge_dict["A"]:
    if (loc[0], loc[1]-1) not in edge_dict["A"]:
      num_sides += 1
  for loc in edge_dict["L"]:
    if (loc[0] + 1, loc[1]) not in edge_dict["L"]:
      num_sides += 1
  for loc in edge_dict["B"]:
    if (loc[0], loc[1]-1) not in edge_dict["B"]:
      num_sides += 1
  for loc in edge_dict["R"]:
    if (loc[0] + 1, loc[1]) not in edge_dict["R"]:
      num_sides += 1
  #print(f"{crop_dict[region[0]]} has area: {area}  and number of sides: {num_sides}")
  return num_sides * area


def calculate_fence_price(region, crop_dict):
  perimeter = 0
  area = len(region)
  for loc in region:
    potential_locs = [(loc[0]-1, loc[1]), (loc[0], loc[1]-1), (loc[0]+1, loc[1]), (loc[0], loc[1]+1)]
    for p_loc in potential_locs:
      if p_loc not in crop_dict or crop_dict[loc] != crop_dict[p_loc]:
            perimeter += 1
  #print(f"{crop_dict[region[0]]} has perimeter: {perimeter} and area: {area}")
  return perimeter * area

def define_regions(crop_dict):
  length = int(math.sqrt(len(crop_dict.keys())))
  regions = []
  global visited
  visited = set()
  for i in range(length):
    for j in range(length):
      if (i,j) not in visited:
        new_region = navigate_region(crop_dict, (i,j), length, [])
        regions.append(new_region)
  return regions
  
def navigate_region(crop_dict, loc, length, cur_region):
  global visited
  visited.add(loc)
  cur_region.append(loc)
  potential_locs = [(loc[0]-1, loc[1]), (loc[0], loc[1]-1), (loc[0]+1, loc[1]), (loc[0], loc[1]+1)]
  for p_loc in potential_locs:
    if p_loc not in visited and \
        p_loc in crop_dict and \
        crop_dict[loc] == crop_dict[p_loc]:
      navigate_region(crop_dict, p_loc, length, cur_region)
  return cur_region

def main():
  print("Part 2 (sample): ", sum_regions(import_data("sample.txt")))
  print("Part 2: ", sum_regions(import_data("input.txt")))

main()
