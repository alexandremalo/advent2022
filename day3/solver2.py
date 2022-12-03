def find_char_priority(char):
    if ord(char) >= 97:
        return ord(char) - 96
    else:
        return ord(char) - 38


def find_common_item_in_group(array_of_backpack):
    common_char = ''
    backpack_one = array_of_backpack[0]
    backpack_two = array_of_backpack[1]
    backpack_three = array_of_backpack[2]
    for char_one in backpack_one:
        if char_one in backpack_two:
            if char_one in backpack_three:
                common_char = char_one
                break
    return find_char_priority(common_char)


def solve():
    with open('input/input1', 'r') as file:
        total_priority = 0
        elf_in_same_group_counter = 0
        elf_group_backpacks = []
        for line in file:
            elf_in_same_group_counter += 1
            elf_group_backpacks.append(line.strip())
            if elf_in_same_group_counter == 3:
                total_priority += find_common_item_in_group(elf_group_backpacks)
                elf_in_same_group_counter = 0
                elf_group_backpacks = []
        print("=== Result ===")
        print(total_priority)
        print("==============")


if __name__ == '__main__':
    solve()
