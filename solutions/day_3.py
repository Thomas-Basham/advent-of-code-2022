# https://adventofcode.com/2022/day/1
import time

day = "3"
input = ""
start_time = time.time()


def convert_test_input(case):
  global input
  with open(case) as f:
    for line in f.read():
      input += line
  input = input.splitlines()
  print(input)


def solution():
  commons = []
  priority_sum = 0
  for i in input:
    temp_list = []
    half = int(len(i) / 2)
    comp_1 = i[0:half]
    comp_2 = i[half::]

    for char in comp_1:
      if char in comp_2:
        temp_list.append(char)
    commons.append(temp_list[0])

  print(commons)

  for i in commons:
    if i.isupper():
      priority_sum += ord(i) - 38
    if i.islower():
      priority_sum += ord(i) - 96

  print(priority_sum)
  end_time = time.time()
  print(f"It took {end_time - start_time:.2f} seconds to compute")


def solution_part_2():
  end_time = time.time()
  print(f"It took {end_time - start_time:.2f} seconds to compute")


if __name__ == '__main__':
  ## test input
  # convert_test_input(f'inputs/day_{day}_test.txt')

  ## challenge input
  convert_test_input(f'inputs/day_{day}.txt')

  solution()
  # solution_part_2()
