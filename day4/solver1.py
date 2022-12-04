def array_contains_other(start_one, end_one, start_two, end_two):
    to_return = False
    if start_one <= start_two and end_two <= end_one :
        to_return = True
    elif start_two <= start_one and end_one <= end_two:
        to_return = True
    return to_return



def solve():
    with open('input/input1', 'r') as file:
        total_full_duplicate_work = 0
        for line in file:
            pair_of_assignment = line.strip().split(',')
            elf_one_assignment = pair_of_assignment[0].split('-')
            elf_one_start_index = int(elf_one_assignment[0])
            elf_one_end_index = int(elf_one_assignment[1])
            elf_two_assignment = pair_of_assignment[1].split('-')
            elf_two_start_index = int(elf_two_assignment[0])
            elf_two_end_index = int(elf_two_assignment[1])
            if array_contains_other(elf_one_start_index, elf_one_end_index, elf_two_start_index, elf_two_end_index):
                total_full_duplicate_work += 1
        print("=== Result ===")
        print(total_full_duplicate_work)
        #print(elf_one_start_index)
        #print(elf_one_end_index)
        #print(elf_two_start_index)
        #print(elf_two_end_index)
        print("==============")

if __name__ == '__main__':
    solve()
