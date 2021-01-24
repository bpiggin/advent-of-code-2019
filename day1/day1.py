from math import floor

f = open("input.txt", "r")
f_input = [int(x) for x in f.read().split("\n")]


def calculate_fuel(mass):
    return floor(mass / 3) - 2


def part_one():
    return sum(calculate_fuel(mass) for mass in f_input)


# -----------------------------------------------------------------


def accumulate_fuel(cur, acc):
    fuel = calculate_fuel(cur)
    if fuel <= 0:
        return acc

    return accumulate_fuel(fuel, acc + fuel)


def part_two():
    return sum(accumulate_fuel(mass, 0) for mass in f_input)


if __name__ == "__main__":
    # print(part_one())
    print(part_two())
