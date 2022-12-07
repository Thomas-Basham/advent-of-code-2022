# https://adventofcode.com/2022/day/1
import time

day = "4"
input = ""
start_time = time.time()


def convert_test_input(case):
  global input
  with open(case) as f:
    for line in f.read():
      input += line
  input = input.splitlines()

  for i in range(len(input)):
    input[i] = input[i].split(',')
    for j in range(len(input[i])):
      input[i][j] = input[i][j].split('-')
      for k in range(len(input[i][j])):
        input[i][j][k] = int(input[i][j][k])
  print(input)


def solution():
  pairs = 0
  for i in input:
    range_1_list = [i for i in range(min(i[0]), max(i[0]) + 1)]
    range_2_list = [i for i in range(min(i[1]), max(i[1]) + 1)]

    print(range_1_list)
    if all(elem in range_1_list for elem in range_2_list) or all(elem in range_2_list for elem in range_1_list):
      pairs += 1

  print("PAIRS:", pairs)
  end_time = time.time()
  print(f"It took {end_time - start_time:.2f} seconds to compute")


def solution_part_2():
  pairs = 0
  for i in input:
    range_1_list = [i for i in range(min(i[0]), max(i[0]) + 1)]
    range_2_list = [i for i in range(min(i[1]), max(i[1]) + 1)]

    print(range_1_list)
    if any(elem in range_1_list for elem in range_2_list) or any(elem in range_2_list for elem in range_1_list):
      pairs += 1

  print("PAIRS:", pairs)
  end_time = time.time()
  print(f"It took {end_time - start_time:.2f} seconds to compute")



  end_time = time.time()
  print(f"It took {end_time - start_time:.2f} seconds to compute")


if __name__ == '__main__':
  ## test input
  # convert_test_input(f'inputs/day_{day}_test.txt')

  ## challenge input
  convert_test_input(f'inputs/day_{day}.txt')

  solution()
  solution_part_2()
