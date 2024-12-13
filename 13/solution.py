import sys
def import_data(filename):
  with open(filename) as file:
    lines = file.read().splitlines()
  games = []
  new_game = []
  for i in range(len(lines)):
    if i%4 == 0:
      new_game = [lines[i]]
    elif i%4 != 3:
      new_game.append(lines[i])
    else:
      games.append(new_game)
  games.append(new_game)
  return games

def cost_winnable_prizes(games, adjusted):
  total_cost = 0
  counter = 1
  for game in games:
    if adjusted:
      total_cost += find_cheapest_adjusted_game_value(game)
    else:
      total_cost += find_cheapest_game_value(game)
    counter += 1
  return total_cost

def find_xy(button_string):
  a_x_idx = button_string.find("X")
  a_y_idx = button_string.find("Y")
  a_c_idx = button_string.find(",")
  return (int(button_string[a_x_idx + 2:a_c_idx]), int(button_string[a_y_idx+2:]))

def calc_pos(but_a, but_b, push_a, push_b):
  return (but_a[0]*push_a + but_b[0]*push_b, but_a[1]*push_a + but_b[1]*push_b)

def find_cheapest_game_value(game):
  cheapest_game_value = 401
  button_a = find_xy(game[0])
  button_b = find_xy(game[1])
  target = find_xy(game[2])
  for pushes_a in range(101):
    for pushes_b in range(101):
      if calc_pos(button_a, button_b, pushes_a, pushes_b) == target:
        cheapest_game_value = min(cheapest_game_value, pushes_a * 3 + pushes_b)
  if cheapest_game_value == 401:
    return 0
  return cheapest_game_value

def find_cheapest_adjusted_game_value(game):
  pushes = solve_system(game)
  print("\n")
  return pushes[0]*3 + pushes[1]

def solve_system(game):
  print("Game: ", game)
  button_a = find_xy(game[0])
  button_b = find_xy(game[1])
  target = find_xy(game[2])
  target = (target[0] + 10000000000000, target[1] + 10000000000000)
  pushes_a = solve(button_a, button_b, target)
  if int(pushes_a) != pushes_a:
    print("Lose")
    return (0,0)
  else:
    print("Win")
    pushes_b = (target[0] - pushes_a * button_a[0])/button_b[0]
    return (int(pushes_a), int(pushes_b))

def solve(but_a, but_b, target):
  new_a = -but_a[0] * but_b[1] + but_b[0] * but_a[1]
  new_target = -target[0] * but_b[1] + target[1]*but_b[0]
  return new_target/new_a

def main():
  print("Part 1 (sample): ", cost_winnable_prizes(import_data("sample.txt"), False))
  print("Part 1: ", cost_winnable_prizes(import_data("input.txt"), False))
  print("Part 2 (sample): ", cost_winnable_prizes(import_data("sample.txt"), True))
  print("Part 2: ", cost_winnable_prizes(import_data("input.txt"), True))

main() 