# https://adventofcode.com/2022/day/1
import time
import re

day = "8"
inputs = ""
start_time = time.time()


def convert_test_input(case):
  global inputs
  with open(case) as f:
    for line in f.read():
      inputs += line
  inputs = inputs.splitlines()
  print("INPUTS:", inputs)


def solution():
  def CheckForLess(list1, val):

    # traverse in the list
    for x in list1:
      # compare with all the
      if x >= val:
        return False

    return True

  def check_col(col_index, row_index):
    collumn = [inputs[x][col_index] for x in range(len(inputs))]
    print("CHECKING COLLUMN:", collumn)

    # check the top half of collumn
    top_half = collumn[:row_index]
    # check the bottom half of collumn
    bot_half = collumn[row_index + 1:]
    print("top_half, bot_half", top_half, bot_half)

    # print("CHECK TOP:", CheckForLess(top_half, collumn[row_index]))
    # print("CHECK BOTTOM:", CheckForLess(bot_half, collumn[row_index]))

    if CheckForLess(top_half, collumn[row_index]) or CheckForLess(bot_half, collumn[row_index]):
      print("VISIBLE!")
      return True

  def check_row(col_index, row_index):
    row = inputs[row_index]
    print("CHECKING ROW:", row, "MADE FROM col ,row:", col_index, row_index)
    left_half = row[:col_index]
    right_half = row[col_index + 1:]

    if CheckForLess(left_half, row[col_index]) or CheckForLess(right_half, row[col_index]):
      print("ROW VISIBLE")
      return True

  trees_visible = 0

  # DRIVER
  # get the edges
  for index, row in enumerate(inputs):
    if index == 0 or index == len(inputs) - 1:
      for _ in row:
        trees_visible += 1

    else:
      for ind, col in enumerate(row):
        if ind == 0:  # if beginning of row
          trees_visible += 1
        if ind == len(row) - 1:  # if end of row
          trees_visible += 1

      for ind, col in enumerate(row):
        if ind != 0 and ind != len(row) - 1:
          if check_row(ind, index) or check_col(ind, index):  # check up and down
            trees_visible += 1

  print(trees_visible)

  end_time = time.time()
  print(f"It took {end_time - start_time:.2f} seconds to compute")


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
