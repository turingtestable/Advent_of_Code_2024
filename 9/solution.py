def import_data():
  with open("input.txt") as file:
    return file.read().splitlines()[0]

def build_file(diskmap):
  file = []
  write_char = ""
  for index in range(len(diskmap)):
    if index %2 == 0:
      write_char = index//2
    else:
      write_char = "."
    for j in range(int(diskmap[index])):
      file.append(write_char)
  return file

def build_compacted_file(file):
  front = 0 
  back = len(file) - 1
  while front < back:
    if file[front] != ".":
      front += 1
    elif file[back] == ".":
      back -= 1
    else:
      switch(file, front, back)
  return file

def build_smarter_compacted_file(file):
  back = len(file) - 1
  while(file[back] != 0):
    if file[back] == ".":
      back -= 1
    else:
      start_back = file.index(file[back])
      file_size = len(file[start_back:back+1])
      index_of_space = find_space(file, file_size, start_back)
      if index_of_space >= 0:
        print("Back: ", file[back] )
        switch_chunks(file, index_of_space, index_of_space + file_size, back, start_back)
      back = start_back - 1
  return file

def find_space(file, space_length, start_back):
  for i in range(start_back):
    if file[i] == ".":
      j = 0
      while j < space_length:
        if i+j< len(file) and file[i+j] == ".":
          j += 1
        else:
          break
      if len(file[i:i+j]) == space_length:
        return i
  return -1
        


def switch_chunks(file, front, end_front, back, start_back):
  hold_slice = file[front:end_front + 1]
  back_slice = file[start_back:back + 1]
  file[front:front+len(back_slice)] = back_slice
  file[start_back:back+1] = hold_slice[:len(back_slice)]

def calc_checksum(file):
  checksum = 0 
  for i in range(len(file)):
    if file[i] != ".":
      checksum += i * int(file[i])
  return checksum

def switch(file, index1, index2):
  hold = file[index1]
  file[index1] = file[index2]
  file[index2] = hold
    

def main():
  file = build_file(import_data())
  new_file = file.copy()
  print("Part 1: ",calc_checksum(build_compacted_file(file)))
  print("Part 2: ", calc_checksum(build_smarter_compacted_file(new_file)))
  

main()