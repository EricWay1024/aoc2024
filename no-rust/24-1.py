# This file in its entirety is ChatGPT o1's work
# What a miracle...
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
            gates.append( (input1, operation, input2, output) )
        else:
            raise ValueError(f"Invalid gate definition: {line}")
        index += 1

    return initial_wires, gates

def compute_gate(op, val1, val2):
    if op == 'AND':
        return val1 & val2
    elif op == 'OR':
        return val1 | val2
    elif op == 'XOR':
        return val1 ^ val2
    else:
        raise ValueError(f"Unknown operation: {op}")

def simulate_wires(initial_wires, gates):
    wires = dict(initial_wires)
    gates_remaining = gates.copy()
    progress = True

    while gates_remaining and progress:
        progress = False
        gates_to_remove = []
        for gate in gates_remaining:
            input1, operation, input2, output = gate
            if input1 in wires and input2 in wires:
                val1 = wires[input1]
                val2 = wires[input2]
                output_val = compute_gate(operation, val1, val2)
                wires[output] = output_val
                gates_to_remove.append(gate)
                progress = True
        for gate in gates_to_remove:
            gates_remaining.remove(gate)

    if gates_remaining:
        raise ValueError("Could not resolve all gates. Possible missing inputs or cyclic dependencies.")

    return wires

def collect_z_wires(wires):
    z_wires = {}
    z_pattern = re.compile(r'^z(\d+)$')
    for wire, value in wires.items():
        match = z_pattern.match(wire)
        if match:
            index = int(match.group(1))
            z_wires[index] = value
    if not z_wires:
        raise ValueError("No wires starting with 'z' found.")
    # Sort by index in descending order to have z12 (MSB) first
    sorted_indices = sorted(z_wires.keys(), reverse=True)
    # Assemble binary string with z12 as MSB and z00 as LSB
    binary_bits = [str(z_wires[i]) for i in sorted_indices]
    binary_str = ''.join(binary_bits)
    # Convert binary string to decimal
    decimal_number = int(binary_str, 2)
    return decimal_number

def main():
    input_file = '../input/24.in'  # Adjust the path as needed
    initial_wires, gates = parse_input(input_file)
    wires = simulate_wires(initial_wires, gates)
    decimal_output = collect_z_wires(wires)
    print(decimal_output)

if __name__ == "__main__":
    main()
