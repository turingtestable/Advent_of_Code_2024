def importData():
  with open("input.txt") as file:
    lines_array = file.read().splitlines()
  return lines_array

def is_safe_report(line_arr):
  print(line_arr)
  if (int(line_arr[0]) < int(line_arr[1])):
    increasing = True
  else:
    increasing = False 
  pos = 0
  while pos < len(line_arr) - 1:
    first,second = int(line_arr[pos]),int(line_arr[pos + 1])
    if increasing and (first >= second or second - first > 3):
      return False
    elif not increasing and (first <= second or first - second > 3):
      return False
    pos +=1
  print("Success")
  return True

def is_safe_report_dampened(line_arr):
  if (int(line_arr[0]) < int(line_arr[1])):
    increasing = True
  else:
    increasing = False 
  pos = 0
  while pos < len(line_arr) - 1:
    first,second = int(line_arr[pos]),int(line_arr[pos + 1])
    if increasing and (first >= second or second - first > 3):
      return is_safe_report(line_arr[:pos+1] + line_arr[pos+2:]) or is_safe_report(line_arr[:pos] + line_arr[pos+1:]) or is_safe_report(line_arr[:pos - 1] + line_arr[pos:])
    elif not increasing and (first <= second or first - second > 3):
      return is_safe_report(line_arr[:pos+1] + line_arr[pos+2:] ) or is_safe_report(line_arr[:pos] + line_arr[pos+1:]) or is_safe_report(line_arr[:pos - 1] + line_arr[pos:])
    pos +=1
  return True

def count_safe_reports(lines):
  safe_reports = 0
  for line in lines:
    if is_safe_report(line.split()):
      safe_reports += 1
  return safe_reports

def count_safe_reports_with_dampener(lines):
  safe_reports = 0
  for line in lines:
    if is_safe_report_dampened(line.split()):
      safe_reports += 1
  return safe_reports


def main():
  print("Number of safe reports:")
  print(count_safe_reports(importData()))
  print("-------------------------------------------------------------------------------")
  print("Number of safe reports with Dampener")
  print(count_safe_reports_with_dampener(importData()))

main()