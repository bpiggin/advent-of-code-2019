from itertools import groupby


def count_passwords(start, end):
    count = 0
    for i in range(start, end + 1):
        j = str(i)
        if j == "".join(sorted(j)) and len([k for k, g in groupby(j)]) != 6:
            count += 1
    return count


def part_one():
    count = count_passwords(240298, 784956)
    return count


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    print(part_one())
    # print(part_two())
