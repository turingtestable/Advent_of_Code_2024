blink_len = {("0",1):1}
def import_data():
  with open("input.txt") as file:
    return file.read().splitlines()[0].split(" ")

def blink(stones):
  new_stones = []
  for i in range(len(stones)):
    if stones[i] == "0":
      new_stones.append("1")
    elif len(stones[i]) % 2 == 0:
      half = len(stones[i])//2
      new_stones = new_stones + [stones[i][0:half], str(int(stones[i][half:]))]
    else:
      new_stones.append(str(2024 * int(stones[i])))
  return new_stones

def fast_blinks_len(stone, num_blinks):
  global blink_len
  if (num_blinks == 1):
    blink_len[(stone, 1)] = len(blink([stone]))
  elif (stone, num_blinks) not in blink_len:
    new_stones = blink([stone])
    sum_blink_len = 0
    for i in new_stones:
      sum_blink_len += fast_blinks_len(i, num_blinks - 1)
    blink_len[(stone, num_blinks)] = sum_blink_len
  return blink_len[(stone, num_blinks)]  

def main():
  stones = import_data()
  current_total_len = 0 
  ## INITIAL SOLVE FOR PART 1
  # for i in range(25):
  #   stones = blink(stones)
  # print("Part 1: ", len(stones))

  for stone in stones:
    current_total_len += fast_blinks_len(stone, 25)
  print("Part 1: ", current_total_len)

  current_total_len = 0 
  for stone in stones:
    current_total_len += fast_blinks_len(stone, 75)
  print("Part 2: ", current_total_len)

main()
