# https://adventofcode.com/2022/day/13
import time
import math
import re
import numpy as np

day = "13"
start_time = time.time()
inputs = ""


def convert_test_input(case):
  global inputs
  with open(case) as f:
    for line in f.readlines():
      inputs += line
  inputs = inputs.splitlines()

  [inputs.remove(i) for i in inputs if i == '']
  for i in range(len(inputs)):
    inputs[i] = eval(inputs[i])
    print(inputs[i], len(inputs[i]))

  print("INPUTS:", inputs, "\nGROUPS:", int(len(inputs) / 2))


def solution():
  def get_elements_of_nested_list(element):
    count = 0
    if isinstance(element, list):

      for each_element in element:
        count += get_elements_of_nested_list(each_element)
    else:
      count += 1
    return count

  sum_of_groups = 0
  groups = int(len(inputs) / 2)
  for i in range(1, len(inputs), 2):
    # right side needs to be bigger than left
    left = inputs[i - 1]
    right = inputs[i]
    print("LEFT:", left, get_elements_of_nested_list(left))
    print("RIGHT", right, get_elements_of_nested_list(right))

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
