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


# -----------------------------------------------------------

def part_two(p_input):
    noun, verb = 0, 0
    for i in range(99):
        for j in range(99):
            trial_input = p_input.copy()
            trial_input[1:3] = [i, j]
            output = run_intcode(trial_input)
            if output[0] == 19690720:
                noun, verb = i, j
                break
    return 100 * noun + verb


if __name__ == "__main__":
    # print(part_one())
    print(part_two(f_input))
