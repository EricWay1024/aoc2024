import re

def parse_input(file_path):
    initial_wires = {}
    gates = []

    with open(file_path, 'r') as file:
        lines = file.read().splitlines()

    # Separate initial wire values and gate definitions
    # Assuming that initial wire values are listed first, followed by gate definitions
    # We'll find the first line that does not match 'wire: value' pattern
    wire_value_pattern = re.compile(r'^(\w+):\s*([01])$')
    gate_pattern = re.compile(r'^(\w+)\s+(AND|OR|XOR)\s+(\w+)\s+->\s+(\w+)$')

    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if not line:
            index += 1
            continue
        if wire_value_pattern.match(line):
            match = wire_value_pattern.match(line)
            wire = match.group(1)
            value = int(match.group(2))
            initial_wires[wire] = value
            index += 1
        else:
            break

    # The rest are gate definitions
    while index < len(lines):
        line = lines[index].strip()
        if not line:
            index += 1
            continue
        match = gate_pattern.match(line)
        if match:
            input1 = match.group(1)
            operation = match.group(2)
            input2 = match.group(3)
            output = match.group(4)
            if input1 > input2:
                input1, input2 = input2, input1
            gates.append( (input1, operation, input2, output) )
        else:
            raise ValueError(f"Invalid gate definition: {line}")
        index += 1

    return initial_wires, gates


def get_gate(wire):
    for gate in gates:
        input1, operation, input2, output = gate
        if output == wire:
            return gate


def print_input_if_false(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not result:  # If the result is False
            print(f"Function called with input: {args}")
        return result
    return wrapper


@print_input_if_false
def check_dependency(wire, cur, expected_status):
    """Check the given wire at position cur implements a half adder (if cur = 0) or a full adder (if cur >= 1)"""
    if expected_status == 'input':
        return (wire in initial_wires) and (wire == f"x{cur:02}" or wire == f"y{cur:02}")
    
    input1, operation, input2, _ = get_gate(wire)

    if expected_status == 'sum':
        if cur == 0:
            return operation == 'XOR' and check_dependency(input1, 0, 'input') and check_dependency(input2, 0, 'input')
        else:
            return operation == 'XOR' and ((
                check_dependency(input1, cur, 'bit_xor') and check_dependency(input2, cur - 1, 'carry')
            ) or (
                check_dependency(input2, cur, 'bit_xor') and check_dependency(input1, cur - 1, 'carry')
            ))

    elif expected_status == 'bit_xor':
        return operation == 'XOR' and check_dependency(input1, cur, 'input') and check_dependency(input2, cur, 'input')
    
    elif expected_status == 'carry':
        if cur == 0:
            return operation == 'AND' and check_dependency(input1, cur, 'input') and check_dependency(input2, cur, 'input')
        else:
            return operation == 'OR' and ((
                check_dependency(input1, cur, 'bit_and') and check_dependency(input2, cur, 'carry_and_xor')
            ) or (
                check_dependency(input2, cur, 'bit_and') and check_dependency(input1, cur, 'carry_and_xor')
            ))
    
    elif expected_status == 'bit_and':
        return operation == 'AND' and check_dependency(input1, cur, 'input') and check_dependency(input2, cur, 'input')
    
    elif expected_status == 'carry_and_xor':
        return operation == 'AND' and ((
            check_dependency(input1, cur - 1, 'carry') and check_dependency(input2, cur, 'bit_xor')
        ) or (
            check_dependency(input2, cur - 1, 'carry') and check_dependency(input1, cur, 'bit_xor')
        ))

    else:
        raise ValueError(f'Wrong expected_status {expected_status}')

# def print_dependency(wire):
#     if wire in initial_wires:
#         return
    
#     for gate in gates:
#         input1, operation, input2, output = gate
#         if output == wire:
#             print(gate)
#             print_dependency(initial_wires, gates, input1)
#             print_dependency(initial_wires, gates, input2)


input_file = '../input/24-new.in'
initial_wires, gates = parse_input(input_file)

for i in range(46):
    s = check_dependency(f'z{i:02}', i, 'sum')
    print(s)
    if not s:
        print(i)
        break


# The idea is doing this manually...
# We use the function check_dependency to spot any errors
# Then we try to fix the bugs manually by doing some mental maths and changing the input
# Then rerun this script to spot the next error and so on
# There are only four pairs so this is not too much work... Much less than trying to find a general algrorithm...
# Note that check_dependency does not consider the highest position (45) so it will give you an error, just ignore it