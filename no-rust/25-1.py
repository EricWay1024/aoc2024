import sys

def read_schematics(file_path):
    """
    Reads the schematics from the input file.
    Each schematic is separated by a blank line.
    Returns a list of schematics, where each schematic is a list of strings.
    """
    with open(file_path, 'r') as f:
        content = f.read()
    schematics = [schem for schem in content.strip().split('\n\n') if schem]
    schematics = [schem.splitlines() for schem in schematics]
    return schematics

def is_lock(schematic):
    """
    Determines if a schematic is a lock.
    A lock has the top row filled with '#' and the bottom row filled with '.'.
    """
    top_row = schematic[0]
    bottom_row = schematic[-1]
    return all(c == '#' for c in top_row) and all(c == '.' for c in bottom_row)

def is_key(schematic):
    """
    Determines if a schematic is a key.
    A key has the top row filled with '.' and the bottom row filled with '#'.
    """
    top_row = schematic[0]
    bottom_row = schematic[-1]
    return all(c == '.' for c in top_row) and all(c == '#' for c in bottom_row)

def compute_lock_heights(schematic, num_cols=5, max_height=5):
    """
    Computes the heights for a lock schematic.
    For each column, counts the number of consecutive '#' characters starting from the second row.
    Stops counting when a '.' is encountered or max_height is reached.
    """
    heights = []
    for c in range(num_cols):
        h = 0
        for r in range(1, len(schematic)-1):  # Exclude the last row (all '.')
            if schematic[r][c] == '#':
                h +=1
                if h == max_height:
                    break
            else:
                break
        heights.append(h)
    return tuple(heights)

def compute_key_heights(schematic, num_cols=5, max_height=5):
    """
    Computes the heights for a key schematic.
    For each column, counts the number of consecutive '#' characters starting from the second last row upwards.
    Stops counting when a '.' is encountered or max_height is reached.
    """
    heights = []
    for c in range(num_cols):
        h = 0
        for r in range(len(schematic)-2, -1, -1):  # Start from second last row up to first row
            if schematic[r][c] == '#':
                h +=1
                if h == max_height:
                    break
            else:
                break
        heights.append(h)
    return tuple(heights)

def main():
    input_file = '../input/25.in'
    schematics = read_schematics(input_file)
    
    locks = []
    keys = []
    
    for schem in schematics:
        if is_lock(schem):
            heights = compute_lock_heights(schem)
            locks.append(heights)
        elif is_key(schem):
            heights = compute_key_heights(schem)
            keys.append(heights)
        else:
            # Invalid schematic, ignore or handle as needed
            pass
    
    # Define the total available space per column
    TOTAL_SPACE = 5
    
    # Count valid lock-key pairs
    valid_pairs = 0
    for lock in locks:
        for key in keys:
            # Check if for all columns, lock_height + key_height <= TOTAL_SPACE
            if all(l + k <= TOTAL_SPACE for l, k in zip(lock, key)):
                valid_pairs +=1
    
    print(valid_pairs)

if __name__ == "__main__":
    main()
