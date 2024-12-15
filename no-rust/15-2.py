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
            map_lines.append(line.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.'))
        elif line_set.issubset(move_chars):
            move_lines.append(line)
    
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
    
    def push_boxes(x, y, dx, dy):
        nx, ny = x + dx, y + dy
        res = []
        if warehouse[nx][ny] == ']':
            q = [(nx, ny - 1)]
        else:
            q = [(nx, ny)]

        while q:
            xx, yy = q[-1]
            q.pop()

            lx, ly = xx, yy
            rx, ry = xx, yy + 1
            
            res.append((lx, ly, '['))
            res.append((rx, ry, ']'))

            lc = warehouse[lx + dx][ly + dy]
            rc = warehouse[rx + dx][ry + dy]

            if '#' in [lc, rc]:
                return False

            if dx == 0 and dy == 1:
                if rc == '[':
                    q.append((rx + dx, ry + dy))
 
            elif dx == 0 and dy == -1:
                if lc == ']':
                    q.append((lx + dx, ly + dy - 1))
            else:
                if lc == '[':
                    q.append((lx + dx, ly + dy))
                elif lc == ']':
                    q.append((lx + dx, ly + dy - 1))
                
                if rc == '[':
                    q.append((rx + dx, ry + dy))
        
        for (x, y, t) in res:
            warehouse[x][y] = '.'
        
        for (x, y, t) in res:
            warehouse[x + dr][y + dc] = t

        return True
    
    # Simulation function
    for move in enumerate(moves):
        dr, dc = dir_map[move]
        r, c = robot_pos
        nr, nc = r + dr, c + dc
        
        if warehouse[nr][nc] == '#':
            # Can't move
            continue
        
        elif warehouse[nr][nc] in ["]", "["]:
            if push_boxes(r, c, dr, dc):
                robot_pos = (nr, nc)
        else:
            robot_pos = (nr, nc)
        

    # After all moves, sum GPS coordinates of all boxes
    # GPS coordinate = 100 * row_index + col_index
    total = 0
    for r in range(rows):
        for c in range(cols):
            if warehouse[r][c] == '[':
                total += 100 * r + c
    
    print(total)

if __name__ == '__main__':
    solve()
