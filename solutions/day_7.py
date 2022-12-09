# https://adventofcode.com/2022/day/1
import time
import re

day = "7"
input = ""
start_time = time.time()


def convert_test_input(case):
  global input
  with open(case) as f:
    for line in f.read():
      input += line
  input = input.splitlines()
  print(input[2:])


def solution():
  sum_dirs = 0
  directories = [['dir /', 0]]
  current_dir = []

  temp_list = []
  res = []
  for i in range(1, len(input)):  # get directories
    if input[i].startswith('dir'):
      temp_list.append(input[i])
      [res.append(x) for x in temp_list if x not in res]

  for t in range(len(res)):
    directories.append([res[t], 0])

  for i in range(1, len(input)):  # get root home files
    if input[i][0].isnumeric():
      num = re.findall(r'[0-9]+', input[i])
      # if int(num[0]) <= 100000:
      directories[0][1] += int(num[0])
    if input[i].startswith('$ cd'):
      break

  for i in range(1, len(input)):
    if input[i].startswith('$ cd') and input[i] != '$ cd ..':  # increase level with cd
      current_dir.append('dir ' + input[i][5:])
      # print("CURRENT DIR:", current_dir)

    if input[i][0].isnumeric():
      num = re.findall(r'[0-9]+', input[i])
      print("CURRENT DIR:", current_dir)
      print("NUM TO ADD", num[0])
      dir_list = [i[0] for i in directories]
      # print("DIR LIST",dir_list)
      for d in current_dir:
        if d in dir_list:
          for dirr in range(len(directories)):
            if directories[dirr][0] == d:
              directories[dirr][1] += int(num[0])
              print(directories[dirr][0], "+=", int(num[0]))

    if input[i] == '$ cd ..':
      current_dir.pop()
      print(input[i])

  for dirr in directories:
    if dirr[1] <= 100000:
      sum_dirs += dirr[1]
  directories[0][1] += sum([i[1] for i in directories[1:]])

  print(directories)
  print(sum_dirs)
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

  # solution()
  # solution_part_2()

# 1243729 is right
# 1152715 too low
#  663061 too low
#  758423
