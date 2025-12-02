from math import sumprod

from puzzle_input_reader import read_lines

def part1(file):
    line = read_lines(file)[0]
    product_ranges = line.split(",")
    sum_invalid_ids = 0

    for productRange in product_ranges:
        range_start_end = productRange.split("-")

        for product_id in range(int(range_start_end[0]), int(range_start_end[1]) + 1):
            id_str = str(product_id)
            first_half = id_str[0:int(len(id_str) / 2)]
            second_half = id_str[int(len(id_str) / 2): len(id_str)]

            if first_half == second_half:
                sum_invalid_ids += product_id

    return sum_invalid_ids

def part2(file):
    line = read_lines(file)[0]
    product_ranges = line.split(",")
    sum_invalid_ids = 0

    for productRange in product_ranges:
        range_start_end = productRange.split("-")

        for product_id in range(int(range_start_end[0]), int(range_start_end[1]) + 1):
            product_id_str = str(product_id)
            for r in range(1, len(product_id_str)):
                split = [(product_id_str[i:i + r]) for i in range(0, len(product_id_str), r)]
                if split.count(split[0]) == len(split):
                    sum_invalid_ids += product_id
                    break

    return sum_invalid_ids

if __name__ == '__main__':
    print(f'Solution to part 1 (test input): {part1('test_input/day02_test_input.txt')}')
    print(f'Solution to part 1 (real input): {part1('day02_input.txt')}')

    print(f'Solution to part 2 (test input): {part2('test_input/day02_test_input.txt')}')
    print(f'Solution to part 2 (real input): {part2('day02_input.txt')}')