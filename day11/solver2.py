def get_two_most_active_monkey_item_count(round_count, monkey_items):
    for round in range(0, round_count):
        print(round)
        for monkey_id in range(0, len(monkey_items)):
            for item in monkey_items[monkey_id]['items']:
                current_total_item_handled = monkey_items[monkey_id].get('total_handled_item', 0)
                current_total_item_handled += 1
                monkey_items[monkey_id]['total_handled_item'] = current_total_item_handled
                item_after_operation = (lambda old: eval(monkey_items[monkey_id]['operation']))(item) % 9_699_690
                # item_after_getting_bored = item_after_operation // 3
                if item_after_operation % monkey_items[monkey_id]['test_divide'] == 0:
                    monkey_items[monkey_items[monkey_id]['target_monkey_if_true']]['items'].append(item_after_operation)
                else:
                    monkey_items[monkey_items[monkey_id]['target_monkey_if_false']]['items'].append(item_after_operation)
            monkey_items[monkey_id]['items'] = []
    list_of_total_items_handled = []
    for done_monkey in monkey_items:
        list_of_total_items_handled.append(done_monkey.get('total_handled_item', 0))
    list_of_total_items_handled.sort(reverse=True)
    return list_of_total_items_handled[0], list_of_total_items_handled[1]


def generate_starting_monkey_state(file):
    monkey_items = []
    current_monkey = {'items': [], 'operation': lambda old: old, 'test_divide': 1, 'target_monkey_if_true': 0, 'target_monkey_if_false': 0}
    current_monkey_index = -1
    for line in file:
        if line == '\n':
            monkey_items.append(current_monkey)
        elif "Monkey " in line:
            current_monkey_index += 1
            current_monkey = {'items': [], 'operation': lambda old: +1, 'test_divide': 1, 'target_monkey_if_true': 0, 'target_monkey_if_false': 0}
        elif line.split(':')[0] == "  Starting items":
            for item in line.split(':')[1].strip().split(", "):
                current_monkey['items'].append(int(item))
        elif line.split(':')[0] == "  Operation":
            function = line.split(':')[1].strip().split('= ')[1]
            current_monkey['operation'] = function
        elif line.split(':')[0] == "  Test":
            current_monkey['test_divide'] = int(line.split('divisible by ')[1].strip())
        elif line.split(':')[0] == "    If true":
            current_monkey['target_monkey_if_true'] = int(line.split('throw to monkey ')[1].strip())
        elif line.split(':')[0] == "    If false":
            current_monkey['target_monkey_if_false'] = int(line.split('throw to monkey ')[1].strip())
    monkey_items.append(current_monkey)
    return monkey_items


def solve():
    with open('input/input1', 'r') as file:
        monkey_items = generate_starting_monkey_state(file)
        result1, result2 = get_two_most_active_monkey_item_count(10000, monkey_items)
        result = result1 * result2
        print("=== Result ===")
        print(result)
        print("==============")


if __name__ == '__main__':
    solve()
