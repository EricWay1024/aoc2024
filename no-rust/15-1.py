def read_input(filename):
    with open(filename, 'r') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

def solve():
    lines = read_input('../input/15.in')
    map_chars = set(['#', '.', 'O', '@'])
    move_chars = set(['^', 'v', '<', '>'])
    
    map_lines = []
    move_lines = []
    
    for line in lines:
        line_set = set(line)
        if len(line_set) == 0:
            continue
        if line_set.issubset(map_chars):
            map_lines.append(line)
        elif line_set.issubset(move_chars):
            move_lines.append(line)
    
    # Now we have map_lines and move_lines.
    # Concatenate all move lines into one string of moves:
    moves = ''.join(move_lines)
    
    # Parse the map
    # We need to find the robot position and box positions
    warehouse = [list(row) for row in map_lines]
    rows = len(warehouse)
    cols = len(warehouse[0]) if rows > 0 else 0
    
    robot_pos = None
    for r in range(rows):
        for c in range(cols):
            if warehouse[r][c] == '@':
                robot_pos = (r, c)
                warehouse[r][c] = '.'
                break
        if robot_pos:
            break
    
    # Directions
    dir_map = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }
    

    # Simulation function
    for move in moves:
        dr, dc = dir_map[move]
        r, c = robot_pos
        nr, nc = r + dr, c + dc
        
        if warehouse[nr][nc] == '#':
            # Can't move
            continue
        
        elif warehouse[nr][nc] == 'O':
            # Need to push boxes
            # Find chain of boxes in that direction
            rr, cc = nr, nc
            while warehouse[rr][cc] == 'O':
                rr += dr
                cc += dc
            
            # rr, cc is the cell after the last box in chain
            if warehouse[rr][cc] == '#':
                continue
            # If warehouse[rr][cc] == '.' means we can push boxes forward
            # Move the boxes from last to first into the free space
            warehouse[rr][cc] = 'O'
            warehouse[nr][nc] = '.'
            robot_pos = (nr, nc)
        else:
            robot_pos = (nr, nc)
    
    # After all moves, sum GPS coordinates of all boxes
    # GPS coordinate = 100 * row_index + col_index
    total = 0
    for r in range(rows):
        for c in range(cols):
            if warehouse[r][c] == 'O':
                total += 100 * r + c
    
    print(total)

if __name__ == '__main__':
    solve()
