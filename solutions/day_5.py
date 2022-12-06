# https://adventofcode.com/2022/day/5
import time

start_time = time.time()

day = "5"
inputs = ""
directions = []
arrays = []


def convert_test_input(case):
  global inputs
  global directions

  with open(case) as f:
    for char in f.read():
      # if char != "[" and char != "]":  # char != ' ' and
      inputs += char

    # inputs += char
    inputs = inputs.splitlines()

    # get the
    splitted = [i.split() for i in inputs]
    for index, i in enumerate(splitted):
      if all(j.isdigit() for j in i) and len(i) > 0:

        arr_ammount = max(list(map(int, i)))
        directions = inputs[index + 2:]
        inputs = inputs[:index]
        for _ in range(arr_ammount):
          arrays.append([])

    for index, row in enumerate(inputs):
      len_row = len(row)
      # print(len_row) # 11
      new_arr = []
      # if row[1].isalpha():
      #   arrays[0].append(row[1])

      for i in range(1, len_row, 4):
        # print(row[i], i)
        new_arr.append(row[i])

      inputs[index] = new_arr
    # print("inputs after", inputs)

    for index, row in enumerate(inputs):
      for i in range(len(row)):
        if row[i] != ' ':
          arrays[i].append(row[i])

    for i in range(len(directions)):
      new_arr = []
      for j in directions[i]:
        if j.isdigit():
          new_arr.append(j)
      directions[i] = new_arr
    print("arrays:", arrays)
    print("directions:", directions)


def solution():
  final_message = ''

  for index, i in enumerate(directions):
    amount = int(i[0])
    from_arr = int(i[1]) - 1
    to_arr = int(i[2]) - 1
    from_len = len(arrays[from_arr])
    print('arrays after LINE:', index + 11, i, arrays)

    for _ in range(amount):
      arrays[to_arr].append(arrays[from_arr].pop(0))

  for i in arrays:
    if len(i) > 0:
      final_message += i[-1]
    else:
      final_message += ' '

  print("MESSAGE FROM THE ELVES:", final_message)

  end_time = time.time()

  print(f"It took {end_time - start_time:.2f} seconds to compute")

  return arrays


if __name__ == '__main__':
  ## test input
  # convert_test_input(f'inputs/day_{day}_test.txt')

  # challenge input
  convert_test_input(f'inputs/day_{day}.txt')

  solution()
