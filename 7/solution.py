file1 = open("MyFile.txt", "w")
def import_data():
  with open("input.txt") as file:
    lines = file.read().splitlines()
    return list(map(process_line, lines))

def process_line(line):
  equation = line.split(": ")
  elements = list(map(int, equation[1].split(' ')))
  answers = [int(equation[0])]
  answers.append(elements)
  return answers

def sum_calibration_results(equations):
  sum_calibrations = 0
  sum_concatenation = 0
  for equation in equations:
    file1.write(f'Trying: {equation[0]}: {equation[1]}|\n')
    if try_operations(equation[0], equation[1]):
      sum_calibrations += equation[0]
    elif try_operations_concat(equation[0], equation[1]):
      sum_concatenation += equation[0]
    else:
      file1.write(f'|Failed: {equation[0]}: {equation[1]}|\n')
  print("Part 1: ", sum_calibrations)
  return sum_concatenation + sum_calibrations

def try_multiply(target, elements):
  return try_operations_concat(target/elements[-1], elements[:-1])

def try_add(target, elements):
  return try_operations_concat(target - elements[-1], elements[:-1])

def try_operations(target, elements):
  if int(target)!= target or target < 0 or len(elements) == 0 :
    return False
  elif target == sum(elements):
    return True
  attempt = try_operations(target - elements[-1], elements[:-1]) or \
    try_operations(target/elements[-1], elements[:-1]) or \
    try_operations(target - elements[-1], elements[:-1])
  if attempt:
    file1.write(f"\tWorked: {target}, Elements: {elements}\n")
  return attempt

def try_operations_concat(target, elements):
  if int(target)!= target or target < 0 or len(elements) == 0 :
    return False
  if target == sum(elements):
    return True
  attempt = try_multiply(target, elements) or try_add(target, elements) or try_concat(target, elements)
  if attempt:
    file1.write(f"\tWorked: {target}, Elements: {elements}\n")
  return attempt

def try_concat(target, elements):
  last_element = str(elements[-1])
  target_string = str(int(target))
  if len(target_string) < len(last_element) or target_string[-len(last_element):] != last_element:
    return False
  possible_target = target_string[:-len(last_element)]
  if possible_target == "":
    if len(elements[:-1]) == 0 :
      return True
    else:
      return False
  else:
    return try_operations_concat(int(possible_target), elements[:-1])


def main():
  print("Part 2: ",sum_calibration_results(import_data()))

main()
