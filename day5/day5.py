f = open("input.txt", "r")
f_input = [int(x) for x in f.read().split(",")]


def parse_instruction(instruction):
    mode_1, mode_2 = "0", "0"

    if len(instruction) == 1:
        return (instruction, mode_1, mode_2)

    opcode = instruction[-2:].replace("0", "")
    mode_1 = instruction[-3:-2]
    if len(instruction) == 4:
        mode_2 = "1"

    return (opcode, mode_1, mode_2)


def parse_params(code, opcode, i, mode_1, mode_2):
    par_1, par_2 = None, None
    par_1 = code[i + 1] if mode_1 == "1" else code[code[i + 1]]
    if not opcode == "4":
        par_2 = code[i + 2] if mode_2 == "1" else code[code[i + 2]]
    return (par_1, par_2)


def run_intcode(code, p_input):
    output = 0
    i = 0
    for j in range(len(code)):
        opcode, mode_1, mode_2 = parse_instruction(str(code[i]))

        if opcode == "99":
            break

        if opcode == "1":
            par_1, par_2 = parse_params(code, opcode, i, mode_1, mode_2)
            code[code[i + 3]] = par_1 + par_2
            i += 4

        if opcode == "2":
            par_1, par_2 = parse_params(code, opcode, i, mode_1, mode_2)
            code[code[i + 3]] = par_1 * par_2
            i += 4

        if opcode == "3":
            code[code[i + 1]] = p_input
            i += 2

        if opcode == "4":
            par_1, par_2 = parse_params(code, opcode, i, mode_1, mode_2)
            output = par_1
            print(output)
            i += 2

        if opcode == "5":
            par_1, par_2 = parse_params(code, opcode, i, mode_1, mode_2)
            i = par_2 if not par_1 == 0 else i + 3

        if opcode == "6":
            par_1, par_2 = parse_params(code, opcode, i, mode_1, mode_2)
            i = par_2 if par_1 == 0 else i + 3

        if opcode == "7":
            par_1, par_2 = parse_params(code, opcode, i, mode_1, mode_2)
            code[code[i + 3]] = 1 if par_1 < par_2 else 0
            i += 4

        if opcode == "8":
            par_1, par_2 = parse_params(code, opcode, i, mode_1, mode_2)
            code[code[i + 3]] = 1 if par_1 == par_2 else 0
            i += 4

    return (code, output)


def part_one():
    code, output = run_intcode(f_input, 1)
    return output


# -----------------------------------------------------------


def part_two():
    code, output = run_intcode(f_input, 5)
    return output


if __name__ == "__main__":
    # part_one()
    part_two()
