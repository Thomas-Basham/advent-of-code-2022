# https://adventofcode.com/2022/day/1
import time

day = "6"
input = ""
start_time = time.time()


def convert_test_input(case):
  global input
  with open(case) as f:
    for line in f.read():
      input += line

  print(input)


def solution():
  temp_list = []
  indexes_list = []
  for index, char in enumerate(input):
    # temp_list.append((index, char))
    temp_list.append(char)
    indexes_list.append(index)
    while len(temp_list) == 4:
      if len(temp_list) == len(set(temp_list)):  # if no duplicates
        print("index is", indexes_list[-1] + 1, )
        print(temp_list)
        break
      if len(temp_list) != len(set(temp_list)):  # if duplicates
        temp_list.pop(0)
        indexes_list.pop(0)

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
