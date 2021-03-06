f = open("input.txt", "r")
f_input = [int(x) for x in f.read().split(",")]

increments = {"1": 4, "2": 4, "3": 2, "4": 2, "5": 0, "6": 0, "7": 4, "8": 4}


def parse_instruction(instruction):
    opcode = instruction[-2:].replace("0", "")
    mode_1 = instruction[-3:-2] if len(instruction) > 2 else "0"
    mode_2 = "1" if len(instruction) == 4 else "0"
    return (opcode, mode_1, mode_2)


def parse_params(code, opcode, i, mode_1, mode_2):
    par_1 = code[i + 1] if mode_1 == "1" else code[code[i + 1]]
    try:
        par_2 = code[i + 2] if mode_2 == "1" else code[code[i + 2]]
        return (par_1, par_2)
    except Exception:
        return (par_1, None)


def run_intcode(code, p_input):
    output = 0
    i = 0
    while code[i] != 99:
        opcode, mode_1, mode_2 = parse_instruction(str(code[i]))
        par_1, par_2 = parse_params(code, opcode, i, mode_1, mode_2)

        if opcode == "1":
            code[code[i + 3]] = par_1 + par_2

        if opcode == "2":
            code[code[i + 3]] = par_1 * par_2

        if opcode == "3":
            code[code[i + 1]] = p_input

        if opcode == "4":
            output = par_1
            print(output)

        if opcode == "5":
            i = par_2 if not par_1 == 0 else i + 3

        if opcode == "6":
            i = par_2 if par_1 == 0 else i + 3

        if opcode == "7":
            code[code[i + 3]] = 1 if par_1 < par_2 else 0

        if opcode == "8":
            code[code[i + 3]] = 1 if par_1 == par_2 else 0

        i += increments[opcode]

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
