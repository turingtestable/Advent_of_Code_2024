from collections import defaultdict

max_i = 0
max_j = 0 

def import_data():
  with open("input.txt") as file:
    return file.read().splitlines()

def find_nodes(lines):
  letter_dict = defaultdict(list)
  global max_i
  global max_j
  max_i = len(lines)
  max_j = len(lines[0])
  for i in range(len(lines)):
    for c in range(len(lines[i])):
      if lines[i][c] != ".":
        letter_dict[lines[i][c]].append((i,c))
  return letter_dict

def sum_anti_nodes(node_dict):
  anti_nodes = set()
  keys = node_dict.keys()
  for key in keys:
    anti_nodes.update(find_anti_nodes(node_dict[key]))
  return len(anti_nodes)

def find_anti_nodes(antenna_locations):
  anti_nodes = set()
  for antenna in antenna_locations:
    for antenna2 in antenna_locations:
      if antenna != antenna2:
        candidate_anti_node = (antenna[0] + antenna[0] - antenna2[0], antenna[1] + antenna[1] - antenna2[1])
        if in_map(candidate_anti_node):
          anti_nodes.add(candidate_anti_node)
  return anti_nodes

def sum_harmonic_anti_nodes(node_dict):
  anti_nodes = set()
  for value in node_dict.values():
    anti_nodes.update(find_harmonic_anti_nodes(value))
  return len(anti_nodes)

def find_harmonic_anti_nodes(antenna_locations):
  anti_nodes = set()
  for antenna in antenna_locations:
    for antenna2 in antenna_locations:
      if antenna != antenna2:
        prev_node = antenna
        while in_map(prev_node):
          anti_nodes.add(prev_node)
          prev_node = (prev_node[0] + antenna[0] - antenna2[0], prev_node[1] + antenna[1] - antenna2[1])
  return anti_nodes
        
def in_map(node):
  if node[0] < 0 or node[0] >= max_i or node[1] < 0 or node[1] >= max_j:
    return False
  return True

def main():
  nodes = find_nodes(import_data())
  print("part 1: ", sum_anti_nodes(nodes))
  print("part 2: ", sum_harmonic_anti_nodes(nodes))

main()