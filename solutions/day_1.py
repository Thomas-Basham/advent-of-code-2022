# https://adventofcode.com/2022/day/1
import time

day = "1"
inputs = ""
start_time = time.time()


def convert_test_input(case):
  global inputs
  with open(case) as f:
    for line in f.read():
      inputs += line
    inputs = inputs.splitlines()
    # inputs = list(map(int, inputs))
    # print(inputs)


def solution():
  elves = []
  cal_sum = 0

  for elf in inputs:
    if elf != '':
      cal_sum += int(elf)
    if elf == '':
      elves.append(cal_sum)
      cal_sum = 0

  end_time = time.time()

  print("PART 1:", max(elves))
  print(f"It took {end_time - start_time:.2f} seconds to compute")

  return max(elves)


def solution_part_2():
  elves = []
  cal_sum = 0

  for elf in inputs:
    if elf != '':
      cal_sum += int(elf)
    if elf == '':
      elves.append(cal_sum)
      cal_sum = 0

  elves = sorted(elves, reverse=True)

  end_time = time.time()

  print("PART 2:", sum([elves[0], elves[1], elves[2]]))
  print(f"It took {end_time - start_time:.2f} seconds to compute")

  return sum([elves[0], elves[1], elves[2]])


if __name__ == '__main__':
  ## test input
  # convert_test_input(f'inputs/day_{day}_test.txt')

  ## challenge input
  convert_test_input(f'inputs/day_{day}.txt')

  solution()
  solution_part_2()

