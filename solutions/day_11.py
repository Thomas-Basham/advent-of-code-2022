# https://adventofcode.com/2022/day/11
import time
import math
import re

day = "11"
inputs = ""
total_cycles = 0
start_time = time.time()
monkeys = []


def convert_test_input(case):
  global inputs
  global monkeys
  with open(case) as f:
    for line in f.readlines():
      inputs += line
  inputs = inputs.splitlines()
  # print("INPUTS:", inputs)
  monkeys = [inputs[i:i + 6] for i in range(0, len(inputs), 7)]
  for m in monkeys:
    m[1] = list(map(int, re.findall(r'[0-9]+', m[1])))
    m[2] = m[2].strip("  Operation: new ").strip('= ')
    m.append(0)
    del m[0]
  print(monkeys)


def solution():
  # global throw_to, operation, commands
  for _ in range(20):
    for monkey in monkeys:
      worry_levels = monkey[0]
      thrown_counter = len(worry_levels)

      for num in worry_levels:
        if '*' in monkey[1]:
          commands = monkey[1].split('* ')

          for c in range(len(commands)):
            if commands[c] == 'old ' or commands[c] == 'old':
              commands[c] = num
          operation = commands[0] * commands[1]

        if '+' in monkey[1]:
          commands = monkey[1].split('+ ')

          for c in range(len(commands)):
            if commands[c] == 'old ' or commands[c] == 'old':
              commands[c] = num

          operation = commands[0] + commands[1]

        operation = operation / 3

        test_amnt = int(re.findall(r'[0-9]+', monkey[2])[0])
        test = math.floor(operation) % test_amnt == 0

        if test == True:
          throw_to = int(re.findall(r'[0-9]+', monkey[3])[0])
        if test == False:
          throw_to = int(re.findall(r'[0-9]+', monkey[4])[0])

        monkeys[throw_to][0].append(str(math.floor(operation)))

      monkey[-1] += thrown_counter
      for i in range(thrown_counter):
        monkey[0].pop(0)

  inspection_count_list = sorted([i[-1] for i in monkeys])
  monkey_business = inspection_count_list[-1] * inspection_count_list[-2]

  end_time = time.time()
  print(f"It took {end_time - start_time:.2f} seconds to compute")

  print(monkey_business)
  return monkey_business


def solution_part_2():
  # global throw_to, operation, commands
  global operation, throw_to
  for i in range(1000):
    for monkey in monkeys:
      worry_levels = monkey[0]
      thrown_counter = len(worry_levels)

      # while thrown_counter > 0
      for num in worry_levels:

        if '*' in monkey[1]:
          commands = monkey[1].split('* ')
          for c in range(len(commands)):
            if commands[c] == 'old ' or commands[c] == 'old':
              commands[c] = num
          operation = math.floor(int(commands[0]) * int(commands[1]))

        if '+' in monkey[1]:
          commands = monkey[1].split('+ ')
          for c in range(len(commands)):
            if commands[c] == 'old ' or commands[c] == 'old':
              commands[c] = num
          operation = math.floor(int(commands[0]) + int(commands[1]))

        test_amnt = int(re.findall(r'[0-9]+', monkey[2])[0])
        test = operation % test_amnt == 0

        if test == True:
          throw_to = int(re.findall(r'[0-9]+', monkey[3])[0])
        if test == False:
          throw_to = int(re.findall(r'[0-9]+', monkey[4])[0])

        # operation = operation / 3 # NEED TO FIGURE OUT HOW TO WORK THIS BACK IN
        monkeys[throw_to][0].append(operation)

      monkey[-1] += thrown_counter
      # for _ in range(thrown_counter):
      #   monkey[0].pop(0)

      [monkey[0].pop(0) for _ in range(thrown_counter)]
    print(i)

  # print(monkeys)
  inspection_count_list = sorted([i[-1] for i in monkeys])
  monkey_business = inspection_count_list[-1] * inspection_count_list[-2]
  end_time = time.time()
  print(f"It took {end_time - start_time:.2f} seconds to compute")

  print(monkey_business)
  return monkey_business


if __name__ == '__main__':
  # test input
  # convert_test_input(f'inputs/day_{day}_test.txt')

  ## challenge input
  convert_test_input(f'inputs/day_{day}.txt')

  # solution()
  solution_part_2()
