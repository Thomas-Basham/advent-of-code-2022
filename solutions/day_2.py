# https://adventofcode.com/2022/day/1
import time

start_time = time.time()

day = "2"
inputs = ""


def convert_test_input(case):
  global inputs
  with open(case) as f:
    for char in f.read():
      if char != ' ':

        if char == 'A' or char == 'X':
          inputs += "1"

        if char == 'B' or char == 'Y':
          inputs += "2"

        if char == 'C' or char == 'Z':
          inputs += "3"

        if char == '\n':
          inputs += char

        # inputs += char
    inputs = inputs.splitlines()
    # print(inputs)


def solution():
  score = 0

  for i in inputs:
    opponent = i[0]
    me = i[1]
    if opponent == "1":
      if me == "3":
        score += int(me)  # lose
      if me == "2":
        score += 6 + int(me)  # win
      if me == "1":
        score += 3 + int(me)  # lose

    if opponent == "2":
      if me == "3":
        score += 6 + int(me)  # win
      if me == "2":
        score += 3 + int(me)
      if me == "1":
        score += int(me)  # lose

    if opponent == "3":
      if me == "3":
        score += 3 + int(me)
      if me == "2":
        score += int(me)  # lose
      if me == "1":
        score += 6 + int(me)  # win

  print("Score Part 1", score)

  end_time = time.time()

  print(f"It took {end_time - start_time:.2f} seconds to compute")


def solution_part_2():
  score = 0

  for i in inputs:
    opponent = i[0]
    me = i[1]
    if me == '1':  # lose
      if opponent == "1":
        score += 3

      if opponent == "2":
        score += 1

      if opponent == "3":
        score += 2

    if me == '2':  # draw
      score += int(opponent) + 3

    if me == '3':  # win
      if opponent == "1":
        score += 6 + 2

      if opponent == "2":
        score += 6 + 3

      if opponent == "3":
        score += 6 + 1
  print("Score Part 2", score)

  end_time = time.time()

  print(f"It took {end_time - start_time:.2f} seconds to compute")


if __name__ == '__main__':
  ## test input
  # convert_test_input(f'inputs/day_{day}_test.txt')

  # challenge input
  convert_test_input(f'inputs/day_{day}.txt')

  solution()
  solution_part_2()
