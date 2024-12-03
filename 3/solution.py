#mul\([0-9]+,[0-9]+\)
import re

def import_data():
  with open("input.txt") as file:
    return "".join(file.read().splitlines())

def sum_multiply_commands(file):
  commands = re.findall("mul\([0-9]+,[0-9]+\)", file)
  sum = 0
  for command in commands:
    sum += value_mul_command(command)
  return sum


def value_mul_command(command):
  numbers = command[4:-1].split(",")
  return int(numbers[0]) * int(numbers[1])

def remove_dont(file):
  altered_file = file
  while altered_file.find("don't()") > -1:
    dont_index = altered_file.find("don't()")
    dont_fragment = altered_file[dont_index:]
    do_index = dont_fragment.find("do()")
    if do_index > -1:
      dont_fragment = dont_fragment[:do_index + 4]
      altered_file = altered_file.replace(dont_fragment, "")
    else:
      altered_file = altered_file.replace(dont_fragment, "")
  return sum_multiply_commands(altered_file)
    

  altered_file = re.sub("don't\(\).*do\(\)", "", file)
  print(altered_file)
  return sum_multiply_commands(altered_file)

def main():
  print(sum_multiply_commands(import_data()))
  print(remove_dont(import_data()))

main()