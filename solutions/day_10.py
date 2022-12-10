# https://adventofcode.com/2022/day/9
import time
import numpy as np

day = "9"
inputs = ""
start_time = time.time()
matrix = []


def convert_test_input(case):
  global matrix
  global inputs
  with open(case) as f:
    for line in f.read():
      inputs += line
  inputs = inputs.splitlines()
  # print("INPUTS:", inputs)

  vert_length = 0
  vert_lengths = []
  hori_length = 0
  hori_lengths = []
  for i in inputs:
    if i.startswith('U'):
      vert_length += int(i[2])
      vert_lengths.append(vert_length)
    if i.startswith('D'):
      vert_length -= int(i[2])
      vert_lengths.append(vert_length)

    if i.startswith('R'):
      hori_length += int(i[2])
      hori_lengths.append(hori_length)

    if i.startswith('L'):
      hori_length -= int(i[2])
      hori_lengths.append(hori_length)

  # print(vert_length, hori_length)

  matrix_width = max(hori_lengths) + 1
  matrix_height = max(vert_lengths) + 1
  print(matrix_width, matrix_height)  # matrix is x width by x tall
  print("LENGTHS", hori_length, vert_length)
  for _ in range(matrix_height):
    matrix.append([0 for _ in range(matrix_width)])
  # print(matrix)
  print(np.array(matrix))


def solution():
  for i in range(len(inputs)):
    vert_distance = 0
    hori_distance = 0
    if inputs[i].startswith('U'):
      vert_distance += int(inputs[i][2])
      if vert_distance > 0:

        for v in range(vert_distance):
          print(v + 1, "GREATER")

    if inputs[i].startswith('D'):
      vert_distance -= int(inputs[i][2])
      print(vert_distance)
      if vert_distance < 0:
        for v in range(abs(vert_distance)):
          print(v + 1, "less")

    if inputs[i].startswith('R'):
      pass
    if inputs[i].startswith('L'):
      pass

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
