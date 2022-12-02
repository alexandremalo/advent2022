def define_score_points(elf_play, human_play):
    to_return = 0
    int_elf = ord(elf_play)
    int_human = ord(human_play) - 23
    #Draw
    if int_elf == int_human:
        to_return += 3

    if human_play == 'X':
        to_return += 1
        #Win
        if elf_play == 'C':
            to_return += 6
    elif human_play == 'Y':
        to_return += 2
        #Win
        if elf_play == 'A':
            to_return += 6
    elif human_play == 'Z':
        to_return += 3
        #Win
        if elf_play == 'B':
            to_return += 6
    return to_return



def solve():
    with open('input/input1', 'r') as file:
        total_score = 0
        for line in file:
            array_value = line.split()
            elf_play, human_play = array_value[0], array_value[1]
            total_score += define_score_points(elf_play, human_play)
        print("=== Result ===")
        print(total_score)
        print("==============")

if __name__ == '__main__':
    solve()
