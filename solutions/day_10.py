# https://adventofcode.com/2022/day/10
import time
import math

day = "10"
inputs = ""
total_cycles = 0
start_time = time.time()


def convert_test_input(case):
  global inputs
  global total_cycles
  with open(case) as f:
    for line in f.readlines():
      inputs += line
      command = line[:4]
      if command.startswith("addx"):
        # print("COMMAND: ", command, ammount)
        total_cycles += 2
      if command.startswith('noop'):
        # print("COMMAND: ", command)
        total_cycles += 1

  print("total_cycles", total_cycles)
  inputs = inputs.splitlines()

  print("INPUTS:", inputs)


def solution():
  signal_strength = 0
  cycle = 1
  x = 1
  for i in inputs:
    command = i[:4]
    amount = i[5:]

    cycle += 1

    if cycle in range(20, cycle + 1, 40):
      signal_strength += (cycle * x)

    if command.startswith("addx"):
      x += int(amount)
      cycle += 1
      if cycle in range(20, cycle + 1, 40):
        signal_strength += (cycle * x)

  end_time = time.time()
  print(f"It took {end_time - start_time:.2f} seconds to compute")

  print(signal_strength)
  return signal_strength


def solution_part_2():
  rows = [["." for _ in range(40)] for _ in range(int(total_cycles / 40))]
  cycle = 0
  x = 0

  for i in inputs:
    command = i[:4]
    amount = i[5:]

    row = math.floor(cycle / 40)
    row_i = cycle - (row * 40)

    if row_i in range(x, x + 3):
      rows[row][row_i] = '#'

    cycle += 1
    row_i += 1

    if command.startswith("addx"):
      if row_i in range(x, x + 3):
        rows[row][row_i] = '#'
      cycle += 1
      row_i += 1

      x += int(amount)

  for i in rows:
    print(i)

  end_time = time.time()
  print(f"It took {end_time - start_time:.2f} seconds to compute")


if __name__ == '__main__':
  # test input
  # convert_test_input(f'inputs/day_{day}_test.txt')

  ## challenge input
  convert_test_input(f'inputs/day_{day}.txt')

  solution()
  solution_part_2()
  # PZULBAUA
