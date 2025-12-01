from puzzle_input_reader import read_lines

def part1(file):
    lines = read_lines(file)

    current_wheel_pos = 50
    number_of_times_hit_zero = 0

    for line in lines:
        direction = line[0]
        amount = int(line[1:])

        current_wheel_pos = current_wheel_pos - amount if direction == 'L' else current_wheel_pos + amount

        if current_wheel_pos % 100 == 0:
            number_of_times_hit_zero += 1

    return number_of_times_hit_zero

def part2(file):
    lines = read_lines(file)

    current_wheel_pos = 50
    number_of_times_hit_zero = 0

    for line in lines:
        direction = line[0]
        amount = int(line[1:])

        for x in range(amount):
            current_wheel_pos = current_wheel_pos - 1 if direction == 'L' else current_wheel_pos + 1

            if current_wheel_pos % 100 == 0:
                number_of_times_hit_zero += 1

    return number_of_times_hit_zero

if __name__ == '__main__':
    print(f'Solution to part 1 (test input): {part1('test_input/day01_test_input.txt')}')
    print(f'Solution to part 1 (real input): {part1('day01_input.txt')}')

    print(f'Solution to part 2 (test input): {part2('test_input/day01_test_input.txt')}')
    print(f'Solution to part 2 (real input): {part2('day01_input.txt')}')