f = open("input.txt", "r")
f_input_1, f_input_2 = map(lambda x: x.split(","), f.read().split("\n"))

vectors = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


def crawl_wire(wire):
    points = set()
    loc = [0, 0]
    for instruction in wire:
        diff = vectors[instruction[0]]
        for step in range(0, int(instruction[1:])):
            loc[0] = loc[0] + diff[0]
            loc[1] = loc[1] + diff[1]
            points.add(tuple(loc))
    return points


def part_one():
    visited = crawl_wire(f_input_1)
    return min(
        abs(point[0]) + abs(point[1])
        for point in visited.intersection(crawl_wire(f_input_2))
    )


if __name__ == "__main__":
    print(part_one())
