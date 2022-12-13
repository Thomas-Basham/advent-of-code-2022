# https://adventofcode.com/2022/day/12
import time
import math
import re
import numpy as np

day = "12"
start_time = time.time()
inputs = ""


def convert_test_input(case):
  global inputs
  global monkeys
  with open(case) as f:
    for line in f.readlines():
      inputs += line
  inputs = inputs.splitlines()
  inputs = list(map(list, inputs))
  for string in inputs:
    for char in range(len(string)):
      if string[char].islower():
        string[char] = ord(string[char]) - 96
  for i in inputs:
    print("INPUTS:", i)


def solution():
  elevation = 1
  current = []
  for i in range(len(inputs)):
    for j in range(len(inputs[i])):
      if inputs[i][j] == "S":
        current = [i, j + 1]

  while elevation < 3:
    # inputs[current[0]][current[1]] # current point
    if current[1] < len(inputs[0]) - 1:
      if int(inputs[current[0]][current[1] + 1]) <= int(inputs[current[0]][current[1]]):
        print(current)
        current[1] += 1

      if inputs[current[0]][current[1] + 1] == elevation + 1:
        print(current)
        elevation += 1
        current[1] += 1
    if current[0] < len(inputs):
      if int(inputs[current[0]][current[1] + 1]) > int(inputs[current[0]][current[1]]):
        print(current)
        current[0] += 1

  end_time = time.time()
  print(f"It took {end_time - start_time:.2f} seconds to compute")


def solution_part_2():
  end_time = time.time()
  print(f"It took {end_time - start_time:.2f} seconds to compute")


if __name__ == '__main__':
  # test input
  convert_test_input(f'inputs/day_{day}_test.txt')

  ## challenge input
  # convert_test_input(f'inputs/day_{day}.txt')

  solution()
  # solution_part_2()
