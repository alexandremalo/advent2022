def define_score_points(elf_play, outcome):
    to_return = 0
    int_flatted_elf_play = ord(elf_play) - 65
    if outcome == 'Y':
        to_return += 3
        to_return += int_flatted_elf_play + 1
    elif outcome == 'Z':
        to_return += 6
        to_return += (int_flatted_elf_play + 1) % 3 + 1
    elif outcome == 'X':
        to_return += 0
        to_return += (int_flatted_elf_play - 1) % 3 + 1
    return to_return



def solve():
    with open('input/input1', 'r') as file:
        total_score = 0
        for line in file:
            array_value = line.split()
            elf_play, outcome = array_value[0], array_value[1]
            total_score += define_score_points(elf_play, outcome)
        print("=== Result ===")
        print(total_score)
        print("==============")

if __name__ == '__main__':
    solve()
