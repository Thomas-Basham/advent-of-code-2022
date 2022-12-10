# https://adventofcode.com/2022/day/10
import time
import numpy as np

day = "10"
inputs = ""

start_time = time.time()


def convert_test_input(case):
  global inputs
  with open(case) as f:
    for line in f.readlines():
      inputs += line
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
  end_time = time.time()
  print(f"It took {end_time - start_time:.2f} seconds to compute")


if __name__ == '__main__':
  # test input
  # convert_test_input(f'inputs/day_{day}_test.txt')

  ## challenge input
  convert_test_input(f'inputs/day_{day}.txt')

  solution()
  # solution_part_2()
