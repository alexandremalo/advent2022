def find_char_priority(char):
    if ord(char) >= 97:
        return ord(char) - 96
    else:
        return ord(char) - 38

def find_common_char(string_one, string_two):
    common_char = ''
    for char_one in string_one:
        if char_one in string_two:
            common_char = char_one
            break
    return find_char_priority(common_char)




def solve():
    with open('input/input1', 'r') as file:
        total_priority = 0
        for line in file:
            backpack_string = line.strip()
            half_backpack_size = int(len(backpack_string) / 2)
            first_compartment = backpack_string[:-half_backpack_size]
            second_compartment = backpack_string[half_backpack_size:]
            total_priority += find_common_char(first_compartment, second_compartment)
        print("=== Result ===")
        print(total_priority)
        #print(find_char_priority('A'))
        #print(find_char_priority('Z'))
        #print(find_char_priority('a'))
        #print(find_char_priority('z'))
        print("==============")

if __name__ == '__main__':
    solve()
