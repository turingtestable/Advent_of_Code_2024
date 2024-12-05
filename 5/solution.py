from functools import cmp_to_key

before_dict = {}

def import_data():
  with open("input.txt") as file:
    file_lines = file.read().splitlines()
    split_index = file_lines.index("")
    chunks = [file_lines[:split_index], file_lines[split_index + 1:]]
  return chunks

def build_sort_order(rules_list):
  for rule in rules_list:
    insert(rule,before_dict)

def insert(new_element, dict):
  k,v = new_element.split("|")
  if k in dict:
    dict[k] += [v]
  else:
    dict[k] = [v]


def count_sorted(orders):
  sum_correct = 0
  sum_incorrect = 0
  for line in orders:
    instructions = line.split(",")
    sorted_instructions = sorted(instructions, key=cmp_to_key(custom_sort))
    if instructions == sorted_instructions:
      sum_correct += int(instructions[(len(instructions)//2)])
    else:
      sum_incorrect += int(sorted_instructions[int(len(sorted_instructions)//2)])
  print("Sum correct instructions middle: ", sum_correct)
  print("Sum incorrect instructions middle: ", sum_incorrect)

def custom_sort(key1, key2):
  if key1 in before_dict and key2 in before_dict[key1]:
    return -1
  return 1

def main():
  info = import_data()
  build_sort_order(info[0])
  count_sorted(info[1])


main()
