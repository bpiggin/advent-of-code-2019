f = open("input.txt", "r")
f_input = [int(x) for x in f.read().split(",")]


def run_intcode(code):
    for opcode, i, j, k in zip(*[iter(code)] * 4):
        if opcode == 99:
            return code
        if opcode == 1:
            code[k] = code[i] + code[j]
        if opcode == 2:
            code[k] = code[i] * code[j]
    return code


def part_one():
    result = run_intcode(f_input)
    return result[0]


if __name__ == "__main__":
    print(part_one())
